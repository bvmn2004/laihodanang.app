import csv
import glob
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 1. Read all keywords from research/keywords/*.csv
all_raw_keywords = []
for f in sorted((PROJECT_ROOT / "research" / "keywords").glob("*.csv")):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for r in reader:
            if r and len(r) >= 3:
                kw = r[0].strip('"\ufeff ').lower()
                source = r[1].strip()
                intent = r[2].strip()
                all_raw_keywords.append((kw, source, intent))

# Deduplicate
unique_kws = {}
for kw, src, intent in all_raw_keywords:
    if kw not in unique_kws:
        unique_kws[kw] = {"source": src, "intent": intent}

print(f"Total unique keywords extracted from 11 CSVs: {len(unique_kws)}")

# Map each keyword to an exact target URL
def determine_target(kw):
    # Location specific
    if "hội an" in kw:
        return "/khu-vuc/da-nang-di-hoi-an/", "Khu vực & Tuyến đường", "Tài Xế Đà Nẵng Đi Hội An"
    if "huế" in kw:
        return "/khu-vuc/da-nang-di-hue/", "Khu vực & Tuyến đường", "Tài Xế Đà Nẵng Đi Huế"
    if "quảng ngãi" in kw:
        return "/khu-vuc/da-nang-di-quang-ngai/", "Khu vực & Tuyến đường", "Tài Xế Đà Nẵng Đi Quảng Ngãi"
    if "hải châu" in kw:
        return "/khu-vuc/hai-chau/", "Khu vực quận huyện", "Lái Xe Hộ Hải Châu Đà Nẵng"
    if "thanh khê" in kw:
        return "/khu-vuc/thanh-khe/", "Khu vực quận huyện", "Lái Xe Hộ Thanh Khê Đà Nẵng"
    if "sơn trà" in kw:
        return "/khu-vuc/son-tra/", "Khu vực quận huyện", "Lái Xe Hộ Sơn Trà Đà Nẵng"
    if "ngũ hành sơn" in kw:
        return "/khu-vuc/ngu-hanh-son/", "Khu vực quận huyện", "Lái Xe Hộ Ngũ Hành Sơn Đà Nẵng"
    if "liên chiểu" in kw:
        return "/khu-vuc/lien-chieu/", "Khu vực quận huyện", "Lái Xe Hộ Liên Chiểu Đà Nẵng"
    if "cẩm lệ" in kw:
        return "/khu-vuc/cam-le/", "Khu vực quận huyện", "Lái Xe Hộ Cẩm Lệ Đà Nẵng"
    if "hòa vang" in kw:
        return "/khu-vuc/hoa-vang/", "Khu vực quận huyện", "Lái Xe Hộ Hòa Vang Đà Nẵng"
    
    # Pricing
    if any(k in kw for k in ["bảng giá", "giá", "cước", "chi phí", "bao nhiêu tiền", "bao nhiêu"]):
        return "/bang-gia/", "Bảng giá", "Bảng Giá Lái Xe Hộ Đà Nẵng 2026"
    
    # Contact / App / Hotline / Booking
    if any(k in kw for k in ["số điện thoại", "hotline", "số hotline", "tổng đài", "liên hệ", "đặt xe", "app", "ứng dụng", "đặt tài xế"]):
        return "/lien-he/", "Liên hệ & Đặt xe", "Liên Hệ Đặt Tài Xế Lái Xe Hộ Đà Nẵng 24/7"
        
    # Vehicle types
    if any(k in kw for k in ["xe máy", "xe may"]):
        return "/dich-vu/lai-xe-ho-xe-may/", "Dịch vụ xe máy", "Lái Xe Hộ Xe Máy Đà Nẵng"
    if any(k in kw for k in ["ô tô", "o to", "xe hơi", "oto"]):
        return "/dich-vu/lai-xe-ho-o-to/", "Dịch vụ ô tô", "Lái Xe Hộ Ô Tô Đà Nẵng"
        
    # Specific services
    if any(k in kw for k in ["theo giờ", "theo gio"]):
        return "/dich-vu/thue-tai-xe-theo-gio/", "Dịch vụ theo giờ", "Thuê Tài Xế Theo Giờ Đà Nẵng"
    if any(k in kw for k in ["theo ngày", "theo ngay"]):
        return "/dich-vu/thue-tai-xe-theo-ngay/", "Dịch vụ theo ngày", "Thuê Tài Xế Theo Ngày Đà Nẵng"
    if any(k in kw for k in ["đi tỉnh", "di tinh", "liên tỉnh", "đường dài"]):
        return "/dich-vu/thue-tai-xe-di-tinh/", "Dịch vụ đi tỉnh", "Thuê Tài Xế Đi Tỉnh Đà Nẵng"
    if any(k in kw for k in ["bạn uống tôi lái", "ban uong toi lai"]):
        return "/dich-vu/ban-uong-toi-lai/", "Dịch vụ an toàn sau tiệc", "Bạn Uống Tôi Lái Đà Nẵng 24/7"
    if any(k in kw for k in ["say", "say rượu", "rượu bia", "uống bia", "sau tiệc", "quán nhậu", "say xỉn"]):
        return "/dich-vu/lai-xe-ho-sau-tiec/", "Dịch vụ sau tiệc", "Lái Xe Hộ Sau Tiệc Rượu Bia Đà Nẵng"
    if any(k in kw for k in ["đối tác", "vip", "sân bay"]):
        return "/dich-vu/thue-tai-xe-dua-don-doi-tac/", "Dịch vụ đối tác VIP", "Thuê Tài Xế Đón Đối Tác VIP"
    if any(k in kw for k in ["cưới", "tiệc cưới", "sự kiện"]):
        return "/dich-vu/thue-tai-xe-tiec-cuoi-su-kien/", "Dịch vụ sự kiện", "Tài Xế Phục Vụ Tiệc Cưới & Sự Kiện"
    if any(k in kw for k in ["đăng kiểm", "gara", "bảo dưỡng"]):
        return "/dich-vu/thue-tai-xe-giao-nhan-xe/", "Dịch vụ giao nhận xe", "Giao Nhận Xe Gara & Đăng Kiểm"

    # Guides & Blog
    if any(k in kw for k in ["là gì", "khái niệm", "định nghĩa"]):
        return "/blog/lai-xe-ho-la-gi/", "Cẩm nang kiến thức", "Lái Xe Hộ Là Gì"
    if any(k in kw for k in ["taxi", "so sánh", "nên chọn"]):
        return "/blog/lai-xe-ho-va-taxi-nen-chon-gi/", "Cẩm nang so sánh", "Lái Xe Hộ Và Taxi Nên Chọn Gì"
    if any(k in kw for k in ["khi nào", "trường hợp", "lý do"]):
        return "/blog/khi-nao-nen-goi-tai-xe-lai-ho/", "Cẩm nang tư vấn", "Khi Nào Nên Gọi Tài Xế Lái Hộ"
    if any(k in kw for k in ["quy trình", "hướng dẫn", "các bước"]):
        return "/blog/quy-trinh-dat-tai-xe-nhu-y-driver/", "Cẩm nang quy trình", "Quy Trình Đặt Tài Xế Như Ý Driver"
    if any(k in kw for k in ["bàn giao", "chìa khóa", "chuẩn bị"]):
        return "/blog/chuan-bi-khi-ban-giao-xe/", "Cẩm nang chuẩn bị", "Chuẩn Bị Khi Bàn Giao Xe Cho Tài Xế"
    if any(k in kw for k in ["ban đêm", "đêm", "khuya"]):
        return "/blog/dat-tai-xe-lai-ho-ban-dem/", "Cẩm nang ban đêm", "Đặt Tài Xế Lái Hộ Ban Đêm Đà Nẵng"
    if any(k in kw for k in ["buồn ngủ", "mệt mỏi"]):
        return "/blog/buon-ngu-khi-lai-xe/", "Cẩm nang an toàn", "Xử Lý Buồn Ngủ Khi Lái Xe"
    if any(k in kw for k in ["tự lái"]):
        return "/blog/thue-xe-tu-lai-goi-tai-xe/", "Cẩm nang thuê xe", "Thuê Xe Tự Lái Cần Tài Xế"
        
    # Default to Homepage
    return "/", "Trang chủ thương hiệu", "Lái Xe Hộ Đà Nẵng Giá Từ 150K | Như Ý Driver 24/7"

fieldnames = [
    "Keyword",
    "Search Intent",
    "Keyword Cluster",
    "Target URL",
    "Page Role",
    "Source",
    "Canonical Domain"
]

rows = []
url_counter = defaultdict(int)

for kw, data in sorted(unique_kws.items()):
    target_url, cluster, page_role = determine_target(kw)
    url_counter[target_url] += 1
    rows.append({
        "Keyword": kw,
        "Search Intent": data["intent"],
        "Keyword Cluster": cluster,
        "Target URL": target_url,
        "Page Role": page_role,
        "Source": data["source"],
        "Canonical Domain": "https://laihodanang.app/"
    })

out_path = PROJECT_ROOT / "research" / "keyword-map.csv"
with open(out_path, "w", encoding="utf-8-sig", newline="") as fp:
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"\nSuccessfully wrote {len(rows)} mapped keywords to {out_path}")
print("\nURL Mapping Distribution:")
for u, c in sorted(url_counter.items(), key=lambda x: -x[1]):
    print(f"  {u:45} : {c:3} keywords")

