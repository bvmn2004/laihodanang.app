# LÁI XE HỘ NHƯ Ý DRIVER (ĐÀ NẴNG) – SOURCE CODE WEBSITE HOÀN CHỈNH

**Website chính thức:** [https://laihodanang.app](https://laihodanang.app)  
**Hotline 24/7:** **0985 666 044**  
**Zalo đặt xe:** [https://zalo.me/0985666044](https://zalo.me/0985666044)  
**Địa bàn:** Thành phố Đà Nẵng và các vùng phụ cận (Hội An, Huế, Quảng Nam, Quảng Ngãi).

---

## 1. TỔNG QUAN HỆ THỐNG WEBSITE

Website được phát triển theo tiêu chuẩn **Modern Premium Automotive & Local SEO 2026** dành riêng cho thương hiệu **Lái Xe Hộ Như Ý Driver**.

### Điểm nổi bật về kỹ thuật & hiệu năng:
- **Kiến trúc tĩnh 100% (Static Site Architecture):** Triển khai trực tiếp và tối ưu hoàn hảo trên nền tảng **GitHub Pages** thông qua custom domain `laihodanang.app`.
- **Điểm số Lighthouse Audit thực tế:**
  - 🚀 **Performance: 100 / 100**
  - ♿ **Accessibility: 97 / 100**
  - 🛡️ **Best Practices: 100 / 100**
  - 🔍 **SEO: 100 / 100**
- **100% Ảnh chụp thật độc bản:** Sử dụng toàn bộ 43 ảnh chụp thực tế của đội ngũ tài xế Như Ý Driver mặc đồng phục áo gile đỏ tại Cầu Rồng và các địa danh Đà Nẵng. Toàn bộ ảnh đã được nén tối ưu sang định dạng **WebP** thế hệ mới (giảm hơn 90% dung lượng mà vẫn giữ nguyên độ sắc nét).
- **Cấu trúc Topic Cluster bao phủ toàn diện:** 36 trang web độc lập, không trùng lặp, tối ưu semantic HTML5, canonical URL, OpenGraph, Twitter Card và đầy đủ dữ liệu có cấu trúc **Schema.org** (`AutomotiveBusiness`, `Service`, `BreadcrumbList`, `FAQPage`, `BlogPosting`).
- **Tối ưu tỷ lệ chuyển đổi (CRO):**
  - Bảng giá minh bạch công khai: **Ô tô từ 150K (0-5km)**, **Xe máy từ 110K (0-5km)**, phụ phí đêm sau 23h +50K.
  - Công cụ tính nhanh giá cước tương tác bằng JavaScript ngay trên trang chủ và trang bảng giá.
  - Thanh liên hệ dính chân trang di động (**Sticky Mobile Floating Bar**) giúp khách hàng bấm gọi điện thoại hoặc nhắn tin Zalo tức thì chỉ trong 1 chạm.

---

## 2. CẤU TRÚC THƯ MỤC SOURCE CODE

```text
laihodanang.app/
├── index.html                           # Trang chủ chuẩn chuyển đổi cao (Hero H1 giá từ 150K)
├── 404.html                             # Trang lỗi 404 tùy chỉnh thân thiện
├── CNAME                                # Khai báo custom domain: laihodanang.app
├── robots.txt                           # Hướng dẫn bot công cụ tìm kiếm
├── sitemap.xml                          # Sơ đồ trang web chứa 36 URLs chuẩn SEO
├── README.md                            # Tài liệu hướng dẫn vận hành và triển khai
│
├── gioi-thieu/
│   └── index.html                       # Về Như Ý Driver, tiêu chuẩn tuyển chọn, đội ngũ tài xế
├── bang-gia/
│   └── index.html                       # Bảng giá chi tiết ô tô & xe máy, phụ phí đêm, công cụ tính cước
├── khu-vuc/
│   ├── index.html                       # Tổng quan khu vực phục vụ khắp TP. Đà Nẵng
│   ├── hai-chau/index.html              # Lái xe hộ Quận Hải Châu (Bạch Đằng, Nguyễn Văn Linh, 2/9...)
│   ├── son-tra/index.html               # Lái xe hộ Quận Sơn Trà (Võ Nguyên Giáp, Phạm Văn Đồng, Hồ Nghinh...)
│   ├── da-nang-di-hoi-an/index.html     # Thuê tài xế tuyến Đà Nẵng - Hội An
│   ├── da-nang-di-hue/index.html        # Thuê tài xế tuyến Đà Nẵng - Huế (Đèo & Hầm Hải Vân)
│   └── da-nang-di-quang-ngai/index.html # Thuê tài xế tuyến Đà Nẵng - Quảng Ngãi
│
├── dich-vu/
│   ├── index.html                       # Tổng hợp tất cả dịch vụ lái xe hộ
│   ├── lai-xe-ho-o-to/index.html        # Dịch vụ lái xe hộ ô tô (Giá từ 150K)
│   ├── lai-xe-ho-xe-may/index.html      # Dịch vụ lái xe hộ xe máy (Giá từ 110K)
│   ├── ban-uong-toi-lai/index.html      # Dịch vụ Bạn uống tôi lái 24/7
│   ├── lai-xe-ho-sau-tiec/index.html    # Dịch vụ lái xe hộ sau tiệc rượu, đưa người say về nhà
│   ├── thue-tai-xe-theo-gio/index.html  # Thuê tài xế theo giờ linh hoạt
│   ├── thue-tai-xe-theo-ngay/index.html # Thuê tài xế theo ngày (công tác, du lịch, city tour)
│   ├── thue-tai-xe-di-tinh/index.html   # Thuê tài xế đường dài đi tỉnh
│   ├── thue-tai-xe-dua-don-doi-tac/index.html # Thuê tài xế đưa đón đối tác & khách VIP
│   ├── thue-tai-xe-tiec-cuoi-su-kien/index.html # Tài xế phục vụ tiệc cưới & sự kiện
│   └── thue-tai-xe-giao-nhan-xe/index.html      # Dịch vụ giao nhận xe gara, đăng kiểm
│
├── blog/
│   ├── index.html                       # Cẩm nang lái xe an toàn & kiến thức nồng độ cồn
│   ├── lai-xe-ho-la-gi/index.html
│   ├── lai-xe-ho-va-taxi-nen-chon-gi/index.html
│   ├── khi-nao-nen-goi-tai-xe-lai-ho/index.html
│   ├── quy-trinh-dat-tai-xe-nhu-y-driver/index.html
│   ├── chuan-bi-khi-ban-giao-xe/index.html
│   ├── dat-tai-xe-lai-ho-ban-dem/index.html
│   ├── buon-ngu-khi-lai-xe/index.html
│   ├── uong-ruou-bia-mang-theo-xe-may/index.html
│   ├── di-tiec-bang-o-to-da-nang/index.html
│   ├── thue-tai-xe-theo-gio-hay-theo-ngay/index.html
│   ├── thue-xe-tu-lai-goi-tai-xe/index.html
│   ├── thue-tai-xe-da-nang-di-hoi-an/index.html
│   └── thue-tai-xe-da-nang-di-hue/index.html
│
├── assets/
│   ├── css/
│   │   └── style.css                    # Hệ thống CSS Design System chuyên nghiệp
│   ├── js/
│   │   └── main.js                      # Core JS: Menu mobile, Accordion, Tính giá cước, Event tracking
│   └── images/                          # 43 ảnh gốc và 43 ảnh nén WebP chất lượng cao
│
├── research/
│   ├── keywords/                        # 11 file CSV gốc từ khóa 2026-10-30
│   ├── keywords_combined.csv            # Dữ liệu gộp 509 từ khóa duy nhất
│   ├── keyword-research-full.csv        # Bảng nghiên cứu chi tiết đầy đủ
│   ├── keyword-map.csv                  # Keyword Mapping chuẩn SEO cho 36 trang
│   ├── serp-analysis.md                 # Báo cáo phân tích đối thủ cạnh tranh trên SERP Đà Nẵng
│   ├── image-manifest.json              # Bản kê khai toàn bộ hình ảnh và alt text chuẩn SEO
│   └── lighthouse-report.json           # Báo cáo kiểm định chất lượng Lighthouse (100/97/100/100)
│
└── scripts/                             # Hệ thống công cụ tự động hóa build website
    ├── process_keywords.py              # Đọc và gộp 11 file CSV từ khóa
    ├── build_research_and_manifest.py   # Phân loại ý định, tạo keyword map và manifest
    ├── process_images.py                # Quét ảnh, chuyển đổi sang WebP và đo lường kích thước
    ├── site_components.py               # Shared header, navigation, footer, breadcrumbs
    ├── site_builder_core.py             # Render HTML shell với đầy đủ JSON-LD Schema
    ├── generate_home.py                 # Sinh mã nguồn trang chủ index.html
    ├── generate_main_pages.py           # Sinh mã nguồn các trang giới thiệu, bảng giá, liên hệ, 404
    ├── generate_services.py             # Sinh mã nguồn hub dịch vụ và 10 landing page dịch vụ
    ├── generate_locations.py            # Sinh mã nguồn các trang quận huyện và tuyến đường
    ├── generate_blog.py                 # Sinh mã nguồn hub blog và 13 bài viết cẩm nang
    ├── generate_seo_assets.py           # Sinh sitemap.xml, robots.txt, CNAME
    └── verify_website.py                # Kiểm tra toàn diện HTML, link hỏng, ảnh thiếu, H1, Schema
```

---

## 3. HƯỚNG DẪN TRIỂN KHAI LÊN GITHUB PAGES & CẤU HÌNH TÊN MIỀN

### Bước 1: Khởi tạo Git repository và Push mã nguồn
Mở terminal PowerShell tại thư mục dự án `d:\MINHNGUYET\laihodanang.app`:

```powershell
# 1. Khởi tạo repository
git init

# 2. Thêm toàn bộ source code
git add .

# 3. Tạo commit đầu tiên
git commit -m "feat: complete production website for laihodanang.app with full SEO & authentic photos"

# 4. Đặt nhánh chính là main
git branch -M main

# 5. Thêm remote trỏ về repository trên GitHub của bạn
git remote add origin https://github.com/<your-username>/<your-repo-name>.git

# 6. Push mã nguồn lên GitHub
git push -u origin main
```

### Bước 2: Kích hoạt GitHub Pages
1. Truy cập vào GitHub repository của bạn trên trình duyệt.
2. Nhấn vào tab **Settings** &rarr; chọn mục **Pages** ở thanh menu bên trái.
3. Tại phần **Build and deployment**:
   - **Source:** Chọn `Deploy from a branch`
   - **Branch:** Chọn `main`, thư mục `/ (root)` &rarr; Nhấn **Save**.
4. Tại phần **Custom domain**:
   - Nhập `laihodanang.app` &rarr; Nhấn **Save**.
   - GitHub sẽ tự động tạo file `CNAME` (nếu chưa có) và tiến hành kiểm tra DNS.

### Bước 3: Cấu hình bản ghi DNS trên Name.com
Đăng nhập vào tài khoản quản lý tên miền tại **Name.com**, chọn tên miền `laihodanang.app`, vào mục **DNS Records** và thêm các bản ghi sau:

| Loại bản ghi (Type) | Tên máy chủ (Host / Name) | Giá trị đích (Answer / Value) | TTL |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `185.199.108.153` | 300 |
| **A** | `@` | `185.199.109.153` | 300 |
| **A** | `@` | `185.199.110.153` | 300 |
| **A** | `@` | `185.199.111.153` | 300 |
| **CNAME** | `www` | `<your-username>.github.io` | 300 |

*Lưu ý: Thời gian cập nhật DNS trên toàn cầu thường mất từ 5 đến 30 phút.*

### Bước 4: Bật bảo mật HTTPS
Sau khi bản ghi DNS trỏ thành công về GitHub Pages:
1. Quay lại trang **Settings &rarr; Pages** trên GitHub.
2. Tích chọn vào ô **Enforce HTTPS** để kích hoạt chứng chỉ SSL miễn phí tự động của GitHub.

---

## 4. XÁC MINH GOOGLE SEARCH CONSOLE & GỬI SITEMAP

1. Truy cập [Google Search Console](https://search.google.com/search-console).
2. Chọn **Thêm tài sản (Add Property)** &rarr; Chọn phương thức **Tiền tố URL (URL prefix)**: nhập `https://laihodanang.app`.
3. Xác minh quyền sở hữu:
   - Cách 1: Tải file HTML xác minh của Google đặt vào thư mục gốc `d:\MINHNGUYET\laihodanang.app/` rồi push lên GitHub.
   - Cách 2: Thêm thẻ `<meta name="google-site-verification" content="..." />` vào thẻ `<head>` trong file `scripts/site_builder_core.py` và chạy lại lệnh build.
   - Cách 3: Thêm bản ghi DNS TXT trên Name.com.
4. Gửi Sơ đồ trang web:
   - Vào mục **Sơ đồ trang web (Sitemaps)** trên Search Console.
   - Nhập `sitemap.xml` &rarr; Nhấn **Gửi (Submit)**.
   - Google sẽ thu thập và lập chỉ mục toàn bộ 36 trang web của bạn.

---

## 5. HƯỚNG DẪN CẬP NHẬT NỘI DUNG VỀ SAU

Hệ thống được thiết kế theo dạng module hóa cực kỳ tiện lợi:
- **Thêm bài viết cẩm nang mới:** Mở file `scripts/generate_blog.py`, thêm một đối tượng bài viết vào danh sách `BLOG_POSTS`.
- **Cập nhật giá cước hoặc số hotline:** Sửa các hằng số tại `scripts/site_components.py`.
- **Chạy lệnh tái tạo toàn bộ website chỉ trong 5 giây:**
  ```powershell
  python scripts/generate_home.py
  python scripts/generate_main_pages.py
  python scripts/generate_services.py
  python scripts/generate_locations.py
  python scripts/generate_blog.py
  python scripts/generate_seo_assets.py
  python scripts/verify_website.py
  ```
- Sau đó chỉ cần `git add .`, `git commit -m "update"` và `git push origin main`, website sẽ tự động cập nhật ngay lập tức trên môi trường live!

