import sys
from site_components import (
    BASE_URL, BRAND_NAME, HOTLINE, HOTLINE_TEL, ZALO_URL,
    FACEBOOK_URL, EMAIL, AREA, picture_tag, render_breadcrumbs, render_related_topics
)
from site_builder_core import render_page_shell, write_html

sys.stdout.reconfigure(encoding='utf-8')

def build_about():
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/gioi-thieu/", "title": "Giới Thiệu"}
    ])
    
    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">VỀ NHƯ Ý DRIVER – DỊCH VỤ LÁI XE HỘ CHUYÊN NGHIỆP TẠI ĐÀ NẴNG</h1>
        <p class="page-hero-desc">
          Sứ mệnh mang lại sự an tâm tuyệt đối sau mỗi cuộc vui, đồng hành bảo vệ an toàn giao thông cho người dân và du khách tại TP. Đà Nẵng.
        </p>
      </div>
    </section>

    <!-- SECTION MISSION & STORY -->
    <section class="section">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge">Câu Chuyện Của Chúng Tôi</span>
            <h2 class="split-title">ĐÃ UỐNG RƯỢU BIA – HÃY ĐỂ TÀI XẾ LÁI XE CỦA BẠN</h2>
            <p class="split-desc">
              Đà Nẵng – thành phố đáng sống với văn hóa ẩm thực, du lịch và giao lưu sôi động. Tuy nhiên, sau những bữa tiệc liên hoan, gặp gỡ đối tác hay sum họp gia đình, việc tự lái xe khi đã có nồng độ cồn không chỉ tiềm ẩn rủi ro nghiêm trọng về an toàn giao thông mà còn đối diện với mức xử phạt hành chính rất nặng.
            </p>
            <p class="split-desc">
              Thấu hiểu nỗi băn khoăn của khách hàng khi không muốn để lại xe hơi tiền tỷ hoặc xe máy đắt tiền qua đêm tại các quán xá, <strong>Lái Xe Hộ Như Ý Driver</strong> ra đời nhằm cung cấp giải pháp trọn vẹn: <em>Tài xế lái chính phương tiện của khách hàng, đưa cả người và xe về tận cổng nhà an toàn.</em>
            </p>
            <div class="split-checklist">
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>An toàn tuyệt đối:</strong> Đặt tính mạng và tài sản của khách hàng lên hàng đầu.</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>Bảo mật & Tận tâm:</strong> Tôn trọng sự riêng tư, hỗ trợ chu đáo từ lúc nhận chìa khóa đến khi bàn giao tại nhà.</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>Giá cước minh bạch:</strong> Báo giá rõ ràng trước khi đi, cam kết không phụ phí vô lý.</span>
              </div>
            </div>
          </div>
          <div class="split-media-wrap">
            {picture_tag("14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.png", "Khách hàng tin tưởng giao chìa khóa cho tài xế Như Ý Driver", "split-media-img", 1536, 1024, lazy=False)}
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION DRIVER CRITERIA -->
    <section class="section section-gray">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Tiêu Chuẩn Khắt Khe</span>
          <h2 class="section-title">TIÊU CHÍ TUYỂN CHỌN & ĐÀO TẠO TÀI XẾ</h2>
          <p class="section-lead">Mỗi tài xế Như Ý Driver là một người bạn đường đáng tin cậy</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px;">
          <div style="background:#fff; padding:28px 24px; border-radius:var(--radius-lg); border:1px solid var(--border); box-shadow:var(--shadow-sm);">
            <div style="width:48px; height:48px; background:var(--gold-bg); border-radius:var(--radius-full); display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--red)"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Hồ Sơ Minh Bạch</h3>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
              100% tài xế được xác minh danh tính, lý lịch tư pháp trong sạch, giấy phép lái xe hợp lệ từ hạng B2 trở lên.
            </p>
          </div>

          <div style="background:#fff; padding:28px 24px; border-radius:var(--radius-lg); border:1px solid var(--border); box-shadow:var(--shadow-sm);">
            <div style="width:48px; height:48px; background:var(--gold-bg); border-radius:var(--radius-full); display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--red)"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/></svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Kinh Nghiệm Thực Chiến</h3>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
              Tối thiểu 5 năm cầm lái thực tế, am hiểu kỹ thuật lái xe số sàn, số tự động và mọi hệ thống điều khiển xe sang.
            </p>
          </div>

          <div style="background:#fff; padding:28px 24px; border-radius:var(--radius-lg); border:1px solid var(--border); box-shadow:var(--shadow-sm);">
            <div style="width:48px; height:48px; background:var(--gold-bg); border-radius:var(--radius-full); display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--red)"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Thông Thạo Địa Bàn</h3>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
              Nắm vững từng con hẻm, đường một chiều, giờ cao điểm tại Đà Nẵng và các cung đường đèo, đường đi tỉnh.
            </p>
          </div>

          <div style="background:#fff; padding:28px 24px; border-radius:var(--radius-lg); border:1px solid var(--border); box-shadow:var(--shadow-sm);">
            <div style="width:48px; height:48px; background:var(--gold-bg); border-radius:var(--radius-full); display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--red)"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
            </div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Văn Hóa Phục Vụ</h3>
            <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
              Mặc đồng phục vest đỏ chỉn chu, giao tiếp lịch thiệp, giữ gìn vệ sinh nội thất xe và hỗ trợ khách hàng tận cửa nhà.
            </p>
          </div>
        </div>

        <div style="margin-top:40px; text-align:center;">
          {picture_tag("15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png", "Đội ngũ tài xế Như Ý Driver đồng phục đỏ túc trực tại Cầu Rồng Đà Nẵng", "split-media-img", 1536, 1024)}
        </div>
      </div>
    </section>

    <!-- SECTION CTA -->
    <section class="section section-navy" style="text-align:center;">
      <div class="container" style="max-width:750px;">
        <h2 style="font-size:2rem; font-weight:800; margin-bottom:14px;">ĐỒNG HÀNH CÙNG NHƯ Ý DRIVER NGAY HÔM NAY</h2>
        <p style="color:#cbd5e1; font-size:1.05rem; margin-bottom:28px;">
          Lưu ngay số điện thoại hotline để sẵn sàng gọi tài xế cho bất kỳ cuộc vui nào của bạn và bạn bè tại Đà Nẵng.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="{HOTLINE_TEL}" class="btn-primary" style="font-size:1.1rem; padding:14px 32px;" aria-label="Gọi ngay hotline Như Ý Driver 0985 666 044">GỌI NGAY: {HOTLINE}</a>
          <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" style="font-size:1.1rem; padding:14px 32px;" aria-label="Kết nối Zalo đặt xe 0985 666 044">KẾT NỐI ZALO</a>
        </div>
      </div>
    </section>
    '''

    title = "Giới Thiệu Như Ý Driver | Dịch Vụ Lái Xe Hộ Chuyên Nghiệp Đà Nẵng"
    meta_desc = "Đội ngũ tài xế chuyên nghiệp, lịch sự, thông thạo đường phố Đà Nẵng. Cam kết an toàn, phục vụ tận tâm 24/7 cho cả ô tô và xe máy. Hotline: 0985 666 044."
    h1 = "VỀ NHƯ Ý DRIVER – DỊCH VỤ LÁI XE HỘ CHUYÊN NGHIỆP TẠI ĐÀ NẴNG"

    html = render_page_shell("/gioi-thieu/", title, meta_desc, h1, body, og_image="/assets/images/15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.webp", schemas=[breadcrumb_schema])
    write_html("gioi-thieu/index.html", html)

def build_pricing():
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/bang-gia/", "title": "Bảng Giá"}
    ])

    faq_data = [
        {
            "q": "Bảng giá lái xe hộ ô tô tính như thế nào?",
            "a": "Giá mở cửa khung 0 - 5 km là 150.000đ. Khung 5 - 10 km là 200.000đ cố định. Trên 10 km đến 30 km tính 200.000đ cho 10 km đầu, các km tiếp theo tính 15.000đ/km. Trên 30 km là tuyến đường dài/đi tỉnh với giá thỏa thuận trọn gói ưu đãi."
        },
        {
            "q": "Khung giờ khuya sau 23h tính phụ phí bao nhiêu?",
            "a": "Phụ phí đêm là 50.000đ/chuyến, áp dụng từ 23:00 đêm đến 05:59 sáng hôm sau. Mức phí này được tính nhằm hỗ trợ tài xế trực đêm, được thông báo trước rõ ràng và không phát sinh thêm khoản nào khác."
        },
        {
            "q": "Nếu tôi đi nhiều điểm dừng hoặc cần tài xế chờ thì sao?",
            "a": "Tài xế miễn phí chờ 15 - 30 phút đầu tiên. Nếu phát sinh chờ lâu hoặc dừng nhiều điểm đón người, cước phát sinh sẽ được thỏa thuận minh bạch từ 50.000đ/giờ chờ hoặc bạn có thể chọn gói thuê theo giờ tiện lợi hơn."
        },
        {
            "q": "Như Ý Driver có hỗ trợ lái xe máy về nhà không?",
            "a": "Có! Chúng tôi phục vụ lái hộ cả ô tô và xe máy. Cước xe máy chỉ từ 110.000đ (0 - 5 km), 130.000đ (5 - 7 km), 170.000đ (7 - 10 km) và 10.000đ/km cho các km tiếp theo."
        }
    ]

    faq_html = []
    faq_schema_items = []
    for i, item in enumerate(faq_data):
        faq_schema_items.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {"@type": "Answer", "text": item["a"]}
        })
        faq_html.append(f'''
        <div class="faq-item {'active' if i==0 else ''}">
          <button type="button" class="faq-question-btn" aria-expanded="{'true' if i==0 else 'false'}">
            <span>{item["q"]}</span>
            <svg class="faq-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer"><p>{item["a"]}</p></div>
        </div>
        ''')

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema_items}

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">BẢNG GIÁ DỊCH VỤ LÁI XE HỘ ĐÀ NẴNG MỚI NHẤT 2026</h1>
        <p class="page-hero-desc">
          Công khai – Minh bạch – Không phí ẩn. Áp dụng toàn diện cho cả Ô tô và Xe máy trên toàn địa bàn TP. Đà Nẵng 24/7.
        </p>
      </div>
    </section>

    <!-- SECTION PRICING TABLES -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Bảng Cước Chi Tiết</span>
          <h2 class="section-title">BẢNG GIÁ CƯỚC NỘI THÀNH ĐÀ NẴNG</h2>
          <p class="section-lead">Dưới đây là chi tiết giá cước chuẩn được áp dụng thực tế tại Như Ý Driver</p>
        </div>

        <div class="pricing-grid">
          <!-- Car Pricing -->
          <div class="pricing-card featured">
            <span class="featured-ribbon">Dành cho Ô Tô</span>
            <div class="pricing-card-header">
              <div class="pricing-card-title">Lái Xe Hộ Ô Tô</div>
              <div class="pricing-card-sub">Áp dụng cho xe 4 chỗ, 7 chỗ, SUV, bán tải và xe sang</div>
              <div class="pricing-start-at">
                <span class="price-big">150.000đ</span>
                <span class="price-unit">/ cự ly 0 – 5 km</span>
              </div>
            </div>
            <div class="pricing-card-body">
              <table class="pricing-table-clean">
                <thead>
                  <tr>
                    <th>Quãng đường</th>
                    <th>Giá dịch vụ</th>
                    <th>Ví dụ minh họa</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>0 – 5 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">150.000đ</td>
                    <td>Đi 3 km: 150.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>5 – 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">200.000đ</td>
                    <td>Đi 8 km: 200.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>Trên 10 – 30 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">200k + 15k/km</td>
                    <td>Đi 15 km = 200k + 5×15k = 275.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>Trên 30 km</strong></td>
                    <td style="color:var(--navy); font-weight:700;">Thỏa thuận</td>
                    <td>Liên hệ hotline để báo giá trọn gói</td>
                  </tr>
                </tbody>
              </table>

              <div class="pricing-notes-box">
                <strong>Phụ phí giờ khuya sau 23:00:</strong> +50.000đ/chuyến (áp dụng cho chuyến đi từ 23:00 đến 05:59 sáng hôm sau).
              </div>
            </div>
            <div class="pricing-card-footer">
              <a href="{HOTLINE_TEL}" class="btn-primary" style="justify-content:center;" aria-label="Gọi đặt tài xế ô tô 0985 666 044">GỌI TÀI XẾ Ô TÔ NGAY</a>
            </div>
          </div>

          <!-- Motorbike Pricing -->
          <div class="pricing-card">
            <span class="featured-ribbon" style="background:var(--navy);">Dành cho Xe Máy</span>
            <div class="pricing-card-header">
              <div class="pricing-card-title">Lái Xe Hộ Xe Máy</div>
              <div class="pricing-card-sub">Lái chính xe máy đưa bạn và xe về nhà an toàn</div>
              <div class="pricing-start-at">
                <span class="price-big">110.000đ</span>
                <span class="price-unit">/ cự ly 0 – 5 km</span>
              </div>
            </div>
            <div class="pricing-card-body">
              <table class="pricing-table-clean">
                <thead>
                  <tr>
                    <th>Quãng đường</th>
                    <th>Đơn giá</th>
                    <th>Quy cách tính</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>0 – 5 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">110.000đ</td>
                    <td>Cố định theo chặng</td>
                  </tr>
                  <tr>
                    <td><strong>5 – 7 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">130.000đ</td>
                    <td>Cố định theo chặng</td>
                  </tr>
                  <tr>
                    <td><strong>7 – 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">170.000đ</td>
                    <td>Cố định theo chặng</td>
                  </tr>
                  <tr>
                    <td><strong>Qua 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">+10.000đ/km</td>
                    <td>Cộng thêm mỗi km tiếp theo</td>
                  </tr>
                </tbody>
              </table>

              <div class="pricing-notes-box">
                <strong>Qua 23h:</strong> +50.000đ giờ khuya. Bảo đảm bạn không phải gửi xe qua đêm lo nơm nớp trầy xước, mất gương, cháy nổ.
              </div>
            </div>
            <div class="pricing-card-footer">
              <a href="{HOTLINE_TEL}" class="btn-primary" style="justify-content:center; background:var(--navy);" aria-label="Gọi đặt tài xế xe máy 0985 666 044">GỌI TÀI XẾ XE MÁY NGAY</a>
            </div>
          </div>
        </div>

        <!-- INFOGRAPHIC IMAGES VERIFICATION -->
        <div style="margin-top:60px; display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap:30px;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:12px; text-align:center;">Bảng giá Ô Tô chính thức</h3>
            {picture_tag("16_Bang_Gia_Lai_Xe_OTo_Ho.png", "Bảng giá lái xe ô tô hộ Như Ý Driver Đà Nẵng", "split-media-img", 1122, 1402, lazy=False)}
          </div>
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--navy); margin-bottom:12px; text-align:center;">Bảng giá Xe Máy chính thức</h3>
            {picture_tag("16_Bang_Gia_Lai_Xe_May_Ho.png", "Bảng giá lái xe máy hộ Như Ý Driver Đà Nẵng", "split-media-img", 1122, 1402, lazy=False)}
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION COST COMPARISON -->
    <section class="section section-gray">
      <div class="container" style="max-width:900px;">
        <div class="section-header">
          <span class="section-subtitle">Bài Toán Kinh Tế</span>
          <h2 class="section-title">SO SÁNH CHI PHÍ THỰC TẾ</h2>
          <p class="section-lead">Lái xe hộ giúp bạn tiết kiệm chi phí và thời gian như thế nào?</p>
        </div>

        <div style="background:#fff; border-radius:var(--radius-lg); border:1px solid var(--border); overflow-x:auto; -webkit-overflow-scrolling:touch; box-shadow:var(--shadow-md);">
          <table class="pricing-table-clean" style="margin:0;">
            <thead>
              <tr style="background:var(--navy); color:#fff;">
                <th style="color:#fff; padding:14px 16px;">Phương án</th>
                <th style="color:#fff; padding:14px 16px;">Chi phí ước tính</th>
                <th style="color:#fff; padding:14px 16px;">Bất tiện & Rủi ro</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Phương án 1: Gọi Taxi 2 chiều & gửi xe lại quán</strong></td>
                <td>250.000đ – 400.000đ<br><small>(Taxi đi + về + tiền gửi xe qua đêm)</small></td>
                <td>Sáng hôm sau mất 1 - 2 tiếng quay lại lấy xe, nguy cơ trầy xước, mất đồ hoặc vặt gương xe.</td>
              </tr>
              <tr>
                <td><strong>Phương án 2: Cố tự lái xe về khi đã uống rượu bia</strong></td>
                <td><span style="color:var(--red); font-weight:800;">7.000.000đ – 40.000.000đ</span><br><small>Tước GPLX 11 - 24 tháng, tạm giữ xe</small></td>
                <td>Nguy hiểm trực tiếp đến tính mạng bản thân và người tham gia giao thông, tiền án tiền sự nếu xảy ra va chạm.</td>
              </tr>
              <tr style="background:var(--gold-bg);">
                <td><strong style="color:var(--navy);">Phương án 3: Gọi Như Ý Driver lái hộ</strong></td>
                <td><strong style="color:var(--red); font-size:1.15rem;">150.000đ – 200.000đ</strong><br><small>Trọn gói cả người và xe về nhà</small></td>
                <td><strong>Hoàn hảo:</strong> Về nhà an toàn, sáng hôm sau xe đã sẵn sàng ở gara để đi làm, không lo phạt nồng độ cồn!</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- SECTION PRICING FAQ -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Thắc Mắc Chi Phí</span>
          <h2 class="section-title">CÂU HỎI VỀ BẢNG GIÁ LÁI XE HỘ</h2>
        </div>
        <div class="faq-wrap">
          {''.join(faq_html)}
        </div>

        <div style="margin-top:40px;">
          {render_related_topics([
            ("Lái xe hộ ô tô từ 150K", "/dich-vu/lai-xe-ho-o-to/"),
            ("Lái xe hộ xe máy từ 110K", "/dich-vu/lai-xe-ho-xe-may/"),
            ("Bạn uống tôi lái 24/7", "/dich-vu/ban-uong-toi-lai/"),
            ("Thuê tài xế theo giờ", "/dich-vu/thue-tai-xe-theo-gio/"),
            ("Thuê tài xế đi tỉnh", "/dich-vu/thue-tai-xe-di-tinh/"),
            ("Thuê tài xế đi Hội An", "/khu-vuc/da-nang-di-hoi-an/"),
            ("Thuê tài xế đi Huế", "/khu-vuc/da-nang-di-hue/"),
            ("Liên hệ đặt xe 0985 666 044", "/lien-he/")
          ], "Dịch vụ & Chủ đề liên quan")}
        </div>
      </div>
    </section>
    '''

    title = "Bảng Giá Lái Xe Hộ Đà Nẵng 2026 | Ô Tô Từ 150K, Xe Máy Từ 110K"
    meta_desc = "Bảng giá lái xe hộ Đà Nẵng công khai, minh bạch: Ô tô từ 150.000đ (0-5km), Xe máy từ 110.000đ (0-5km). Phụ phí đêm sau 23h +50.000đ. Không phí ẩn. Gọi 0985 666 044."
    h1 = "BẢNG GIÁ DỊCH VỤ LÁI XE HỘ ĐÀ NẴNG MỚI NHẤT 2026"

    html = render_page_shell("/bang-gia/", title, meta_desc, h1, body, og_image="/assets/images/01_Bang_Gia_Lai_Xe_Ho_Da_Nang_2026.webp", schemas=[breadcrumb_schema, faq_schema])
    write_html("bang-gia/index.html", html)

def build_locations_hub():
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/khu-vuc/", "title": "Khu Vực"}
    ])

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">KHU VỰC PHỤC VỤ LÁI XE HỘ KHẮP ĐÀ NẴNG 24/7</h1>
        <p class="page-hero-desc">
          Mạng lưới tài xế Như Ý Driver phân bổ khắp 7 địa bàn truyền thống tại Đà Nẵng và các tuyến liên tỉnh toàn quốc. Có mặt dự kiến sau 15–20 phút nội thành.
        </p>
      </div>
    </section>

    <!-- SECTION LOCAL HUBS -->
    <section class="section">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge">Mạng Lưới Phủ Khắp</span>
            <h2 class="split-title">ĐẶT TÀI XẾ MỌI LÚC MỌI NƠI TẠI ĐÀ NẴNG</h2>
            <p class="split-desc">
              Dù bạn đang ở nhà hàng ven sông Hàn, quán hải sản đường biển Sơn Trà, hay các khu dân cư Cẩm Lệ, Liên Chiểu, Ngũ Hành Sơn, Thanh Khê, Hòa Vang, chỉ cần một cuộc gọi đến <a href="{HOTLINE_TEL}" aria-label="Gọi hotline Như Ý Driver 0985 666 044"><strong>{HOTLINE}</strong></a>, tài xế gần nhất sẽ lập tức di chuyển đến đón bạn.
            </p>
            <div class="split-checklist">
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Hải Châu & Thanh Khê:</strong> Bạch Đằng, Như Nguyệt, 2/9, Nguyễn Văn Linh, Điện Biên Phủ, biển Nguyễn Tất Thành.</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Sơn Trà & Ngũ Hành Sơn:</strong> Tuyến biển Võ Nguyên Giáp, Trường Sa, phố Tây An Thượng, Phạm Văn Đồng, Non Nước.</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Liên Chiểu & Cẩm Lệ:</strong> Tuyến KCN Hòa Khánh, Tôn Đức Thắng, CMT8, KĐT Hòa Xuân, đường Thăng Long ven sông.</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Hòa Vang & Tuyến Đường Dài Toàn Quốc:</strong> Hội An, Huế, Quảng Ngãi, Quy Nhơn, Nha Trang, Đà Lạt, Hà Nội, TP.HCM.</span>
              </div>
            </div>

            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid var(--navy); padding:16px; border-radius:8px; margin-top:20px;">
              <strong style="color:var(--navy);">Lưu ý quy hoạch hành chính (Sau ngày 01/07/2025):</strong>
              <p style="margin:4px 0 0; font-size:0.9rem; color:#475569;">
                Thành phố Đà Nẵng đã triển khai sắp xếp, tinh gọn các đơn vị hành chính cấp phường, xã theo Nghị quyết của Quốc hội. Đội ngũ tài xế Như Ý Driver phục vụ toàn bộ các khu dân cư theo cả địa danh quen thuộc và đơn vị hành chính sau sáp nhập. <em>(Lưu ý: Hoàng Sa là đặc khu hải đảo tiền tiêu, không thuộc phạm vi đón trả khách đường bộ thông thường).</em>
              </p>
            </div>
          </div>
          <div class="split-media-wrap">
            {picture_tag("12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.png", "Bản đồ khu vực phục vụ lái xe hộ Như Ý Driver Đà Nẵng", "split-media-img", 1536, 1024, lazy=False)}
          </div>
        </div>

        <!-- DISTRICT CARDS GRID -->
        <div style="margin-top:60px;">
          <h2 style="font-size:1.6rem; font-weight:800; color:var(--navy); margin-bottom:24px; text-align:center;">7 ĐỊA BÀN PHỤC VỤ TRỌNG ĐIỂM TẠI ĐÀ NẴNG</h2>
          <div class="services-grid">
            <a href="/khu-vuc/hai-chau/" class="service-card" aria-label="Lái Xe Hộ Quận Hải Châu">
              <div class="service-card-img-wrap">
                {picture_tag("30_Lai_Xe_Ho_Hai_Chau_Da_Nang.png", "Lái xe hộ Hải Châu Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Hải Châu</h3>
                <p class="service-card-desc">Trung tâm tiệc tùng, phố đêm Bạch Đằng, đường 2/9, Nguyễn Văn Linh. Tài xế đến sau 10 - 15 phút.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/thanh-khe/" class="service-card" aria-label="Lái Xe Hộ Quận Thanh Khê">
              <div class="service-card-img-wrap">
                {picture_tag("12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.png", "Lái xe hộ Thanh Khê Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Thanh Khê</h3>
                <p class="service-card-desc">Phố biển Nguyễn Tất Thành, Điện Biên Phủ, Hà Huy Tập, Lê Độ. Phục vụ các quán nhậu bờ biển 24/7.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/son-tra/" class="service-card" aria-label="Lái Xe Hộ Quận Sơn Trà">
              <div class="service-card-img-wrap">
                {picture_tag("31_Lai_Xe_Ho_Son_Tra_Da_Nang.png", "Lái xe hộ Sơn Trà Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Sơn Trà</h3>
                <p class="service-card-desc">Khu ẩm thực biển Võ Nguyên Giáp, Hoàng Sa, Phạm Văn Đồng. Đưa khách và xe về khách sạn/nhà riêng an toàn.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/ngu-hanh-son/" class="service-card" aria-label="Lái Xe Hộ Quận Ngũ Hành Sơn">
              <div class="service-card-img-wrap">
                {picture_tag("15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png", "Lái xe hộ Ngũ Hành Sơn Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Ngũ Hành Sơn</h3>
                <p class="service-card-desc">Phố Tây An Thượng, tuyến resort Võ Nguyên Giáp &ndash; Trường Sa, Non Nước. Đón trả khách tận nơi chu đáo.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/lien-chieu/" class="service-card" aria-label="Lái Xe Hộ Quận Liên Chiểu">
              <div class="service-card-img-wrap">
                {picture_tag("04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png", "Lái xe hộ Liên Chiểu Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Liên Chiểu</h3>
                <p class="service-card-desc">Khu công nghiệp Hòa Khánh, trục Tôn Đức Thắng, Hoàng Thị Loan, đường vịnh Nguyễn Tất Thành.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/cam-le/" class="service-card" aria-label="Lái Xe Hộ Quận Cẩm Lệ">
              <div class="service-card-img-wrap">
                {picture_tag("02_Lai_Xe_Ho_Da_Nang_247.png", "Lái xe hộ Cẩm Lệ Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Quận Cẩm Lệ</h3>
                <p class="service-card-desc">Khu đô thị sinh thái Hòa Xuân, phố ẩm thực ven sông Thăng Long, trục CMT8, Nguyễn Hữu Thọ.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/hoa-vang/" class="service-card" aria-label="Lái Xe Hộ Huyện Hòa Vang">
              <div class="service-card-img-wrap">
                {picture_tag("14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.png", "Lái xe hộ Hòa Vang Đà Nẵng", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Lái Xe Hộ Huyện Hòa Vang</h3>
                <p class="service-card-desc">Cửa ngõ sinh thái, tuyến Bà Nà Suối Mơ, QL14B, các khu du lịch Suối Hoa, Yên Retreat, Lái Thiêu.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Từ 150.000đ</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>
          </div>
        </div>

        <!-- LONG DISTANCE SECTION -->
        <div style="margin-top:60px;">
          <h2 style="font-size:1.6rem; font-weight:800; color:var(--navy); margin-bottom:24px; text-align:center;">TUYẾN ĐƯỜNG DÀI &amp; LIÊN TỈNH TIÊU BIỂU</h2>
          <div class="services-grid">
            <a href="/khu-vuc/da-nang-di-hoi-an/" class="service-card" aria-label="Tài Xế Đà Nẵng Đi Hội An">
              <div class="service-card-img-wrap">
                {picture_tag("28_Thue_Tai_Xe_Da_Nang_Di_Hoi_An.png", "Thuê tài xế Đà Nẵng đi Hội An", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Tài Xế Đà Nẵng Đi Hội An</h3>
                <p class="service-card-desc">Tuyến đường di sản 30km. Lái xe riêng phục vụ ăn tối phố cổ Hội An và đưa về Đà Nẵng an toàn xuyên đêm.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Giá trọn gói</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/da-nang-di-hue/" class="service-card" aria-label="Tài Xế Đà Nẵng Đi Huế">
              <div class="service-card-img-wrap">
                {picture_tag("29_Thue_Tai_Xe_Da_Nang_Di_Hue.png", "Thuê tài xế Đà Nẵng đi Huế", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Tài Xế Đà Nẵng Đi Huế</h3>
                <p class="service-card-desc">Cung đường 100km qua Đèo Hải Vân hoặc hầm Hải Vân. Tài xế kinh nghiệm đường đèo, an toàn tuyệt đối.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Giá trọn gói</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>

            <a href="/khu-vuc/da-nang-di-quang-ngai/" class="service-card" aria-label="Tài Xế Đà Nẵng Đi Quảng Ngãi">
              <div class="service-card-img-wrap">
                {picture_tag("08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.png", "Thuê tài xế Đà Nẵng đi Quảng Ngãi", "service-card-img", 1536, 1024)}
              </div>
              <div class="service-card-content">
                <h3 class="service-card-title">Tài Xế Đà Nẵng Đi Quảng Ngãi</h3>
                <p class="service-card-desc">Tuyến cao tốc 140km êm ái. Phục vụ KKT Dung Quất, TP. Quảng Ngãi, Cảng Sa Kỳ và liên tỉnh miền Trung.</p>
                <div class="service-card-footer">
                  <span class="service-price-tag">Giá trọn gói</span>
                  <span class="service-more-link">Xem chi tiết &rarr;</span>
                </div>
              </div>
            </a>
          </div>

          <div style="text-align:center; margin-top:30px;">
            <a href="/dich-vu/thue-tai-xe-di-tinh/" class="btn-primary" style="padding:12px 28px;">&rarr; XEM TOÀN BỘ TUYẾN ĐƯỜNG DÀI TOÀN QUỐC (HÀ NỘI, NHA TRANG, ĐÀ LẠT, TP.HCM...)</a>
          </div>

          <div style="margin-top:40px;">
            {render_related_topics([
              ("Bảng giá lái xe hộ ô tô 150K", "/bang-gia/"),
              ("Lái xe hộ ô tô Đà Nẵng", "/dich-vu/lai-xe-ho-o-to/"),
              ("Lái xe hộ xe máy từ 110K", "/dich-vu/lai-xe-ho-xe-may/"),
              ("Bạn uống tôi lái 24/7", "/dich-vu/ban-uong-toi-lai/"),
              ("Thuê tài xế đi Hội An", "/khu-vuc/da-nang-di-hoi-an/"),
              ("Thuê tài xế đi Huế", "/khu-vuc/da-nang-di-hue/"),
              ("Thuê tài xế theo giờ", "/dich-vu/thue-tai-xe-theo-gio/"),
              ("Tổng đài liên hệ 0985 666 044", "/lien-he/")
            ], "Dịch vụ & Chủ đề liên quan")}
          </div>
        </div>
      </div>
    </section>
    '''

    title = "Khu Vực Phục Vụ Lái Xe Hộ Đà Nẵng | Có Mặt Nhanh 15-20 Phút"
    meta_desc = "Như Ý Driver phục vụ lái xe hộ tại tất cả 7 quận huyện Đà Nẵng: Hải Châu, Sơn Trà, Thanh Khê, Ngũ Hành Sơn, Liên Chiểu, Cẩm Lệ, Hòa Vang và đường dài toàn quốc. Gọi 0985 666 044."
    h1 = "KHU VỰC PHỤC VỤ LÁI XE HỘ KHẮP ĐÀ NẴNG 24/7"

    html = render_page_shell("/khu-vuc/", title, meta_desc, h1, body, og_image="/assets/images/12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.webp", schemas=[breadcrumb_schema])
    write_html("khu-vuc/index.html", html)

def build_contact():
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/lien-he/", "title": "Liên Hệ"}
    ])

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">LIÊN HỆ NHƯ Ý DRIVER – TỔNG ĐÀI LÁI XE HỘ ĐÀ NẴNG 24/7</h1>
        <p class="page-hero-desc">
          Cần tài xế lái xe hộ đưa về nhà ngay lập tức? Gọi hotline <a href="{HOTLINE_TEL}" aria-label="Gọi hotline Như Ý Driver 0985 666 044"><strong>{HOTLINE}</strong></a> hoặc nhắn <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" aria-label="Nhắn Zalo Như Ý Driver 0985 666 044"><strong>Zalo {HOTLINE}</strong></a> để tài xế có mặt sau 15–20 phút.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge">Kết Nối Trực Tiếp</span>
            <h2 class="split-title">THÔNG TIN TỔNG ĐÀI ĐẶT TÀI XẾ</h2>
            <p class="split-desc">
              Như Ý Driver hoạt động liên tục 24 giờ mỗi ngày, 7 ngày trong tuần, kể cả ngày nghỉ cuối tuần và các dịp lễ tết. Đội ngũ điều phối luôn sẵn sàng hỗ trợ bạn.
            </p>
            
            <div style="display:flex; flex-direction:column; gap:16px; margin:24px 0;">
              <div style="display:flex; align-items:center; gap:14px; background:var(--bg-gray); padding:16px; border-radius:var(--radius-md); border-left:4px solid var(--red);">
                <div style="width:40px; height:40px; border-radius:var(--radius-full); background:var(--red); color:#fff; display:flex; align-items:center; justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                </div>
                <div>
                  <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Hotline khẩn cấp 24/7</div>
                  <a href="{HOTLINE_TEL}" style="font-size:1.35rem; font-weight:900; color:var(--red);" aria-label="Gọi hotline khẩn cấp Như Ý Driver 0985 666 044">{HOTLINE}</a>
                </div>
              </div>

              <div style="display:flex; align-items:center; gap:14px; background:var(--bg-gray); padding:16px; border-radius:var(--radius-md); border-left:4px solid #0068FF;">
                <div style="width:40px; height:40px; border-radius:var(--radius-full); background:#0068FF; color:#fff; display:flex; align-items:center; justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.38 5.07L2.1 21.9l4.98-1.25C8.5 21.49 10.19 22 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2z"/></svg>
                </div>
                <div>
                  <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Zalo điều phối tài xế</div>
                  <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" style="font-size:1.2rem; font-weight:800; color:#0068FF;" aria-label="Nhắn Zalo điều phối tài xế 0985 666 044">0985 666 044 (Như Ý Driver)</a>
                </div>
              </div>

              <div style="display:flex; align-items:center; gap:14px; background:var(--bg-gray); padding:16px; border-radius:var(--radius-md); border-left:4px solid var(--navy);">
                <div style="width:40px; height:40px; border-radius:var(--radius-full); background:var(--navy); color:#fff; display:flex; align-items:center; justify-content:center;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </div>
                <div>
                  <div style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Email hỗ trợ & Hợp đồng</div>
                  <a href="mailto:{EMAIL}" style="font-size:0.92rem; font-weight:700; color:var(--navy); word-break:break-all;">{EMAIL}</a>
                </div>
              </div>
            </div>

            <!-- QR code card -->
            <div style="display:flex; align-items:center; gap:16px; background:var(--gold-bg); border:1px solid var(--gold); padding:18px; border-radius:var(--radius-md);">
              <img src="/assets/images/qr zalo.webp" alt="Mã QR Zalo Đặt Xe 0985 666 044" width="90" height="90" loading="lazy" decoding="async" style="width:90px; height:90px; border-radius:var(--radius-sm); background:#fff; padding:3px;">
              <div>
                <h3 style="font-size:1.05rem; font-weight:800; color:#78350f; margin-bottom:4px;">QUÉT MÃ ZALO ĐẶT XE</h3>
                <p style="font-size:0.875rem; color:#92400e; line-height:1.5;">
                  Mở ứng dụng Zalo trên điện thoại, quét mã QR để nhắn vị trí đón ngay lập tức với điều phối viên.
                </p>
              </div>
            </div>
          </div>

          <div class="split-media-wrap">
            {picture_tag("13_Lien_He_Nhu_Y_Driver.png", "Cần tài xế lái xe thay liên hệ Như Ý Driver 0985 666 044", "split-media-img", 1536, 1024, lazy=False)}
          </div>
        </div>

        <div style="margin-top:40px;">
          {render_related_topics([
            ("Bảng giá lái xe hộ ô tô 150K", "/bang-gia/"),
            ("Lái xe hộ ô tô Đà Nẵng", "/dich-vu/lai-xe-ho-o-to/"),
            ("Lái xe hộ xe máy từ 110K", "/dich-vu/lai-xe-ho-xe-may/"),
            ("Bạn uống tôi lái 24/7", "/dich-vu/ban-uong-toi-lai/"),
            ("Khu vực phục vụ Đà Nẵng", "/khu-vuc/"),
            ("Cẩm nang lái xe hộ 24/7", "/blog/"),
            ("Thuê tài xế đi tỉnh", "/dich-vu/thue-tai-xe-di-tinh/"),
            ("Về trang chủ", "/")
          ], "Dịch vụ & Tra cứu nhanh")}
        </div>
      </div>
    </section>
    '''

    title = "Liên Hệ Đặt Tài Xế Lái Xe Hộ Đà Nẵng 24/7 | Như Ý Driver"
    meta_desc = "Cần tài xế lái xe hộ tại Đà Nẵng? Liên hệ hotline 0985 666 044 hoặc Zalo 0985 666 044. Phục vụ 24/7 khắp các quận Đà Nẵng, có mặt sau 15-20 phút."
    h1 = "LIÊN HỆ NHƯ Ý DRIVER – TỔNG ĐÀI LÁI XE HỘ ĐÀ NẴNG 24/7"

    html = render_page_shell("/lien-he/", title, meta_desc, h1, body, og_image="/assets/images/13_Lien_He_Nhu_Y_Driver.webp", schemas=[breadcrumb_schema])
    write_html("lien-he/index.html", html)

def build_404():
    body = f'''
    <section class="section" style="padding:80px 0;">
      <div class="container error-page-wrap">
        <div class="error-code">404</div>
        <h1 class="error-title">KHÔNG TÌM THẤY TRANG YÊU CẦU</h1>
        <p class="error-desc">
          Trang bạn đang tìm kiếm có thể đã được thay đổi địa chỉ hoặc không tồn tại. Nếu bạn đang cần tài xế lái xe hộ khẩn cấp tại Đà Nẵng, hãy gọi ngay hotline bên dưới.
        </p>
        <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
          <a href="/" class="btn-primary" style="background:var(--navy);">VỀ TRANG CHỦ</a>
          <a href="{HOTLINE_TEL}" class="btn-primary" aria-label="Gọi hotline Như Ý Driver 0985 666 044">GỌI HOTLINE {HOTLINE}</a>
        </div>
      </div>
    </section>
    '''
    title = "404 - Không Tìm Thấy Trang | Như Ý Driver Đà Nẵng"
    meta_desc = "Trang không tồn tại trên hệ thống Như Ý Driver. Vui lòng quay lại trang chủ hoặc gọi hotline 0985 666 044 để đặt tài xế lái xe hộ tại Đà Nẵng."
    h1 = "404 - KHÔNG TÌM THẤY TRANG"

    html = render_page_shell("/404.html", title, meta_desc, h1, body)
    write_html("404.html", html)

if __name__ == '__main__':
    build_about()
    build_pricing()
    build_locations_hub()
    build_contact()
    build_404()

