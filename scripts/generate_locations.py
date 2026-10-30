import os
import sys
from site_components import (
    BASE_URL, BRAND_NAME, HOTLINE, HOTLINE_TEL, ZALO_URL, picture_tag, render_breadcrumbs, render_related_topics
)
from site_builder_core import render_page_shell, write_html

sys.stdout.reconfigure(encoding='utf-8')

LOCATIONS_DATA = [
    {
        "slug": "hai-chau",
        "title": "Lái Xe Hộ Hải Châu Đà Nẵng 24/7 | Tài Xế Đến Sau 10-15 Phút",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN HẢI CHÂU ĐÀ NẴNG – PHỤC VỤ 24/7",
        "meta_desc": "Lái xe hộ ô tô & xe máy tại quận Hải Châu (Bạch Đằng, Nguyễn Văn Linh, 2/9, Trần Phú...). Đội ngũ tài xế túc trực trung tâm, có mặt sau 10-15 phút. Gọi 0985 666 044.",
        "image": "30_Lai_Xe_Ho_Hai_Chau_Da_Nang.png",
        "og_image": "/assets/images/30_Lai_Xe_Ho_Hai_Chau_Da_Nang.webp",
        "lead": "Quận Hải Châu là trái tim sôi động của thành phố Đà Nẵng với hàng loạt tuyến phố ẩm thực, quán bar, pub, trung tâm hội nghị tiệc cưới lớn. Tài xế Như Ý Driver túc trực xuyên đêm tại các nút giao trung tâm, có mặt đón bạn dự kiến chỉ từ 10–15 phút.",
        "key_routes": [
            "Tuyến phố ven sông Hàn: Đường Bạch Đằng, Như Nguyệt, Như Nguyệt kéo dài, khu vực cầu Rồng & cầu Trần Thị Lý.",
            "Trục tài chính, thương mại & ẩm thực: Nguyễn Văn Linh, Trần Phú, Phan Châu Trinh, Lê Duẩn, Hùng Vương.",
            "Tuyến phố tiệc tùng, sự kiện & nightlife: Đường 2 Tháng 9, Quảng trường 29/3, khu phức hợp Helio Center, chợ đêm.",
            "Phố chuyên doanh ẩm thực: Huỳnh Thúc Kháng, Phạm Hồng Thái, Hoàng Diệu, Trưng Nữ Vương."
        ],
        "content": """
        <h2>Dịch vụ lái xe hộ nhanh chóng, chuyên nghiệp nhất tại Quận Hải Châu</h2>
        <p>Hải Châu là khu vực tập trung mật độ nhà hàng, quán bar, phòng trà và tụ điểm tiếp khách lớn nhất Đà Nẵng. Vào mỗi buổi tối hay các dịp cuối tuần, lễ Tết, các tuyến phố như Bạch Đằng, Nguyễn Văn Linh, đường 2/9 luôn đông đúc các buổi tiệc tùng, gặp gỡ đối tác.</p>
        <p>Với quy định kiểm soát nồng độ cồn nghiêm ngặt và mức phạt hành chính rất cao kèm tước giấy phép lái xe, việc tự điều khiển xe sau khi đã uống bia rượu là hành vi cực kỳ rủi ro. <strong>Dịch vụ lái xe hộ Như Ý Driver</strong> là giải pháp an toàn tuyệt đối: tài xế lái chính ô tô hoặc xe máy của bạn đưa cả người và xe về tận nhà an toàn.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Lưu ý về quy hoạch hành chính (Cập nhật sau ngày 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Theo đề án sắp xếp đơn vị hành chính của thành phố Đà Nẵng, một số ranh giới phường tại quận Hải Châu được tổ chức, tinh gọn lại. Đội ngũ tài xế Như Ý Driver luôn cập nhật mạng lưới giao thông đô thị mới nhất, phục vụ xuyên suốt toàn bộ các phường truyền thống và đơn vị sáp nhập mới (Hải Châu 1, Hải Châu 2, Thạch Thang, Thanh Bình, Thuận Phước, Hòa Cường Bắc, Hòa Cường Nam, Bình Hiên, Bình Thuận, Hòa Thuận Đông, Hòa Thuận Tây, Nam Dương).
          </p>
        </div>

        <h2>Bảng giá lái xe hộ tại Hải Châu – Minh bạch không phí ẩn</h2>
        <p>Như Ý Driver áp dụng mức giá niêm yết rõ ràng, không phụ thu bất hợp lý:</p>
        <ul>
          <li><strong>Lái ô tô hộ:</strong> Khung 0 – 5 km giá chỉ <strong>150.000đ</strong>; khung 5 – 10 km là <strong>200.000đ</strong>; từ km 11 áp dụng 15.000đ/km.</li>
          <li><strong>Lái xe máy hộ:</strong> Khung 0 – 5 km giá chỉ <strong>110.000đ</strong>; 5 – 7 km là 130.000đ; 7 – 10 km là 170.000đ.</li>
          <li><strong>Phụ phí đêm:</strong> Sau 23h đêm phụ thu 50.000đ/chuyến nhằm hỗ trợ tài xế trực đêm tận tâm.</li>
        </ul>

        <h2>Quy trình đặt tài xế đón tại Hải Châu</h2>
        <ol>
          <li><strong>Bước 1:</strong> Gọi Hotline <a href="tel:0985666044" aria-label="Gọi Như Ý Driver 0985 666 044"><strong>0985 666 044</strong></a> hoặc gửi định vị vị trí quán nhậu/nhà hàng qua <a href="https://zalo.me/0985666044" target="_blank" rel="noopener nofollow">Zalo 0985 666 044</a>.</li>
          <li><strong>Bước 2:</strong> Tổng đài xác nhận vị trí, loại xe (ô tô/xe máy, số sàn/số tự động) và thông báo mức cước chính xác.</li>
          <li><strong>Bước 3:</strong> Tài xế mặc đồng phục áo đỏ, mang bảng tên Như Ý Driver đến điểm hẹn sau 10–15 phút.</li>
          <li><strong>Bước 4:</strong> Hai bên kiểm tra ngoại quan xe, tài xế nhận chìa khóa và đưa bạn cùng phương tiện về gara nhà an toàn.</li>
        </ol>
        """
    },
    {
        "slug": "thanh-khe",
        "title": "Lái Xe Hộ Thanh Khê Đà Nẵng 24/7 | Tài Xế Đến Sau 15 Phút",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN THANH KHÊ ĐÀ NẴNG – TÀI XẾ 24/7",
        "meta_desc": "Dịch vụ lái xe hộ ô tô và xe máy tại quận Thanh Khê (Điện Biên Phủ, Hà Huy Tập, bờ biển Nguyễn Tất Thành, Lê Độ...). Có mặt sau 15 phút. Báo giá trọn gói từ 150K. Gọi 0985 666 044.",
        "image": "12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.png",
        "og_image": "/assets/images/12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.webp",
        "lead": "Quận Thanh Khê có mật độ dân cư đông đúc, các tụ điểm quán nhậu dọc bờ biển Nguyễn Tất Thành lộng gió cùng các phố kinh doanh sầm uất Điện Biên Phủ, Hà Huy Tập. Tài xế Như Ý Driver sẵn sàng đón bạn sau 10–15 phút.",
        "key_routes": [
            "Tuyến ẩm thực ven vịnh: Đường biển Nguyễn Tất Thành (đoạn Thanh Khê Đông, Thanh Khê Tây).",
            "Trục giao thông thương mại trung tâm: Tuyến Điện Biên Phủ, Hà Huy Tập, Huỳnh Ngọc Huệ.",
            "Tuyến phố kinh doanh nhộn nhịp: Lê Độ, Trần Cao Vân, Nguyễn Tri Phương, Dũng Sĩ Thanh Khê.",
            "Khu vực giáp ranh kết nối: Ngã ba Huế, khu hồ Thạc Gián – Vĩnh Trung, chợ Cồn, công viên 29/3."
        ],
        "content": """
        <h2>Gọi tài xế lái xe hộ an toàn tại Thanh Khê sau tiệc rượu</h2>
        <p>Thanh Khê là một trong những quận trung tâm nội thành Đà Nẵng có chiều dài bờ vịnh biển Nguyễn Tất Thành tuyệt đẹp. Tại đây tập trung hàng trăm quán nhậu bình dân lẫn nhà hàng hải sản tươi sống hoạt động nhộn nhịp từ chiều đến tận nửa đêm.</p>
        <p>Sau những giờ phút nâng ly sảng khoái cùng bạn bè và đồng nghiệp, việc cầm lái trên các tuyến đường đông đúc như Điện Biên Phủ hay đoạn ngã ba Huế trong trạng thái đã có hơi men tiềm ẩn nguy cơ va quẹt giao thông rất cao. Đừng để niềm vui gặp gỡ biến thành sự cố đáng tiếc – hãy để tài xế Như Ý Driver cầm lái chính xe của bạn.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Phạm vi phục vụ tại địa bàn Thanh Khê (Quy hoạch sau 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Chúng tôi phục vụ tất cả các khu dân cư trên địa bàn truyền thống quận Thanh Khê và các phường thuộc đề án sắp xếp đơn vị hành chính đô thị: An Khê, Thanh Khê Đông, Thanh Khê Tây, Vĩnh Trung, Tân Chính, Chính Gián, Tam Thuận, Xuân Hà, Hòa Khê. Tài xế nắm rõ các ngõ hẻm, đường một chiều và các nút giao giờ cao điểm để đưa bạn về nhà nhanh chóng và êm dịu nhất.
          </p>
        </div>

        <h2>Cam kết chất lượng dịch vụ của Như Ý Driver tại Thanh Khê</h2>
        <ul>
          <li><strong>Tài xế chuyên nghiệp:</strong> Đủ bằng lái hạng B2, C, D, có ít nhất 5 năm kinh nghiệm điều khiển các dòng xe số sàn, số tự động từ xe phổ thông đến xe sang gầm cao.</li>
          <li><strong>Minh bạch chi phí:</strong> Giá ô tô chỉ từ 150K (0–5km), xe máy chỉ từ 110K (0–5km). Báo giá trước, cam kết không phát sinh bất kỳ khoản phí nào ngoài thỏa thuận.</li>
          <li><strong>Đón khách đúng hẹn:</strong> Tài xế túc trực thường trực tại khu vực công viên 29/3, đường Hà Huy Tập và tuyến bờ biển Nguyễn Tất Thành, dự kiến có mặt chỉ 10–15 phút sau cuộc gọi.</li>
        </ul>
        """
    },
    {
        "slug": "son-tra",
        "title": "Lái Xe Hộ Sơn Trà Đà Nẵng 24/7 | Tuyến Biển Võ Nguyên Giáp",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN SƠN TRÀ ĐÀ NẴNG – AN TOÀN & CHU ĐÁO",
        "meta_desc": "Dịch vụ lái xe hộ tại Sơn Trà, tuyến biển Võ Nguyên Giáp, Phạm Văn Đồng, Hồ Nghinh, quán hải sản ven biển. Tài xế lái chính xe của bạn về nhà an toàn. Gọi 0985 666 044.",
        "image": "31_Lai_Xe_Ho_Son_Tra_Da_Nang.png",
        "og_image": "/assets/images/31_Lai_Xe_Ho_Son_Tra_Da_Nang.webp",
        "lead": "Sơn Trà nổi tiếng với thiên đường ẩm thực hải sản biển Mỹ Khê và các resort nghỉ dưỡng đẳng cấp. Thưởng thức hải sản tươi ngon cùng bia mát lạnh, đường về đã có Như Ý Driver đưa bạn và xe về an toàn tuyệt đối.",
        "key_routes": [
            "Tuyến ven biển triệu đô: Tuyến Võ Nguyên Giáp, Hoàng Sa, bãi biển Mỹ Khê, bãi tắm Phạm Văn Đồng.",
            "Phố hải sản & ẩm thực đêm sầm uất: Phạm Văn Đồng, Hồ Nghinh, Dương Đình Nghệ, Hà Bổng, Võ Văn Kiệt.",
            "Bờ Đông sông Hàn & cầu cảnh quan: Tuyến Trần Hưng Đạo (khu vực cầu Rồng, cầu Sông Hàn, bến du thuyền DHC).",
            "Trục dân cư & thương mại: Ngô Quyền, Nguyễn Văn Thoại, Yết Kiêu, khu vực bán đảo Sơn Trà."
        ],
        "content": """
        <h2>Thưởng thức hải sản biển Sơn Trà thả ga – Không lo nồng độ cồn</h2>
        <p>Những bữa tiệc hải sản tươi sống cùng đối tác, bạn bè bên bãi biển Sơn Trà luôn rôm rả tiếng cười và những ly bia mát lạnh. Tuy nhiên, sau tiệc rượu, việc tự điều khiển xe ô tô hay xe máy vượt qua các cây cầu lớn như Cầu Rồng, Cầu Sông Hàn hay Cầu Thuận Phước trong trạng thái chuếnh choáng là vô cùng nguy hiểm.</p>
        <p>Lực lượng cảnh sát giao thông thường xuyên lập chốt kiểm tra nồng độ cồn tại các nút giao hai đầu cầu và trục đường ven biển. Hãy bảo vệ giấy phép lái xe, phương tiện và sự bình an của bản thân bằng cách gọi ngay Như Ý Driver.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Địa bàn hoạt động Sơn Trà & Ghi chú địa giới hành chính</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Chúng tôi phục vụ đón khách tại toàn bộ các phường thuộc bán đảo và đô thị Sơn Trà: An Hải Bắc, An Hải Tây, An Hải Đông, Phước Mỹ, Mân Thái, Thọ Quang, Nại Hiên Đông. <em>Lưu ý: Huyện đảo Hoàng Sa là đặc khu hải đảo tiền tiêu thuộc chủ quyền quốc gia, không thuộc phạm vi cung cấp dịch vụ đưa đón đường bộ nội đô thông thường.</em>
          </p>
        </div>

        <h2>Lý do du khách và người dân Sơn Trà tin chọn Như Ý Driver</h2>
        <ul>
          <li><strong>Đón tận nơi tại bãi biển & nhà hàng:</strong> Dù bạn đang ở quán hải sản ven biển đường Võ Nguyên Giáp, nhà hàng ven sông Trần Hưng Đạo hay quán pub đường Võ Văn Kiệt, tài xế chỉ mất 10–15 phút để có mặt.</li>
          <li><strong>Lái xe cẩn thận, êm dịu:</strong> Luôn tuân thủ quy tắc số sàn / số tự động, giữ khoảng cách phanh an toàn, đảm bảo bạn có thể ngủ ngon lành trên ghế phụ suốt chặng đường về.</li>
          <li><strong>Giá cước cố định công khai:</strong> 150K cho 5km đầu ô tô, 110K cho xe máy. Có hóa đơn dịch vụ rõ ràng khi khách hàng công tác yêu cầu.</li>
        </ul>
        """
    },
    {
        "slug": "ngu-hanh-son",
        "title": "Lái Xe Hộ Ngũ Hành Sơn Đà Nẵng | Phố Tây An Thượng, Resort Ven Biển",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN NGŨ HÀNH SƠN ĐÀ NẴNG – 24/7",
        "meta_desc": "Dịch vụ tài xế lái xe hộ tại Ngũ Hành Sơn: Phố Tây An Thượng, đường Võ Nguyên Giáp - Trường Sa, Non Nước, resort ven biển. Có mặt sau 15 phút. Hotline: 0985 666 044.",
        "image": "15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png",
        "og_image": "/assets/images/15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.webp",
        "lead": "Ngũ Hành Sơn là trung tâm du lịch nghỉ dưỡng cao cấp với phố Tây An Thượng, các resort 5 sao ven biển và danh thắng Non Nước. Đội ngũ tài xế Như Ý Driver túc trực 24/7 sẵn sàng đưa bạn và xế cưng về nhà an toàn.",
        "key_routes": [
            "Trục du lịch biển tỷ đô: Tuyến đường Võ Nguyên Giáp – Trường Sa nối liền Đà Nẵng và Hội An.",
            "Khu phố Tây nightlife sầm uất: Phố đi bộ An Thượng (An Thượng 1 đến An Thượng 30), đường Hoàng Kế Viêm, Ngô Thì Sĩ.",
            "Trục giao thông nội đô huyết mạch: Tuyến Lê Văn Hiến, Nam Kỳ Khởi Nghĩa, Trần Đại Nghĩa, Minh Mạng.",
            "Khu vực resort đẳng cấp: Furama Resort, Hyatt Regency, Vinpearl Luxury, bãi tắm Non Nước, cầu Tiên Sơn."
        ],
        "content": """
        <h2>Tận hưởng trọn vẹn không gian nightlife phố Tây An Thượng & tiệc resort</h2>
        <p>Quận Ngũ Hành Sơn là điểm giao thoa giữa nét văn hóa quốc tế nhộn nhịp tại khu phố Tây An Thượng và không gian nghỉ dưỡng cao cấp dọc tuyến biển Trường Sa. Các quán pub, bar ngoài trời, nhà hàng nướng BBQ và beach club thu hút lượng lớn du khách cũng như người dân địa phương tham gia giao lưu, tiệc tùng thâu đêm.</p>
        <p>Tuy nhiên, sau khi đã sử dụng đồ uống có cồn, cung đường dài từ Ngũ Hành Sơn về lại các quận trung tâm như Hải Châu, Cẩm Lệ hay Thanh Khê qua cầu Tiên Sơn, cầu Trần Thị Lý tiềm ẩn nhiều rủi ro. <strong>Như Ý Driver</strong> cung cấp tài xế lái chính xe của bạn, đảm bảo cả người lẫn xe về tận nhà nguyên vẹn, êm ái.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Địa bàn phục vụ thực tế tại Ngũ Hành Sơn (Cập nhật sau 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Dịch vụ lái xe hộ của chúng tôi bao phủ toàn bộ các khu vực dân cư và dự án đô thị tại Ngũ Hành Sơn: Phường Mỹ An, Khuê Mỹ, Hòa Hải, Hòa Quý, khu đô thị FPT City Đà Nẵng, khu đô thị làng đại học. Tài xế thông thuộc đường nội bộ resort lẫn ngõ phố An Thượng, đón khách chu đáo và lịch sự.
          </p>
        </div>

        <h2>Bảng giá dịch vụ lái hộ tại Ngũ Hành Sơn</h2>
        <p>Mức giá áp dụng đồng nhất toàn hệ thống, kiểm tra minh bạch trước chuyến đi:</p>
        <ul>
          <li><strong>Ô tô:</strong> 150.000đ (0–5km), 200.000đ (5–10km), từ km thứ 11 áp dụng 15.000đ/km.</li>
          <li><strong>Xe máy:</strong> 110.000đ (0–5km), 130.000đ (5–7km), 170.000đ (7–10km).</li>
          <li><strong>Tuyến liên tỉnh Ngũ Hành Sơn &rarr; Hội An:</strong> Báo giá trọn gói ưu đãi chỉ từ 300.000đ – 450.000đ tùy điểm đón/trả và thời gian chờ.</li>
        </ul>
        """
    },
    {
        "slug": "lien-chieu",
        "title": "Lái Xe Hộ Liên Chiểu Đà Nẵng 24/7 | KCN Hòa Khánh, Nguyễn Tất Thành",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN LIÊN CHIỂU ĐÀ NẴNG – PHỤC VỤ 24/7",
        "meta_desc": "Dịch vụ lái xe hộ ô tô & xe máy tại Liên Chiểu, KCN Hòa Khánh, đường biển Nguyễn Tất Thành, Tôn Đức Thắng, Hoàng Thị Loan. Tài xế đến sau 15 phút. Gọi 0985 666 044.",
        "image": "04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png",
        "og_image": "/assets/images/04_Dich_Vu_Lai_Ho_O_To_Da_Nang.webp",
        "lead": "Liên Chiểu là cửa ngõ phía Bắc thành phố với các khu công nghiệp sầm uất, các trường đại học lớn và chuỗi nhà hàng ẩm thực bờ biển vịnh Đà Nẵng. Tài xế Như Ý Driver túc trực hỗ trợ bạn và xe về nhà an toàn mọi khung giờ.",
        "key_routes": [
            "Trục đường biển vịnh Đà Nẵng: Tuyến Nguyễn Tất Thành (đoạn Liên Chiểu nối chân đèo Hải Vân).",
            "Tuyến giao thông cửa ngõ Bắc: Tôn Đức Thắng, Nguyễn Lương Bằng (QL1A), đường tránh Nam Hải Vân.",
            "Trục đô thị mới: Tuyến Hoàng Thị Loan, Nguyễn Sinh Sắc, khu đô thị Tây Bắc, trục đường số 4.",
            "Khu vực tập trung tiệc tùng: KCN Hòa Khánh, chợ Hòa Khánh, khu ăn uống bờ biển Xuân Thiều, Nam Ô."
        ],
        "content": """
        <h2>Giải pháp an toàn sau mỗi buổi tiệc tại khu vực Liên Chiểu</h2>
        <p>Liên Chiểu có đặc thù là địa bàn tập trung nhiều nhà máy xí nghiệp tại KCN Hòa Khánh, các công ty xây dựng và trường đại học lớn. Nhu cầu giao lưu, liên hoan tổng kết, tiếp khách sau giờ làm việc diễn ra rất thường xuyên tại các nhà hàng bia, quán lẩu nướng, quán dê, bê thui và hải sản bờ biển Nguyễn Tất Thành.</p>
        <p>Đặc biệt, lưu lượng xe tải, xe container trên các tuyến Tôn Đức Thắng, Nguyễn Lương Bằng rất lớn. Việc lái xe về sau khi đã uống bia rượu trong điều kiện giao thông phức tạp này là vô cùng nguy hiểm. Đặt <strong>tài xế Như Ý Driver</strong> là quyết định sáng suốt nhất để bảo vệ an toàn tính mạng cho chính bạn và người tham gia giao thông.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Địa bàn phục vụ tại Liên Chiểu (Tổ chức hành chính sau 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Chúng tôi phục vụ nhanh chóng tại tất cả các phường truyền thống và khu dân cư mới của Liên Chiểu: Hòa Minh, Hòa Khánh Nam, Hòa Khánh Bắc, Hòa Hiệp Nam, Hòa Hiệp Bắc (khu vực Làng Vân, chân đèo Hải Vân, cảng Liên Chiểu). Tài xế luôn có mặt dự kiến sau 15–20 phút kể từ khi nhận cuộc gọi.
          </p>
        </div>

        <h2>Ưu điểm vượt trội của dịch vụ lái hộ Như Ý Driver tại Liên Chiểu</h2>
        <ul>
          <li><strong>Có mặt đúng cam kết:</strong> Tài xế phân bổ tại các nút giao Nguyễn Sinh Sắc – Hoàng Thị Loan và ngã tư KCN Hòa Khánh, di chuyển tiếp cận nhanh chóng.</li>
          <li><strong>Lái xe thuần thục:</strong> Đội ngũ tài xế giàu kinh nghiệm, lái êm ái trên cả xe số sàn và số tự động, xe bán tải, SUV gia đình.</li>
          <li><strong>Giá cả bình dân:</strong> Ô tô chỉ từ 150.000đ, xe máy chỉ từ 110.000đ. Phục vụ 24/7 kể cả ngày nghỉ cuối tuần và ngày lễ lớn.</li>
        </ul>
        """
    },
    {
        "slug": "cam-le",
        "title": "Lái Xe Hộ Cẩm Lệ Đà Nẵng | Hòa Xuân, CMT8, Nguyễn Hữu Thọ",
        "h1": "DỊCH VỤ LÁI XE HỘ QUẬN CẨM LỆ ĐÀ NẴNG – 24/7 AN TOÀN",
        "meta_desc": "Dịch vụ lái xe hộ tại Cẩm Lệ: KĐT Hòa Xuân, đường CMT8, Nguyễn Hữu Thọ, Lê Đại Hành, đường ven sông Thăng Long. Đón sau 15 phút. Giá từ 150K. Hotline: 0985 666 044.",
        "image": "02_Lai_Xe_Ho_Da_Nang_247.png",
        "og_image": "/assets/images/02_Lai_Xe_Ho_Da_Nang_247.webp",
        "lead": "Cẩm Lệ nổi tiếng với khu đô thị sinh thái Hòa Xuân ven sông lộng gió, các phố ẩm thực đồng quê ven sông Thăng Long và các trục kết nối CMT8, Nguyễn Hữu Thọ. Tài xế Như Ý Driver hỗ trợ bạn về nhà an toàn.",
        "key_routes": [
            "Trục ven sông sinh thái: Đường Thăng Long ven sông Cẩm Lệ, cầu Cẩm Lệ, cầu Đỏ, cầu Hòa Xuân.",
            "Khu đô thị sinh thái Hòa Xuân: Tuyến Nguyễn Phước Lan, 29 Tháng 3, Văn Tiến Dũng, Võ Chí Công.",
            "Trục thương mại & giao thông trung tâm: Đường Cách Mạng Tháng Tám (CMT8), Nguyễn Hữu Thọ, Lê Đại Hành.",
            "Khu vực sân vận động & trung tâm tiệc cưới: Khu vực Sân vận động Hòa Xuân, bến xe trung tâm (khu vực Hòa An)."
        ],
        "content": """
        <h2>Tài xế lái hộ tận tâm tại Cẩm Lệ – Về nhà bình an sau mọi bữa tiệc</h2>
        <p>Quận Cẩm Lệ và đặc biệt là bán đảo sinh thái Hòa Xuân sở hữu hệ sinh thái nhà hàng ven sông tuyệt vời. Những quán nhậu dọc đường Thăng Long, đường ven sông Đô Tỏa hay các nhà hàng sân vườn Hòa Xuân là địa điểm tụ họp quen thuộc của gia đình, bạn bè sau giờ tan sở.</p>
        <p>Sau những cuộc vui có bia rượu, cảm giác mệt mỏi cộng với việc phải di chuyển qua các cây cầu như Cầu Hòa Xuân, Cầu Nguyễn Tri Phương, Cầu Cẩm Lệ với mật độ phương tiện cao là điều rất nguy hiểm. Hãy để các bác tài Như Ý Driver chịu trách nhiệm đưa phương tiện và bạn về tận gara an toàn.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Địa bàn phục vụ tại Cẩm Lệ (Theo đề án tổ chức sau 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Như Ý Driver phục vụ toàn bộ các phường truyền thống và khu dân cư của Cẩm Lệ: Khuê Trung, Hòa Thọ Đông, Hòa Thọ Tây, Hòa An, Hòa Phát, và toàn bộ khu đô thị Hòa Xuân (Đảo 1, Đảo 2, khu ven sông). Chỉ cần gửi vị trí Zalo, tài xế gần nhất sẽ có mặt dự kiến sau 10–15 phút.
          </p>
        </div>

        <h2>Cam kết chất lượng dịch vụ Như Ý Driver tại Cẩm Lệ</h2>
        <ul>
          <li><strong>Bảo vệ xe cẩn thận:</strong> Kiểm tra xe kỹ càng, tắt máy, khóa cửa, bàn giao chìa khóa tận tay người nhà hoặc khách hàng sau khi xe vào gara an toàn.</li>
          <li><strong>Giá cước niêm yết:</strong> 150K cho 5km đầu tiên với ô tô, 110K cho xe máy. Không phát sinh chi phí bất hợp lý.</li>
          <li><strong>Phục vụ xuyên đêm:</strong> Dù tiệc tàn lúc 23h đêm hay 2h sáng, tài xế áo đỏ Như Ý Driver luôn sẵn sàng phục vụ.</li>
        </ul>
        """
    },
    {
        "slug": "hoa-vang",
        "title": "Lái Xe Hộ Hòa Vang Đà Nẵng | Bà Nà, QL14B, Du Lịch Sinh Thái",
        "h1": "DỊCH VỤ LÁI XE HỘ HUYỆN HÒA VANG ĐÀ NẴNG – PHỤC VỤ 24/7",
        "meta_desc": "Dịch vụ tài xế lái xe hộ tại Hòa Vang: Tuyến QL14B, QL1A, đường Bà Nà Suối Mơ, các khu du lịch sinh thái Yên Retreat, Lái Thiêu... Báo giá rõ ràng. Gọi 0985 666 044.",
        "image": "14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.png",
        "og_image": "/assets/images/14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.webp",
        "lead": "Hòa Vang là vùng sinh thái ngoại ô với các điểm dã ngoại nổi tiếng như Bà Nà Hills, Núi Thần Tài, Suối Hoa, Yên Retreat cùng các nhà hàng đặc sản đồng quê. Thuê tài xế lái xe riêng giúp cả đoàn thảnh thơi vui chơi.",
        "key_routes": [
            "Trục du lịch Bà Nà – Suối Mơ: Tuyến Hoàng Văn Thái nối dài đi Sun World Ba Na Hills.",
            "Trục Quốc lộ 14B & cao tốc liên tỉnh: Kết nối Tây Nguyên, Đại Lộc (Quảng Nam), cao tốc Túy Loan – La Sơn.",
            "Trục Quốc lộ 1A cửa ngõ phía Nam: Hòa Phước, Hòa Châu kết nối thị xã Điện Bàn.",
            "Các khu dã ngoại sinh thái: Xã Hòa Bắc, Hòa Ninh, Hòa Phú (KDL Suối Hoa, Núi Thần Tài, Lái Thiêu, Yên Retreat)."
        ],
        "content": """
        <h2>Thảnh thơi dã ngoại & tiệc tùng ngoại ô Hòa Vang – Đã có tài xế lái hộ</h2>
        <p>Hòa Vang là điểm đến nghỉ dưỡng cuối tuần lý tưởng của các gia đình và nhóm bạn bè tại Đà Nẵng. Những buổi dã ngoại cắm trại tại Hòa Bắc, tắm suối khoáng nóng tại Hòa Phú hay ăn tiệc liên hoan tại các nhà hàng đặc sản gà đồi, cá sông luôn mang lại những phút giây thư giãn tuyệt vời.</p>
        <p>Tuy nhiên, đường về từ Hòa Vang vào trung tâm thành phố có quãng đường khá dài (15 – 35 km), đi qua nhiều đoạn đèo dốc quanh co, đường thiếu đèn chiếu sáng và giao cắt nhiều xe tải trọng lớn. Sau một ngày dài vui chơi mệt mỏi và có sử dụng bia rượu, việc tự cầm lái xe chở gia đình là rất rủi ro. <strong>Hãy để tài xế Như Ý Driver lái chính chiếc xe của bạn</strong> đưa cả nhà về trung tâm an toàn.</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:18px; border-radius:8px; margin:24px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">Địa bàn phục vụ ngoại thành Hòa Vang (Cập nhật sau 01/07/2025)</h3>
          <p style="margin-bottom:0; font-size:0.95rem; color:#475569;">
            Chúng tôi nhận điều phối tài xế đến tận nơi tại tất cả các xã trên địa bàn huyện Hòa Vang: Hòa Phong (trung tâm hành chính huyện), Hòa Châu, Hòa Tiến, Hòa Phước, Hòa Khương, Hòa Nhơn, Hòa Ninh, Hòa Sơn, Hòa Liên, Hòa Bắc, Hòa Phú. Do đặc thù ngoại thành quãng đường xa, quý khách nên liên hệ trước từ 20–30 phút để tài xế kịp thời di chuyển đến điểm đón.
          </p>
        </div>

        <h2>Báo giá dịch vụ lái hộ tại Hòa Vang</h2>
        <ul>
          <li><strong>Chuyến ngắn ngoại thành:</strong> Áp dụng giá tiêu chuẩn 150K (0–5km), 200K (5–10km) và 15.000đ/km tiếp theo.</li>
          <li><strong>Thuê tài xế lái đi dã ngoại theo ngày:</strong> Gói 8 tiếng chỉ từ 600.000đ – 800.000đ, tài xế phục vụ đưa đón suốt ngày dài, túc trực chờ xe trong khi quý khách vui chơi, ăn uống.</li>
        </ul>
        """
    },
    {
        "slug": "da-nang-di-hoi-an",
        "title": "Thuê Tài Xế Đà Nẵng Đi Hội An Trọn Gói | An Toàn, Đúng Giờ",
        "h1": "THUÊ TÀI XẾ LÁI XE ĐÀ NẴNG ĐI HỘI AN – LỊCH TRÌNH THEO YÊU CẦU",
        "meta_desc": "Dịch vụ thuê tài xế lái ô tô riêng từ Đà Nẵng đi Hội An và ngược lại. Phù hợp du lịch, công tác, dự tiệc. Báo giá trọn gói minh bạch, tài xế chu đáo. Hotline: 0985 666 044.",
        "image": "28_Thue_Tai_Xe_Da_Nang_Di_Hoi_An.png",
        "og_image": "/assets/images/28_Thue_Tai_Xe_Da_Nang_Di_Hoi_An.webp",
        "lead": "Tuyến đường di sản khoảng 30km kết nối Đà Nẵng và Phố Cổ Hội An. Thuê tài xế lái chính xe của bạn để cả gia đình tận hưởng trọn vẹn chuyến dạo chơi phố cổ, thưởng thức ẩm thực và về lại Đà Nẵng thảnh thơi.",
        "key_routes": [
            "Tuyến ven biển: Đường Võ Nguyên Giáp &rarr; Trường Sa &rarr; Lạc Long Quân &rarr; An Bàng &rarr; Phố Cổ Hội An.",
            "Tuyến nội địa: Tuyến Lê Văn Hiến &rarr; Trần Đại Nghĩa &rarr; Đường DT607 &rarr; Trung tâm TP. Hội An.",
            "Lịch trình khứ hồi trong ngày: Đưa đi chiều - Chờ ăn tối cà phê ngắm đèn lồng - Đưa về Đà Nẵng trong đêm.",
            "Lịch trình công tác hoặc đưa đón khách VIP tham dự hội nghị tại Hội An."
        ],
        "content": """
        <h2>Du lịch Hội An trọn vẹn không lo mệt mỏi cầm lái</h2>
        <p>Sau một ngày dạo bộ chụp ảnh và thưởng thức ẩm thực phố cổ Hội An, cảm giác mệt mỏi và buồn ngủ rất dễ ập đến trên đường lái xe 30km về lại Đà Nẵng trong đêm muộn. Hơn nữa, đường ven biển ban đêm thường vắng xe nhưng có nhiều đoạn giao cắt và khúc cua tiềm ẩn rủi ro.</p>
        <p>Thuê tài xế Như Ý Driver lái xe riêng đi Hội An giúp bạn và gia đình hoàn toàn thư giãn, nghỉ ngơi trên xe sau chuyến đi chơi thú vị.</p>
        """
    },
    {
        "slug": "da-nang-di-hue",
        "title": "Thuê Tài Xế Đà Nẵng Đi Huế An Toàn Qua Đèo Hải Vân / Hầm Hải Vân",
        "h1": "THUÊ TÀI XẾ ĐÀ NẴNG ĐI HUẾ – TAY LÁI VỮNG ĐƯỜNG ĐÈO & CAO TỐC",
        "meta_desc": "Dịch vụ thuê tài xế lái xe riêng tuyến Đà Nẵng - Huế (qua hầm hoặc đèo Hải Vân). Tài xế giàu kinh nghiệm đường trường, lái cẩn thận, an toàn. Gọi 0985 666 044.",
        "image": "29_Thue_Tai_Xe_Da_Nang_Di_Hue.png",
        "og_image": "/assets/images/29_Thue_Tai_Xe_Da_Nang_Di_Hue.webp",
        "lead": "Hành trình khoảng 100km vượt thiên hạ đệ nhất hùng quan Đèo Hải Vân hoặc qua Hầm Hải Vân kết nối Cố đô Huế. Tài xế đường trường Như Ý Driver giàu kinh nghiệm, đảm bảo an toàn tuyệt đối.",
        "key_routes": [
            "Tuyến hầm đường bộ Hải Vân & Quốc lộ 1A: Nhanh chóng, êm ái, chỉ mất khoảng 2 giờ di chuyển.",
            "Tuyến ngắm cảnh Đèo Hải Vân: Dành cho du khách muốn chiêm ngưỡng vẻ đẹp vịnh Lăng Cô và đèo mây.",
            "Tuyến Cao tốc La Sơn – Túy Loan: Kết nối liên tỉnh hiện đại.",
            "Phục vụ khứ hồi trong ngày: Thăm lăng tẩm, dự đám cưới, làm việc với đối tác tại TP. Huế."
        ],
        "content": """
        <h2>Chinh phục cung đường Đà Nẵng – Huế an tâm tuyệt đối</h2>
        <p>Cung đường nối liền Đà Nẵng và Thừa Thiên Huế có nhiều đoạn dốc quanh co và thời tiết sương mù đặc thù ở khu vực đèo Hải Vân và Lăng Cô. Điều này đòi hỏi người lái xe phải có kỹ năng phanh số, kiểm soát tốc độ và kinh nghiệm đường trường dày dặn.</p>
        <p>Tài xế Như Ý Driver nhận cầm lái chính xe ô tô của bạn đi Huế với tinh thần trách nhiệm cao nhất, giúp bạn có chuyến đi êm thuận, an toàn và đúng hẹn.</p>
        """
    },
    {
        "slug": "da-nang-di-quang-ngai",
        "title": "Thuê Tài Xế Đà Nẵng Đi Quảng Ngãi | Lái Xe Đường Dài An Toàn",
        "h1": "THUÊ TÀI XẾ LÁI XE ĐÀ NẴNG ĐI QUẢNG NGÃI & CÁC TỈNH MIỀN TRUNG",
        "meta_desc": "Thuê tài xế lái ô tô đi Quảng Ngãi, Tam Kỳ, Chu Lai xuất phát từ Đà Nẵng. Phục vụ theo lịch trình 1 chiều hoặc khứ hồi trong ngày/nhiều ngày. Hotline: 0985 666 044.",
        "image": "08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.png",
        "og_image": "/assets/images/08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.webp",
        "lead": "Tuyến đường khoảng 140km theo cao tốc Đà Nẵng – Quảng Ngãi. Lái xe đường dài êm ái, đúng tốc độ làn đường cao tốc, phục vụ nhu cầu về quê, công tác KCN Dung Quất, Chu Lai.",
        "key_routes": [
            "Cao tốc Đà Nẵng – Quảng Ngãi: Di chuyển thần tốc chỉ khoảng 1.5 - 2 giờ đồng hồ.",
            "Quốc lộ 1A qua Điện Bàn, Thăng Bình, TP. Tam Kỳ, Núi Thành.",
            "Khu kinh tế Dung Quất, KCN VSIP Quảng Ngãi, Cảng Sa Kỳ (đi đảo Lý Sơn).",
            "Lịch trình công tác dài ngày theo yêu cầu của công ty hoặc đoàn thể."
        ],
        "content": """
        <h2>Lái xe đường dài đi Quảng Ngãi – Nghỉ ngơi trọn vẹn suốt hành trình</h2>
        <p>Quãng đường 140km từ Đà Nẵng vào Quảng Ngãi trên cao tốc yêu cầu tài xế phải giữ tốc độ chuẩn từ 100 - 120km/h và luôn giữ khoảng cách an toàn. Sau những ngày làm việc căng thẳng, việc tự cầm lái liên tục dễ gây mệt mỏi và mất tập trung.</p>
        <p>Thuê tài xế Như Ý Driver lái hộ là giải pháp tuyệt vời để bạn có thể tranh thủ chợp mắt, chuẩn bị tinh thần cho buổi làm việc hoặc thoải mái trò chuyện cùng người thân.</p>
        """
    }
]

def build_location_page(loc):
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/khu-vuc/", "title": "Khu Vực"},
        {"url": f"/khu-vuc/{loc['slug']}/", "title": loc["h1"].split("–")[0].strip()}
    ])

    routes_html = "".join([f'''
    <div class="split-check-item">
      <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
      <span>{r}</span>
    </div>
    ''' for r in loc["key_routes"]])

    core_services = [
        {
            "slug": "lai-xe-ho-o-to",
            "title": f"Lái Xe Hộ Ô Tô {loc['slug'].replace('-', ' ').title()}",
            "image": "04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png",
            "lead": "Tài xế lái chính ô tô đưa bạn và xe về nhà an toàn sau tiệc rượu, tiếp khách.",
            "price": "Từ 150.000đ"
        },
        {
            "slug": "lai-xe-ho-xe-may",
            "title": f"Lái Xe Hộ Xe Máy {loc['slug'].replace('-', ' ').title()}",
            "image": "05_Dich_Vu_Lai_Ho_Xe_May_Da_Nang.png",
            "lead": "Tài xế chạy chính xe máy của bạn đưa cả người và xe về gara an toàn.",
            "price": "Từ 110.000đ"
        },
        {
            "slug": "ban-uong-toi-lai",
            "title": "Bạn Uống Tôi Lái 24/7",
            "image": "03_Lai_Xe_Ho_Sau_Khi_Uong_Ruou_Bia.png",
            "lead": "Dịch vụ tài xế trực đêm phục vụ sau tiệc nhậu, quán bar, liên hoan.",
            "price": "Trực 24/7"
        }
    ]

    related_services_html = "".join([f'''
    <a href="/dich-vu/{srv['slug']}/" class="service-card" aria-label="{srv['title']}">
      <div class="service-card-img-wrap">
        {picture_tag(srv["image"], srv["title"], "service-card-img", 1536, 1024)}
        <span class="service-card-badge">{srv["price"]}</span>
      </div>
      <div class="service-card-content">
        <h3 class="service-card-title">{srv["title"]}</h3>
        <p class="service-card-desc">{srv["lead"]}</p>
        <div class="service-card-footer">
          <span class="service-price-tag">{srv["price"]}</span>
          <span class="service-more-link">Chi tiết &rarr;</span>
        </div>
      </div>
    </a>
    ''' for srv in core_services])

    nearby_locs = [(f"Khu vực {other['slug'].replace('-', ' ').title()}", f"/khu-vuc/{other['slug']}/") for other in LOCATIONS_DATA if other["slug"] != loc["slug"]]
    nearby_topics = render_related_topics(nearby_locs, "Địa bàn & Tuyến đường lân cận")

    local_topic_pills = [
        ("Bảng giá lái xe hộ ô tô 150K", "/bang-gia/"),
        ("Lái xe hộ xe máy từ 110K", "/dich-vu/lai-xe-ho-xe-may/"),
        ("Bạn uống tôi lái 24/7", "/dich-vu/ban-uong-toi-lai/"),
        ("Lái xe hộ sau tiệc rượu", "/dich-vu/lai-xe-ho-sau-tiec/"),
        ("Thuê tài xế đi Hội An", "/khu-vuc/da-nang-di-hoi-an/"),
        ("Thuê tài xế đi Huế", "/khu-vuc/da-nang-di-hue/"),
        ("Cẩm nang đặt tài xế ban đêm", "/blog/dat-tai-xe-lai-ho-ban-dem/"),
        ("Liên hệ tổng đài 0985 666 044", "/lien-he/")
    ]
    topics_html = render_related_topics(local_topic_pills, f"Chủ đề liên quan tại {loc['slug'].replace('-', ' ').title()}")

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">{loc["h1"]}</h1>
        <p class="page-hero-desc">{loc["lead"]}</p>
        <div style="display:inline-flex; gap:12px; margin-top:10px; flex-wrap:wrap;">
          <a href="{HOTLINE_TEL}" class="btn-primary" style="padding:10px 22px;" aria-label="Gọi Như Ý Driver {HOTLINE}">GỌI TÀI XẾ: {HOTLINE}</a>
          <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" style="padding:10px 22px;" aria-label="Đặt tài xế qua Zalo {HOTLINE}">GỬI ĐỊA CHỈ QUA ZALO</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge">Tuyến Đường Trọng Điểm</span>
            <h2 class="split-title">ĐỊA BÀN PHỤC VỤ TẠI {loc["slug"].replace("-", " ").upper()}</h2>
            <div class="split-checklist">
              {routes_html}
            </div>
            <div style="background:var(--gold-bg); padding:16px; border-radius:var(--radius-md); border-left:4px solid var(--gold); margin-top:16px;">
              <strong style="color:#78350f;">Thời gian có mặt dự kiến:</strong>
              <div style="color:var(--navy); font-size:1.1rem; font-weight:800; margin-top:4px;">Chỉ từ 10 – 20 phút nội thành Đà Nẵng!</div>
            </div>
          </div>
          <div class="split-media-wrap">
            {picture_tag(loc["image"], loc["title"], "split-media-img", 1536, 1024, lazy=False)}
          </div>
        </div>

        <div class="post-content" style="margin-top:50px; max-width:850px;">
          {loc["content"]}

          <!-- Pricing summary table -->
          <div style="margin:35px 0;">
            <h3 style="color:var(--navy); font-size:1.3rem; margin-bottom:12px;">Bảng giá tham khảo tại khu vực {loc['slug'].replace('-', ' ').title()}</h3>
            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; margin-bottom:15px; font-size:0.95rem;">
                <thead>
                  <tr style="background:var(--navy); color:#fff; text-align:left;">
                    <th style="padding:10px 14px; border:1px solid #cbd5e1;">Loại dịch vụ</th>
                    <th style="padding:10px 14px; border:1px solid #cbd5e1;">Cự ly 0 – 5 km</th>
                    <th style="padding:10px 14px; border:1px solid #cbd5e1;">Cự ly 5 – 10 km</th>
                    <th style="padding:10px 14px; border:1px solid #cbd5e1;">Km tiếp theo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Lái hộ ô tô (Số sàn / Tự động)</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; color:#b45309; font-weight:700;">150.000đ</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">200.000đ</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1;">+15.000đ/km</td>
                  </tr>
                  <tr style="background:#f8fafc;">
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Lái hộ xe máy (Xe số / Tay ga)</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; color:#b45309; font-weight:700;">110.000đ</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">170.000đ (7-10km)</td>
                    <td style="padding:10px 14px; border:1px solid #cbd5e1;">+10.000đ/km</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p style="font-size:0.875rem; color:#64748b;"><em>* Ghi chú: Sau 23h đêm phụ thu 50.000đ/chuyến. Tuyến đường dài liên tỉnh thỏa thuận trọn gói minh bạch trước khi xuất phát.</em></p>
          </div>

          <div class="post-cta-banner">
            <h3 style="color:#fff; font-size:1.6rem; font-weight:800; margin-bottom:12px;">ĐẶT TÀI XẾ TẠI {loc["slug"].replace("-", " ").upper()} NGAY BÂY GIỜ</h3>
            <p style="color:#cbd5e1; margin-bottom:20px;">Tài xế Như Ý Driver đồng phục đỏ túc trực 24/7 sẵn sàng phục vụ bạn mọi lúc mọi nơi.</p>
            <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
              <a href="{HOTLINE_TEL}" class="btn-primary" aria-label="Gọi ngay {HOTLINE}">GỌI NGAY: {HOTLINE}</a>
              <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" aria-label="Chat qua Zalo đặt xe">CHAT QUA ZALO</a>
              <a href="/bang-gia/" class="btn-outline-gold">XEM BẢNG GIÁ ĐÀ NẴNG</a>
            </div>
          </div>

          {topics_html}
          {nearby_topics}
        </div>

        <div class="related-section-wrap" style="max-width:850px; margin-left:auto; margin-right:auto;">
          <h2 class="related-section-heading">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/></svg>
            <span>DỊCH VỤ LÁI XE HỘ TẠI {loc["slug"].replace("-", " ").upper()}</span>
          </h2>
          <div class="services-grid">
            {related_services_html}
          </div>
        </div>
      </div>
    </section>
    '''

    html = render_page_shell(
        f"/khu-vuc/{loc['slug']}/",
        loc["title"],
        loc["meta_desc"],
        loc["h1"],
        body,
        og_image=loc["og_image"],
        schemas=[breadcrumb_schema]
    )
    write_html(f"khu-vuc/{loc['slug']}/index.html", html)

def main():
    print("Generating all 10 location pages (7 Da Nang districts + 3 routes)...")
    for loc in LOCATIONS_DATA:
        build_location_page(loc)
        print(f"  ✓ Built /khu-vuc/{loc['slug']}/index.html")

if __name__ == '__main__':
    main()
