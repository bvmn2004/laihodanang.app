import csv
import glob
import os
import sys
import re
import json
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

def normalize_text(text):
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def classify_intent(kw, orig_intent):
    kw_l = kw.lower()
    if any(x in kw_l for x in ['giá', 'bảng giá', 'nhiêu tiền', 'chi phí', 'so sánh', 'review', 'tốt nhất', 'uy tín']):
        return "Thương mại (Commercial)"
    if any(x in kw_l for x in ['đặt', 'gọi', 'thuê', 'số điện thoại', 'hotline', 'liên hệ', 'bạn uống tôi lái', '24/7', '247', 'đón']):
        return "Giao dịch (Transactional)"
    if any(x in kw_l for x in ['là gì', 'như thế nào', 'thế nào', 'kinh nghiệm', 'lưu ý', 'cần chuẩn bị', 'quy trình', 'có nên', 'buồn ngủ', 'mệt mỏi', 'uống rượu', 'nồng độ cồn', 'khác']):
        return "Thông tin (Informational)"
    if any(x in kw_l for x in ['tuyển', 'việc làm', 'đăng ký lái', 'làm tài xế', 'hồ sơ', 'bằng lái', 'học lái']):
        return "Tuyển dụng / Điều hướng (Non-target / Exclude)"
    if 'Giao dịch' in orig_intent:
        return "Giao dịch (Transactional)"
    if 'Thương mại' in orig_intent:
        return "Thương mại (Commercial)"
    if 'Thông tin' in orig_intent:
        return "Thông tin (Informational)"
    return "Giao dịch (Transactional)"

def assign_cluster_and_url(kw):
    kw_l = kw.lower()
    
    # Excluded keywords
    if any(x in kw_l for x in ['tuyển', 'việc làm', 'đăng ký lái', 'làm tài xế', 'hồ sơ', 'thi bằng', 'học lái']):
        return "Excluded", "None", "None", "Lạc đề - tuyển dụng/đào tạo"

    # Route / Local
    if 'hội an' in kw_l:
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/da-nang-di-hoi-an/", "Khu vực / Tuyến đường", "Tuyến Đà Nẵng đi Hội An"
    if 'huế' in kw_l:
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/da-nang-di-hue/", "Khu vực / Tuyến đường", "Tuyến Đà Nẵng đi Huế"
    if 'quảng ngãi' in kw_l:
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/da-nang-di-quang-ngai/", "Khu vực / Tuyến đường", "Tuyến Đà Nẵng đi Quảng Ngãi"
    if 'hải châu' in kw_l:
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/hai-chau/", "Khu vực / Địa phương", "Quận Hải Châu Đà Nẵng"
    if 'sơn trà' in kw_l:
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/son-tra/", "Khu vực / Địa phương", "Quận Sơn Trà Đà Nẵng"
    if any(x in kw_l for x in ['thanh khê', 'liên chiểu', 'ngũ hành sơn', 'cẩm lệ', 'hòa vang', 'khu vực']):
        return "Nhóm F - Địa phương & Tuyến đường", "/khu-vuc/", "Khu vực / Tổng hợp", "Khu vực phục vụ tại Đà Nẵng"

    # Vehicles
    if any(x in kw_l for x in ['xe máy', 'xe may', 'hai bánh']):
        return "Nhóm D - Loại phương tiện", "/dich-vu/lai-xe-ho-xe-may/", "Dịch vụ", "Lái xe máy hộ Đà Nẵng"
    if any(x in kw_l for x in ['ô tô', 'oto', 'xe hơi', 'xe con', '4 chỗ', '7 chỗ']):
        return "Nhóm D - Loại phương tiện", "/dich-vu/lai-xe-ho-o-to/", "Dịch vụ", "Lái ô tô hộ Đà Nẵng"

    # Special needs
    if any(x in kw_l for x in ['đi tỉnh', 'đường dài', 'về quê', 'liên tỉnh']):
        return "Nhóm G - Nhu cầu đặc biệt", "/dich-vu/thue-tai-xe-di-tinh/", "Dịch vụ", "Thuê tài xế đi tỉnh"
    if any(x in kw_l for x in ['giao xe', 'nhận xe', 'giao nhận', 'đưa xe về gara', 'đưa xe đi đăng kiểm']):
        return "Nhóm G - Nhu cầu đặc biệt", "/dich-vu/thue-tai-xe-giao-nhan-xe/", "Dịch vụ", "Giao nhận xe theo yêu cầu"
    if any(x in kw_l for x in ['đối tác', 'khách vip', 'chuyên gia', 'sếp', 'doanh nghiệp']):
        return "Nhóm G - Nhu cầu đặc biệt", "/dich-vu/thue-tai-xe-dua-don-doi-tac/", "Dịch vụ", "Đưa đón đối tác"
    if any(x in kw_l for x in ['cưới', 'tiệc cưới', 'sự kiện', 'hội nghị', 'event']):
        return "Nhóm G - Nhu cầu đặc biệt", "/dich-vu/thue-tai-xe-tiec-cuoi-su-kien/", "Dịch vụ", "Phục vụ cưới hỏi sự kiện"

    # Time & pricing
    if any(x in kw_l for x in ['theo giờ', 'theo tieng', 'mấy tiếng']):
        return "Nhóm E - Thời gian & Bảng giá", "/dich-vu/thue-tai-xe-theo-gio/", "Dịch vụ", "Thuê tài xế theo giờ"
    if any(x in kw_l for x in ['theo ngày', 'nguyên ngày', 'trong ngày']):
        return "Nhóm E - Thời gian & Bảng giá", "/dich-vu/thue-tai-xe-theo-ngay/", "Dịch vụ", "Thuê tài xế theo ngày"
    if any(x in kw_l for x in ['giá', 'bảng giá', 'nhiêu tiền', 'chi phí', '150k', 'cước phí', 'giá rẻ', 'bao nhiêu']):
        return "Nhóm E - Thời gian & Bảng giá", "/bang-gia/", "Bảng giá", "Bảng giá lái xe hộ Đà Nẵng"

    # Alcohol & After party
    if any(x in kw_l for x in ['bạn uống tôi lái', 'uống say', 'người say', 'say rượu', 'uống rượu', 'uống bia', 'sau tiệc', 'quán nhậu', 'về nhà an toàn']):
        if 'bạn uống tôi lái' in kw_l:
            return "Nhóm C - Rượu bia & Sau tiệc", "/dich-vu/ban-uong-toi-lai/", "Dịch vụ", "Bạn uống tôi lái Đà Nẵng"
        return "Nhóm C - Rượu bia & Sau tiệc", "/dich-vu/lai-xe-ho-sau-tiec/", "Dịch vụ", "Lái xe hộ sau tiệc / say rượu"

    # Informational / Blog questions
    if 'là gì' in kw_l:
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/lai-xe-ho-la-gi/", "Blog / Bài viết", "Lái xe hộ là gì"
    if any(x in kw_l for x in ['taxi', 'so sánh taxi', 'grab']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/lai-xe-ho-va-taxi-nen-chon-gi/", "Blog / Bài viết", "So sánh Lái xe hộ vs Taxi"
    if any(x in kw_l for x in ['khi nào', 'trường hợp nào', 'lý do']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/khi-nao-nen-goi-tai-xe-lai-ho/", "Blog / Bài viết", "Khi nào nên gọi tài xế"
    if any(x in kw_l for x in ['chuẩn bị', 'bàn giao', 'thủ tục giao xe']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/chuan-bi-khi-ban-giao-xe/", "Blog / Bài viết", "Chuẩn bị gì khi bàn giao xe"
    if any(x in kw_l for x in ['ban đêm', 'nửa đêm', 'khuya', '24h', '24/7 đêm']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/dat-tai-xe-lai-ho-ban-dem/", "Blog / Bài viết", "Đặt tài xế ban đêm"
    if any(x in kw_l for x in ['buồn ngủ', 'mệt mỏi', 'không tỉnh táo']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/buon-ngu-khi-lai-xe/", "Blog / Bài viết", "Buồn ngủ khi lái xe"
    if any(x in kw_l for x in ['xe máy mang theo', 'xe máy gửi lại', 'quán giữ xe']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/uong-ruou-bia-mang-theo-xe-may/", "Blog / Bài viết", "Uống rượu mang theo xe máy"
    if any(x in kw_l for x in ['đi tiệc bằng ô tô', 'dự tiệc ô tô']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/di-tiec-bang-o-to-da-nang/", "Blog / Bài viết", "Kinh nghiệm đi tiệc ô tô Đà Nẵng"
    if any(x in kw_l for x in ['giờ hay theo ngày', 'chọn theo giờ']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/thue-tai-xe-theo-gio-hay-theo-ngay/", "Blog / Bài viết", "Thuê theo giờ hay theo ngày"
    if any(x in kw_l for x in ['tự lái', 'thuê xe tự lái']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/thue-xe-tu-lai-goi-tai-xe/", "Blog / Bài viết", "Thuê xe tự lái gọi tài xế lái thay"
    if any(x in kw_l for x in ['quy trình', 'cách đặt', 'hướng dẫn đặt']):
        return "Nhóm H - Bài viết & Cẩm nang", "/blog/quy-trinh-dat-tai-xe-nhu-y-driver/", "Blog / Bài viết", "Quy trình đặt tài xế Như Ý Driver"

    # Booking & Call intent
    if any(x in kw_l for x in ['gọi', 'đặt', 'liên hệ', 'hotline', 'số điện thoại']):
        return "Nhóm B - Ý định đặt dịch vụ", "/lien-he/", "Liên hệ", "Liên hệ & Gọi đặt tài xế"

    # Core Driving Service
    if any(x in kw_l for x in ['lái xe hộ đà nẵng', 'dịch vụ lái xe hộ', 'thuê tài xế đà nẵng', 'tài xế lái hộ', 'lái hộ']):
        return "Nhóm A - Dịch vụ chính", "/", "Trang chủ", "Trang chủ Lái Xe Hộ Đà Nẵng"

    return "Nhóm A - Dịch vụ chính", "/", "Trang chủ", "Trang chủ Lái Xe Hộ Đà Nẵng"

def get_page_seo_meta(target_url):
    seo_meta = {
        "/": {
            "title": "Lái Xe Hộ Đà Nẵng Giá Chỉ Từ 150K | Như Ý Driver Phục Vụ 24/7",
            "h1": "LÁI XE HỘ ĐÀ NẴNG – GIÁ CHỈ TỪ 150K",
            "meta_desc": "Dịch vụ lái xe hộ ô tô & xe máy tại Đà Nẵng uy tín 24/7. Tài xế lái chính xe của bạn đưa cả người và xe về an toàn. Giá ô tô từ 150K. Gọi ngay 0985 666 044.",
            "priority": "High"
        },
        "/gioi-thieu/": {
            "title": "Giới Thiệu Như Ý Driver | Dịch Vụ Lái Xe Hộ Chuyên Nghiệp Đà Nẵng",
            "h1": "Về Như Ý Driver – Dịch Vụ Lái Xe Hộ Uy Tín Tại Đà Nẵng",
            "meta_desc": "Đội ngũ tài xế chuyên nghiệp, lịch sự, thông thạo đường phố Đà Nẵng. Cam kết an toàn, phục vụ tận tâm 24/7 cho cả ô tô và xe máy.",
            "priority": "Medium"
        },
        "/dich-vu/": {
            "title": "Dịch Vụ Lái Xe Hộ Tại Đà Nẵng | Ô Tô, Xe Máy, Theo Giờ & Đi Tỉnh",
            "h1": "Hệ Thống Dịch Vụ Lái Xe Hộ Chuyên Nghiệp Tại Đà Nẵng",
            "meta_desc": "Tổng hợp các dịch vụ lái xe hộ của Như Ý Driver: lái hộ ô tô, xe máy, đưa người say về nhà, thuê tài xế theo giờ, theo ngày, đi tỉnh. Phục vụ 24/7.",
            "priority": "High"
        },
        "/dich-vu/lai-xe-ho-o-to/": {
            "title": "Dịch Vụ Lái Xe Hộ Ô Tô Đà Nẵng Giá Từ 150K | Có Mặt Sau 15-20 Phút",
            "h1": "Dịch Vụ Lái Xe Hộ Ô Tô Đà Nẵng – Giá Chỉ Từ 150.000đ",
            "meta_desc": "Lái xe hộ ô tô nội thành Đà Nẵng giá chỉ từ 150K (0-5km). Tài xế lái vững mọi dòng xe số sàn, số tự động, xe sang. Có mặt sau 15-20 phút.",
            "priority": "High"
        },
        "/dich-vu/lai-xe-ho-xe-may/": {
            "title": "Dịch Vụ Lái Xe Hộ Xe Máy Đà Nẵng Giá Từ 110K | Đưa Khách & Xe Về Nhà",
            "h1": "Dịch Vụ Lái Xe Hộ Xe Máy Đà Nẵng – Giá Chỉ Từ 110.000đ",
            "meta_desc": "Đã uống rượu bia có xe máy? Như Ý Driver nhận lái xe máy đưa bạn và xe về tận nhà an toàn. Giá từ 110.000đ (0-5km). Phục vụ 24/7 khắp Đà Nẵng.",
            "priority": "High"
        },
        "/dich-vu/ban-uong-toi-lai/": {
            "title": "Bạn Uống Tôi Lái Đà Nẵng 24/7 | Đưa Cả Người Và Xe Về An Toàn",
            "h1": "Dịch Vụ Bạn Uống Tôi Lái Đà Nẵng – An Tâm Mọi Cuộc Vui",
            "meta_desc": "Dịch vụ Bạn uống tôi lái tại Đà Nẵng 24/7. Không lo nồng độ cồn, không để xe lại quán. Tài xế lịch sự, an toàn. Gọi 0985 666 044 có mặt ngay.",
            "priority": "High"
        },
        "/dich-vu/lai-xe-ho-sau-tiec/": {
            "title": "Lái Xe Hộ Sau Tiệc & Đưa Người Say Về Nhà An Toàn Tại Đà Nẵng",
            "h1": "Lái Xe Hộ Sau Tiệc – Đưa Người Và Xe Về Nhà Bình An",
            "meta_desc": "Giải pháp đưa người say về nhà an toàn sau tiệc tùng, tiếp khách tại Đà Nẵng. Tài xế chu đáo, hỗ trợ tận tâm, bảo vệ tuyệt đối phương tiện của bạn.",
            "priority": "High"
        },
        "/dich-vu/thue-tai-xe-theo-gio/": {
            "title": "Thuê Tài Xế Theo Giờ Tại Đà Nẵng | Linh Hoạt Theo Lịch Trình Riêng",
            "h1": "Thuê Tài Xế Theo Giờ Tại Đà Nẵng – Linh Hoạt & Tiện Lợi",
            "meta_desc": "Dịch vụ thuê tài xế riêng theo giờ tại Đà Nẵng. Phù hợp tiếp khách, di chuyển nhiều điểm, đi sự kiện. Tài xế lịch thiệp, thông thạo đường phố.",
            "priority": "Medium"
        },
        "/dich-vu/thue-tai-xe-theo-ngay/": {
            "title": "Thuê Tài Xế Theo Ngày Tại Đà Nẵng | Công Tác, Du Lịch, City Tour",
            "h1": "Thuê Tài Xế Theo Ngày Tại Đà Nẵng – Phục Vụ Trọn Gói Theo Lịch Trình",
            "meta_desc": "Thuê tài xế lái xe theo ngày tại Đà Nẵng cho chuyến công tác, du lịch gia đình, tiếp đối tác. Chủ động lịch trình, tài xế chuyên nghiệp, đúng giờ.",
            "priority": "Medium"
        },
        "/dich-vu/thue-tai-xe-di-tinh/": {
            "title": "Thuê Tài Xế Lái Xe Đi Tỉnh Từ Đà Nẵng | Hội An, Huế, Quảng Ngãi",
            "h1": "Thuê Tài Xế Lái Xe Đi Tỉnh Xuất Phát Từ Đà Nẵng",
            "meta_desc": "Thuê tài xế lái xe đường dài, đi tỉnh xuất phát từ Đà Nẵng (Hội An, Huế, Quảng Nam, Quảng Ngãi...). Báo giá trọn gói minh bạch, an toàn tuyệt đối.",
            "priority": "Medium"
        },
        "/dich-vu/thue-tai-xe-giao-nhan-xe/": {
            "title": "Dịch Vụ Thuê Tài Xế Giao Nhận Xe Đà Nẵng | Đưa Xe Gara, Đăng Kiểm",
            "h1": "Dịch Vụ Thuê Tài Xế Giao Nhận Xe Tại Đà Nẵng",
            "meta_desc": "Nhận giao nhận ô tô, đưa xe đi bảo dưỡng gara, đăng kiểm, chuyển xe về nhà cho khách hàng bận rộn. Bàn giao biên bản rõ ràng, bảo hiểm an tâm.",
            "priority": "Low"
        },
        "/dich-vu/thue-tai-xe-dua-don-doi-tac/": {
            "title": "Thuê Tài Xế Đưa Đón Đối Tác Đà Nẵng | Chuyên Nghiệp, Bảo Mật",
            "h1": "Thuê Tài Xế Đưa Đón Đối Tác & Khách VIP Tại Đà Nẵng",
            "meta_desc": "Dịch vụ tài xế lái xe riêng đưa đón đối tác, chuyên gia, lãnh đạo tại Đà Nẵng. Tác phong lịch thiệp, đón sân bay đúng giờ, bảo mật thông tin tối đa.",
            "priority": "Medium"
        },
        "/dich-vu/thue-tai-xe-tiec-cuoi-su-kien/": {
            "title": "Thuê Tài Xế Phục Vụ Tiệc Cưới & Sự Kiện Đà Nẵng | Chu Đáo 24/7",
            "h1": "Tài Xế Phục Vụ Tiệc Cưới, Hội Nghị & Sự Kiện Tại Đà Nẵng",
            "meta_desc": "Dịch vụ tài xế phục vụ tiệc cưới, xe hoa, đoàn rước dâu và sự kiện tại Đà Nẵng. Đảm bảo lịch trình chỉn chu, hỗ trợ khách mời về nhà an toàn.",
            "priority": "Low"
        },
        "/bang-gia/": {
            "title": "Bảng Giá Lái Xe Hộ Đà Nẵng 2026 | Ô Tô Từ 150K, Xe Máy Từ 110K",
            "h1": "Bảng Giá Dịch Vụ Lái Xe Hộ Đà Nẵng Mới Nhất 2026",
            "meta_desc": "Bảng giá lái xe hộ Đà Nẵng công khai, minh bạch: Ô tô từ 150.000đ (0-5km), Xe máy từ 110.000đ (0-5km). Phụ phí đêm sau 23h +50.000đ. Không phí ẩn.",
            "priority": "High"
        },
        "/khu-vuc/": {
            "title": "Khu Vực Phục Vụ Lái Xe Hộ Đà Nẵng | Có Mặt Nhanh 15-20 Phút",
            "h1": "Khu Vực Phục Vụ Lái Xe Hộ Khắp Đà Nẵng 24/7",
            "meta_desc": "Như Ý Driver phục vụ lái xe hộ tại tất cả quận huyện Đà Nẵng: Hải Châu, Sơn Trà, Thanh Khê, Ngũ Hành Sơn, Liên Chiểu, Cẩm Lệ, Hòa Vang. Gọi là có mặt.",
            "priority": "High"
        },
        "/khu-vuc/hai-chau/": {
            "title": "Lái Xe Hộ Hải Châu Đà Nẵng 24/7 | Tài Xế Đến Sau 10-15 Phút",
            "h1": "Dịch Vụ Lái Xe Hộ Quận Hải Châu Đà Nẵng – Phục Vụ 24/7",
            "meta_desc": "Lái xe hộ ô tô & xe máy tại quận Hải Châu (Bạch Đằng, Nguyễn Văn Linh, 2/9, Trần Phú...). Đội ngũ tài xế túc trực trung tâm, có mặt sau 10-15 phút.",
            "priority": "High"
        },
        "/khu-vuc/son-tra/": {
            "title": "Lái Xe Hộ Sơn Trà Đà Nẵng 24/7 | Đón Nhanh Đường Biển Võ Nguyên Giáp",
            "h1": "Dịch Vụ Lái Xe Hộ Quận Sơn Trà Đà Nẵng – An Toàn & Chu Đáo",
            "meta_desc": "Dịch vụ lái xe hộ tại Sơn Trà, tuyến biển Võ Nguyên Giáp, Phạm Văn Đồng, Hồ Nghinh, quán hải sản ven biển. Tài xế lái chính xe của bạn về nhà an toàn.",
            "priority": "High"
        },
        "/khu-vuc/da-nang-di-hoi-an/": {
            "title": "Thuê Tài Xế Đà Nẵng Đi Hội An Trọn Gói | An Toàn, Đúng Giờ",
            "h1": "Thuê Tài Xế Lái Xe Đà Nẵng Đi Hội An – Lịch Trình Theo Yêu Cầu",
            "meta_desc": "Dịch vụ thuê tài xế lái ô tô riêng từ Đà Nẵng đi Hội An và ngược lại. Phù hợp du lịch, công tác, dự tiệc. Báo giá trọn gói minh bạch, tài xế chu đáo.",
            "priority": "Medium"
        },
        "/khu-vuc/da-nang-di-hue/": {
            "title": "Thuê Tài Xế Đà Nẵng Đi Huế An Toàn Qua Đèo Hải Vân / Hầm Hải Vân",
            "h1": "Thuê Tài Xế Đà Nẵng Đi Huế – Tay Lái Vững Đường Đèo & Cao Tốc",
            "meta_desc": "Dịch vụ thuê tài xế lái xe riêng tuyến Đà Nẵng - Huế (qua hầm hoặc đèo Hải Vân). Tài xế giàu kinh nghiệm đường trường, lái cẩn thận, an toàn.",
            "priority": "Medium"
        },
        "/khu-vuc/da-nang-di-quang-ngai/": {
            "title": "Thuê Tài Xế Đà Nẵng Đi Quảng Ngãi | Lái Xe Đường Dài An Toàn",
            "h1": "Thuê Tài Xế Lái Xe Đà Nẵng Đi Quảng Ngãi & Các Tỉnh Miền Trung",
            "meta_desc": "Thuê tài xế lái ô tô đi Quảng Ngãi, Tam Kỳ, Chu Lai xuất phát từ Đà Nẵng. Phục vụ theo lịch trình 1 chiều hoặc khứ hồi trong ngày/nhiều ngày.",
            "priority": "Low"
        },
        "/lien-he/": {
            "title": "Liên Hệ Đặt Tài Xế Lái Xe Hộ Đà Nẵng 24/7 | Như Ý Driver",
            "h1": "Liên Hệ Như Ý Driver – Tổng Đài Lái Xe Hộ Đà Nẵng 24/7",
            "meta_desc": "Cần tài xế lái xe hộ tại Đà Nẵng? Liên hệ hotline 0985 666 044 hoặc Zalo 0985 666 044. Phục vụ 24/7, có mặt sau 15-20 phút.",
            "priority": "High"
        },
        "/blog/": {
            "title": "Cẩm Nang Lái Xe Hộ & An Toàn Giao Thông Đà Nẵng | Như Ý Driver",
            "h1": "Cẩm Nang Kiến Thức Lái Xe Hộ & An Toàn Giao Thông",
            "meta_desc": "Tổng hợp kinh nghiệm gọi tài xế lái hộ, quy định nồng độ cồn, hướng dẫn bàn giao xe và những điều cần biết khi sử dụng dịch vụ lái xe hộ tại Đà Nẵng.",
            "priority": "Medium"
        },
        "/blog/lai-xe-ho-la-gi/": {
            "title": "Lái Xe Hộ Là Gì? Quy Trình Hoạt Động & Khi Nào Nên Sử Dụng | Như Ý Driver",
            "h1": "Lái Xe Hộ Là Gì? Những Điều Cần Biết Trước Khi Đặt Dịch Vụ",
            "meta_desc": "Tìm hiểu chi tiết dịch vụ lái xe hộ là gì, quy trình nhận xe và đưa khách về, ưu điểm so với việc gửi xe qua đêm hay gọi taxi.",
            "priority": "Medium"
        },
        "/blog/lai-xe-ho-va-taxi-nen-chon-gi/": {
            "title": "Lái Xe Hộ Và Taxi: Nên Chọn Dịch Vụ Nào Khi Đi Tiệc? | Như Ý Driver",
            "h1": "Lái Xe Hộ Hay Taxi: Lựa Chọn Nào Tối Ưu Cho Bạn?",
            "meta_desc": "So sánh chi tiết ưu nhược điểm, chi phí và sự tiện lợi giữa việc gọi taxi và thuê tài xế lái chính xe của bạn về nhà sau cuộc vui.",
            "priority": "Medium"
        },
        "/blog/khi-nao-nen-goi-tai-xe-lai-ho/": {
            "title": "7 Trường Hợp Nên Gọi Tài Xế Lái Hộ Thay Vì Cố Tự Lái | Như Ý Driver",
            "h1": "7 Trường Hợp Bạn Nhất Định Nên Gọi Tài Xế Lái Hộ",
            "meta_desc": "Đã uống rượu bia, mệt mỏi, buồn ngủ hay đường xa không quen? Đừng mạo hiểm tự cầm lái. Hãy xem ngay 7 thời điểm cần gọi tài xế lái hộ.",
            "priority": "Medium"
        },
        "/blog/quy-trinh-dat-tai-xe-nhu-y-driver/": {
            "title": "Hướng Dẫn Quy Trình Đặt Tài Xế Như Ý Driver Nhanh Chóng Trong 3 Bước",
            "h1": "Hướng Dẫn Quy Trình Đặt Tài Xế Lái Hộ Tại Như Ý Driver",
            "meta_desc": "Chỉ với 3 bước đơn giản qua Hotline hoặc Zalo 0985 666 044, tài xế Như Ý Driver sẽ có mặt sau 15-20 phút để lái xe đưa bạn về nhà.",
            "priority": "Medium"
        },
        "/blog/chuan-bi-khi-ban-giao-xe/": {
            "title": "Cần Chuẩn Bị Gì Khi Bàn Giao Xe Cho Tài Xế Lái Hộ? | Như Ý Driver",
            "h1": "Cần Chuẩn Bị Gì Khi Bàn Giao Xe Cho Tài Xế Lái Hộ?",
            "meta_desc": "Checklist quan trọng khi giao xe cho tài xế lái hộ: kiểm tra chìa khóa, tư trang cá nhân, tình trạng ngoại thất và thống nhất điểm đến.",
            "priority": "Medium"
        },
        "/blog/dat-tai-xe-lai-ho-ban-dem/": {
            "title": "Kinh Nghiệm Đặt Tài Xế Lái Hộ Ban Đêm An Toàn Tại Đà Nẵng | Như Ý Driver",
            "h1": "Kinh Nghiệm Đặt Tài Xế Lái Hộ Ban Đêm Tại Đà Nẵng",
            "meta_desc": "Những lưu ý quan trọng khi gọi tài xế đêm khuya: phụ phí giờ khuya sau 23h, cách nhận diện tài xế mặc đồng phục và bảo vệ an toàn cá nhân.",
            "priority": "Medium"
        },
        "/blog/buon-ngu-khi-lai-xe/": {
            "title": "Buồn Ngủ Khi Lái Xe Ban Đêm: Cách Xử Lý An Toàn Nhất | Như Ý Driver",
            "h1": "Buồn Ngủ Khi Đang Lái Xe? Dừng Đúng Lúc Để Bảo Đảm An Toàn",
            "meta_desc": "Cơn buồn ngủ khi lái xe nguy hiểm không kém say rượu bia. Học cách nhận biết dấu hiệu buồn ngủ và phương án gọi tài xế lái thay kịp thời.",
            "priority": "Medium"
        },
        "/blog/uong-ruou-bia-mang-theo-xe-may/": {
            "title": "Uống Rượu Bia Nhưng Đi Xe Máy: Giải Pháp Đưa Cả Người Và Xe Về Nhà",
            "h1": "Đã Uống Rượu Bia Nhưng Có Xe Máy? Giải Pháp Đưa Cả Người & Xe Về",
            "meta_desc": "Đi nhậu bằng xe máy không thể tự lái về? Thay vì gửi lại quán tốn kém và lo mất trộm, hãy gọi dịch vụ lái xe máy hộ đưa cả bạn và xe về tận ngõ.",
            "priority": "Medium"
        },
        "/blog/di-tiec-bang-o-to-da-nang/": {
            "title": "Kinh Nghiệm Đi Tiệc Bằng Ô Tô Tại Đà Nẵng & Phương Án Về Nhà An Toàn",
            "h1": "Đi Tiệc Bằng Ô Tô Tại Đà Nẵng: Bí Quyết Về Nhà Thảnh Thơi",
            "meta_desc": "Làm sao để vừa đi ô tô lịch thiệp đến tiệc cưới, sự kiện mà không phải lo nghĩ lúc về? Đặt trước tài xế lái xe hộ là giải pháp tối ưu nhất.",
            "priority": "Medium"
        },
        "/blog/thue-tai-xe-theo-gio-hay-theo-ngay/": {
            "title": "Nên Thuê Tài Xế Theo Giờ Hay Theo Ngày? Hướng Dẫn Chọn Gói Tiết Kiệm",
            "h1": "Thuê Tài Xế Theo Giờ Hay Theo Ngày: Chọn Thế Nào Để Tiết Kiệm?",
            "meta_desc": "Phân tích cụ thể chi phí và sự phù hợp giữa hình thức thuê tài xế theo giờ và theo ngày cho nhu cầu công tác, gặp đối tác, du lịch.",
            "priority": "Medium"
        },
        "/blog/thue-xe-tu-lai-goi-tai-xe/": {
            "title": "Thuê Xe Tự Lái Có Thể Gọi Tài Xế Lái Thay Được Không? | Như Ý Driver",
            "h1": "Thuê Xe Tự Lái Có Thể Gọi Tài Xế Lái Thay Được Không?",
            "meta_desc": "Giải đáp thắc mắc pháp lý và bảo hiểm khi khách thuê xe tự lái nhưng muốn gọi tài xế lái hộ đưa về nhà hoặc lái tiếp hành trình.",
            "priority": "Medium"
        },
        "/blog/thue-tai-xe-da-nang-di-hoi-an/": {
            "title": "Thuê Tài Xế Đà Nẵng Đi Hội An: Lịch Trình & Những Điều Cần Lưu Ý",
            "h1": "Thuê Tài Xế Đà Nẵng Đi Hội An – Lịch Trình Chi Tiết & Lưu Ý",
            "meta_desc": "Kinh nghiệm thuê tài xế đưa cả gia đình đi phố cổ Hội An thưởng thức ẩm thực, dạo chơi buổi tối và đưa về Đà Nẵng an toàn.",
            "priority": "Medium"
        },
        "/blog/thue-tai-xe-da-nang-di-hue/": {
            "title": "Thuê Tài Xế Đà Nẵng Đi Huế: Khi Nào Nên Liên Hệ Đặt Trước?",
            "h1": "Thuê Tài Xế Đà Nẵng Đi Huế – An Toàn Cung Đường Đèo & Cao Tốc",
            "meta_desc": "Cẩm nang thuê tài xế đường dài Đà Nẵng - Huế: thời gian khởi hành, cung đường qua đèo hay hầm Hải Vân, chi phí và lưu ý đặt trước.",
            "priority": "Medium"
        }
    }
    return seo_meta.get(target_url, {
        "title": "Dịch Vụ Lái Xe Hộ Đà Nẵng 24/7 | Như Ý Driver",
        "h1": "Dịch Vụ Lái Xe Hộ Tại Đà Nẵng",
        "meta_desc": "Như Ý Driver cung cấp dịch vụ lái xe hộ ô tô và xe máy tại Đà Nẵng uy tín, an toàn 24/7. Gọi 0985 666 044.",
        "priority": "Medium"
    })

def main():
    csv_files = glob.glob('research/keywords/tu-khoa-2026-10-30*.csv')
    print(f"Loading {len(csv_files)} CSV files...")

    keywords_data = {}
    for fp in csv_files:
        fn = os.path.basename(fp)
        with open(fp, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row: continue
                kw = normalize_text(row[0])
                if not kw: continue
                src = normalize_text(row[1]) if len(row) > 1 else ""
                intent = normalize_text(row[2]) if len(row) > 2 else ""
                cluster = normalize_text(row[3]) if len(row) > 3 else ""
                score = normalize_text(row[4]) if len(row) > 4 else ""
                
                kw_lower = kw.lower()
                if kw_lower not in keywords_data:
                    keywords_data[kw_lower] = {
                        'kw': kw,
                        'sources': set([src] if src else []),
                        'intents': set([intent] if intent else []),
                        'clusters': set([cluster] if cluster else []),
                        'scores': [score] if score else [],
                        'files': set([fn])
                    }
                else:
                    if src: keywords_data[kw_lower]['sources'].add(src)
                    if intent: keywords_data[kw_lower]['intents'].add(intent)
                    if cluster: keywords_data[kw_lower]['clusters'].add(cluster)
                    if score: keywords_data[kw_lower]['scores'].append(score)
                    keywords_data[kw_lower]['files'].add(fn)

    print(f"Total unique keywords: {len(keywords_data)}")

    # Full Research CSV
    full_research_path = 'research/keyword-research-full.csv'
    with open(full_research_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Từ khóa', 'Phân loại ý định', 'Cụm chủ đề chuẩn hóa', 'Target URL', 
            'Độ ưu tiên', 'Nguồn dữ liệu', 'Cụm chủ đề gốc', 'Điểm cơ hội (gốc)', 
            'Trạng thái lọc', 'Ghi chú phân tích'
        ])
        
        for kw_l, data in sorted(keywords_data.items(), key=lambda x: x[0]):
            kw = data['kw']
            orig_intent = ", ".join(data['intents'])
            final_intent = classify_intent(kw, orig_intent)
            cluster_name, target_url, page_type, cluster_note = assign_cluster_and_url(kw)
            
            is_excluded = cluster_name == "Excluded"
            status = "Loại bỏ (Non-target)" if is_excluded else "Mục tiêu (Target)"
            meta = get_page_seo_meta(target_url) if not is_excluded else {}
            priority = "None" if is_excluded else meta.get('priority', 'Medium')
            
            writer.writerow([
                kw,
                final_intent,
                cluster_name,
                target_url if not is_excluded else "-",
                priority,
                ", ".join(sorted(data['sources'])),
                ", ".join(sorted(data['clusters'])),
                ", ".join(sorted(data['scores'])),
                status,
                cluster_note
            ])
    print(f"Generated {full_research_path}")

    # Build Keyword Map CSV
    kw_map_path = 'research/keyword-map.csv'
    # Group keywords by target_url
    url_groups = {}
    for kw_l, data in keywords_data.items():
        kw = data['kw']
        cluster_name, target_url, page_type, cluster_note = assign_cluster_and_url(kw)
        if cluster_name == "Excluded":
            continue
        if target_url not in url_groups:
            url_groups[target_url] = []
        url_groups[target_url].append((kw, data, cluster_name, page_type))

    with open(kw_map_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Keyword', 'Keyword Cluster', 'Search Intent', 'Priority', 'Target URL',
            'Page Type', 'SEO Title', 'H1', 'Meta Description', 'Supporting Keywords',
            'Internal Links', 'Source', 'Notes'
        ])
        
        # Write rows for each target page
        for target_url, kws in sorted(url_groups.items(), key=lambda x: x[0]):
            meta = get_page_seo_meta(target_url)
            # Pick primary keyword
            # Primary keyword heuristic: shortest with da nang, or top match
            sorted_kws = sorted(kws, key=lambda x: (not ('đà nẵng' in x[0].lower()), len(x[0])))
            primary_kw = sorted_kws[0][0]
            cluster_name = sorted_kws[0][2]
            page_type = sorted_kws[0][3]
            
            supporting = [x[0] for x in sorted_kws[1:15]] # top 14 supporting
            all_sources = set()
            for x in sorted_kws:
                all_sources.update(x[1]['sources'])
            
            # Suggest internal links based on page type
            internal_links = ["/", "/bang-gia/", "/lien-he/"]
            if target_url.startswith("/dich-vu/"):
                internal_links.extend(["/dich-vu/", "/khu-vuc/", "/blog/"])
            elif target_url.startswith("/khu-vuc/"):
                internal_links.extend(["/dich-vu/lai-xe-ho-o-to/", "/dich-vu/lai-xe-ho-xe-may/"])
            elif target_url.startswith("/blog/"):
                internal_links.extend(["/dich-vu/ban-uong-toi-lai/", "/blog/"])

            orig_intent = ", ".join(sorted_kws[0][1]['intents'])
            search_intent = classify_intent(primary_kw, orig_intent)

            writer.writerow([
                primary_kw,
                cluster_name,
                search_intent,
                meta.get('priority', 'Medium'),
                target_url,
                page_type,
                meta.get('title', ''),
                meta.get('h1', ''),
                meta.get('meta_desc', ''),
                " | ".join(supporting),
                ", ".join(internal_links),
                ", ".join(sorted(all_sources)),
                f"Đại diện cụm {len(sorted_kws)} từ khóa liên quan"
            ])

            # Also write out other distinct keywords for this page as individual mappings
            for other_kw, odata, ocluster, otype in sorted_kws[1:]:
                o_intent = classify_intent(other_kw, ", ".join(odata['intents']))
                writer.writerow([
                    other_kw,
                    ocluster,
                    o_intent,
                    "Supporting",
                    target_url,
                    page_type,
                    meta.get('title', ''),
                    meta.get('h1', ''),
                    meta.get('meta_desc', ''),
                    primary_kw,
                    ", ".join(internal_links),
                    ", ".join(sorted(odata['sources'])),
                    f"Từ khóa bổ trợ cho trang {target_url}"
                ])

    print(f"Generated {kw_map_path}")

if __name__ == '__main__':
    main()

