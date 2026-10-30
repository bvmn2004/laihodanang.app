import sys
from site_components import (
    BASE_URL, BRAND_NAME, HOTLINE, HOTLINE_TEL, ZALO_URL, picture_tag
)
from site_builder_core import render_page_shell, write_html

sys.stdout.reconfigure(encoding='utf-8')

def build_home():
    faq_data = [
        {
            "q": "Dịch vụ lái xe hộ Như Ý Driver hoạt động như thế nào?",
            "a": "Tài xế của Như Ý Driver sẽ đến tận điểm hẹn (nhà hàng, quán bar, tiệc cưới...), nhận chìa khóa và trực tiếp lái chính phương tiện (ô tô hoặc xe máy) của bạn, đưa cả bạn và xe về nhà an toàn tuyệt đối. Bạn không cần phải để xe lại qua đêm."
        },
        {
            "q": "Mức giá từ 150K áp dụng cho loại xe nào?",
            "a": "Mức 150.000đ là giá cước cố định áp dụng cho dịch vụ lái hộ xe ô tô nội thành Đà Nẵng với cự ly từ 0 đến 5 km. Đối với xe máy, cước chỉ từ 110.000đ cho cự ly 0 - 5 km."
        },
        {
            "q": "Sau bao lâu tài xế sẽ có mặt sau khi đặt?",
            "a": "Đội ngũ tài xế Như Ý Driver túc trực tại khắp các quận trung tâm Đà Nẵng (Hải Châu, Sơn Trà, Thanh Khê, Ngũ Hành Sơn, Cẩm Lệ, Liên Chiểu), cam kết có mặt dự kiến chỉ từ 15 đến 20 phút sau cuộc gọi hoặc tin nhắn Zalo."
        },
        {
            "q": "Có phụ phí gì phát sinh thêm ngoài bảng giá không?",
            "a": "Bảng giá Như Ý Driver hoàn toàn minh bạch. Chuyến đi ban ngày tính theo km cố định. Sau 23h00 đêm áp dụng phụ phí giờ khuya +50.000đ/chuyến. Khách hàng luôn được báo trước chi phí chính xác trước khi khởi hành."
        },
        {
            "q": "Tài xế có thể lái được các dòng xe ô tô cao cấp không?",
            "a": "100% tài xế Như Ý Driver có bằng lái từ B2 trở lên, trên 5 năm kinh nghiệm thực chiến, thông thạo tất cả các dòng xe: số sàn (MT), số tự động (AT), SUV, bán tải và các thương hiệu xe sang như Mercedes, BMW, Audi, Lexus, Porsche..."
        }
    ]

    faq_items_html = []
    faq_schema_items = []
    for i, item in enumerate(faq_data):
        faq_schema_items.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        })
        is_first = (i == 0)
        faq_items_html.append(f'''
        <div class="faq-item {'active' if is_first else ''}">
          <button type="button" class="faq-question-btn" aria-expanded="{'true' if is_first else 'false'}">
            <span>{item["q"]}</span>
            <svg class="faq-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-answer">
            <p>{item["a"]}</p>
          </div>
        </div>
        ''')

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items
    }

    body = f'''
    <!-- HERO SECTION -->
    <section class="hero-section">
      <div class="container hero-grid">
        <div class="hero-content">
          <div class="hero-badge-pill">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
            <span>TÀI XẾ CHUYÊN NGHIỆP – PHỤC VỤ 24/7 TẠI ĐÀ NẴNG</span>
          </div>
          
          <h1 class="hero-title">
            LÁI XE HỘ ĐÀ NẴNG – <span class="highlight-gold">GIÁ CHỈ TỪ</span> <span class="highlight-red">150K</span>
          </h1>

          <p class="hero-desc">
            Đã uống rượu bia? Như Ý Driver nhận lái chính xe của bạn, đưa cả người và xe về nhà an toàn. Tài xế đồng phục đỏ lịch sự, giàu kinh nghiệm, có mặt sau 15–20 phút tại Đà Nẵng.
          </p>

          <div class="hero-cta-group">
            <a href="{HOTLINE_TEL}" class="btn-primary" aria-label="Gọi ngay hotline Như Ý Driver 0985 666 044" title="Gọi ngay cho tài xế Như Ý Driver">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
              GỌI NGAY {HOTLINE}
            </a>
            <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" aria-label="Đặt tài xế qua Zalo 0985 666 044" title="Đặt tài xế qua Zalo">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.38 5.07L2.1 21.9l4.98-1.25C8.5 21.49 10.19 22 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2z"/></svg>
              ĐẶT TÀI XẾ QUA ZALO
            </a>
          </div>

          <div class="hero-features-list">
            <div class="hero-feature-item">
              <svg class="hero-feature-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.54 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg>
              <span>Ô tô nội thành từ 150K (0-5km)</span>
            </div>
            <div class="hero-feature-item">
              <svg class="hero-feature-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm4.2 14.2L11 13V7h1.5v5.2l4.5 2.7-.8 1.3z"/></svg>
              <span>Có mặt dự kiến 15–20 phút</span>
            </div>
            <div class="hero-feature-item">
              <svg class="hero-feature-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
              <span>Phục vụ cả Ô Tô & Xe Máy</span>
            </div>
          </div>
        </div>

        <div class="hero-media-wrap">
          {picture_tag("02_Lai_Xe_Ho_Da_Nang_24_7.png", "Dịch vụ lái xe hộ Đà Nẵng 24/7 Như Ý Driver giá từ 150K", "hero-media-img", 1536, 1024, lazy=False)}
          <div class="hero-floating-badge">
            <div>
              <div class="badge-text-primary">Tài xế Như Ý Driver – Đồng phục đỏ</div>
              <div class="badge-text-sub">An toàn – Tận tâm – Chuyên nghiệp</div>
            </div>
            <a href="{HOTLINE_TEL}" class="btn-primary" style="padding: 8px 16px; font-size: 0.85rem;" aria-label="Gọi ngay hotline 0985 666 044">GỌI NGAY</a>
          </div>
        </div>
      </div>
    </section>

    <!-- TRUST BADGES SECTION -->
    <section class="section section-gray" style="padding: 35px 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; text-align: center;">
          <div style="background:#fff; padding:20px; border-radius:var(--radius-md); border:1px solid var(--border);">
            <div style="color:var(--red); font-size:1.8rem; font-weight:900; margin-bottom:4px;">15 - 20 PHÚT</div>
            <div style="font-weight:700; color:var(--navy); font-size:1rem;">Có Mặt Nhanh Chóng</div>
            <div style="font-size:0.85rem; color:var(--text-muted);">Tài xế túc trực mọi quận huyện Đà Nẵng</div>
          </div>
          <div style="background:#fff; padding:20px; border-radius:var(--radius-md); border:1px solid var(--border);">
            <div style="color:var(--gold); font-size:1.8rem; font-weight:900; margin-bottom:4px;">TỪ 150.000đ</div>
            <div style="font-weight:700; color:var(--navy); font-size:1rem;">Giá Cước Rõ Ràng</div>
            <div style="font-size:0.85rem; color:var(--text-muted);">Ô tô từ 150K, xe máy từ 110K không phụ phí ẩn</div>
          </div>
          <div style="background:#fff; padding:20px; border-radius:var(--radius-md); border:1px solid var(--border);">
            <div style="color:var(--navy); font-size:1.8rem; font-weight:900; margin-bottom:4px;">24/7 XUYÊN ĐÊM</div>
            <div style="font-weight:700; color:var(--navy); font-size:1rem;">Phục Vụ Không Giới Hạn</div>
            <div style="font-size:0.85rem; color:var(--text-muted);">Mưa gió, ngày lễ tết, gọi là có tài xế</div>
          </div>
          <div style="background:#fff; padding:20px; border-radius:var(--radius-md); border:1px solid var(--border);">
            <div style="color:#16a34a; font-size:1.8rem; font-weight:900; margin-bottom:4px;">100% AN TOÀN</div>
            <div style="font-weight:700; color:var(--navy); font-size:1rem;">Đưa Người & Xe Về Nhà</div>
            <div style="font-size:0.85rem; color:var(--text-muted);">Bảo đảm an toàn thân thể và tài sản của bạn</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION PRICING & FARE CALCULATOR -->
    <section class="section" id="bang-gia">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Minh Bạch & Công Khai</span>
          <h2 class="section-title">BẢNG GIÁ DỊCH VỤ LÁI XE HỘ ĐÀ NẴNG 2026</h2>
          <p class="section-lead">
            Bảng giá cước chính thức của Như Ý Driver áp dụng trên toàn địa bàn TP. Đà Nẵng. Không phí ẩn, thông báo giá trước khi khởi hành.
          </p>
        </div>

        <div class="pricing-grid">
          <!-- Card Ô TÔ -->
          <div class="pricing-card featured">
            <span class="featured-ribbon">Phổ biến nhất</span>
            <div class="pricing-card-header">
              <div class="pricing-card-title">Lái Xe Hộ Ô Tô</div>
              <div class="pricing-card-sub">Lái chính xe ô tô của bạn (4 - 7 chỗ, SUV, bán tải, xe sang)</div>
              <div class="pricing-start-at">
                <span class="price-big">150.000đ</span>
                <span class="price-unit">/ 0 - 5 km đầu</span>
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
                    <td>Đi 3 km = 150.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>5 – 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">200.000đ</td>
                    <td>Đi 8 km = 200.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>Trên 10 – 30 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">200k + 15k/km</td>
                    <td>Đi 15 km = 275.000đ</td>
                  </tr>
                  <tr>
                    <td><strong>Trên 30 km</strong></td>
                    <td style="color:var(--navy); font-weight:700;">Thỏa thuận</td>
                    <td>Tuyến đi tỉnh giá trọn gói</td>
                  </tr>
                </tbody>
              </table>

              <div class="pricing-notes-box">
                <strong>Phụ phí giờ khuya (sau 23:00):</strong> +50.000đ/chuyến (áp dụng cho chuyến đi từ 23:00 đến 05:59 sáng hôm sau).
              </div>
            </div>
            <div class="pricing-card-footer">
              <a href="{HOTLINE_TEL}" class="btn-primary" style="justify-content:center;" aria-label="Gọi đặt tài xế ô tô 0985 666 044">GỌI ĐẶT TÀI XẾ Ô TÔ</a>
              <a href="/dich-vu/lai-xe-ho-o-to/" class="service-more-link" style="justify-content:center;">Xem chi tiết dịch vụ ô tô &rarr;</a>
            </div>
          </div>

          <!-- Card XE MÁY -->
          <div class="pricing-card">
            <div class="pricing-card-header">
              <div class="pricing-card-title">Lái Xe Hộ Xe Máy</div>
              <div class="pricing-card-sub">Lái chính xe máy đưa bạn và xe về tận nhà</div>
              <div class="pricing-start-at">
                <span class="price-big">110.000đ</span>
                <span class="price-unit">/ 0 - 5 km đầu</span>
              </div>
            </div>
            <div class="pricing-card-body">
              <table class="pricing-table-clean">
                <thead>
                  <tr>
                    <th>Quãng đường</th>
                    <th>Đơn giá</th>
                    <th>Ghi chú</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>0 – 5 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">110.000đ</td>
                    <td>Cố định nội thành</td>
                  </tr>
                  <tr>
                    <td><strong>5 – 7 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">130.000đ</td>
                    <td>Cố định theo cự ly</td>
                  </tr>
                  <tr>
                    <td><strong>7 – 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">170.000đ</td>
                    <td>Cố định theo cự ly</td>
                  </tr>
                  <tr>
                    <td><strong>Qua 10 km</strong></td>
                    <td style="color:var(--red); font-weight:700;">+10.000đ/km</td>
                    <td>Cộng thêm mỗi km</td>
                  </tr>
                </tbody>
              </table>

              <div class="pricing-notes-box">
                <strong>Qua 23h:</strong> +50.000đ giờ khuya. Đưa khách và xe về tận cổng, không lo gửi xe qua đêm bị trầy xước mất cắp.
              </div>
            </div>
            <div class="pricing-card-footer">
              <a href="{HOTLINE_TEL}" class="btn-primary" style="justify-content:center; background-color:var(--navy);" aria-label="Gọi đặt tài xế xe máy 0985 666 044">GỌI ĐẶT TÀI XẾ XE MÁY</a>
              <a href="/dich-vu/lai-xe-ho-xe-may/" class="service-more-link" style="justify-content:center;">Xem chi tiết dịch vụ xe máy &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Interactive Fare Calculator -->
        <div class="fare-calc-box" id="fareCalculator">
          <h3 class="calc-title">TÍNH NHANH GIÁ CƯỚC CHUYẾN ĐI CỦA BẠN</h3>
          <p class="calc-subtitle">Chọn loại phương tiện, nhập số km dự kiến để ước tính chi phí minh bạch</p>
          
          <div class="calc-form-grid">
            <div class="calc-field">
              <label for="calcVehicle">Loại phương tiện:</label>
              <select id="calcVehicle">
                <option value="oto" selected>Ô tô (Giá từ 150K)</option>
                <option value="xemay">Xe máy (Giá từ 110K)</option>
              </select>
            </div>

            <div class="calc-field">
              <label for="calcDistance">Quãng đường dự kiến (km):</label>
              <input type="number" id="calcDistance" min="1" max="100" value="5" step="0.5">
              <div style="display:flex; gap:6px; margin-top:6px; flex-wrap:wrap;">
                <button type="button" class="calc-quick-km" data-km="3" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">3km</button>
                <button type="button" class="calc-quick-km" data-km="5" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">5km</button>
                <button type="button" class="calc-quick-km" data-km="8" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">8km</button>
                <button type="button" class="calc-quick-km" data-km="12" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">12km</button>
                <button type="button" class="calc-quick-km" data-km="15" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">15km</button>
                <button type="button" class="calc-quick-km" data-km="25" style="padding:3px 8px; font-size:0.75rem; border:1px solid #cbd5e1; background:#fff; border-radius:4px; cursor:pointer;">25km</button>
              </div>
            </div>
          </div>

          <div style="margin-bottom:20px;">
            <label style="display:inline-flex; align-items:center; gap:8px; cursor:pointer; font-size:0.95rem; font-weight:600; color:var(--navy);">
              <input type="checkbox" id="calcNightTime" style="width:18px; height:18px;">
              <span>Khung giờ đêm khuya sau 23:00 (+50.000đ)</span>
            </label>
          </div>

          <div class="calc-result-wrap">
            <div class="calc-result-label">Chi phí ước tính:</div>
            <div class="calc-result-price" id="calcResultPrice">150.000đ</div>
            <div class="calc-result-breakdown" id="calcResultBreakdown">Quãng đường 5 km (Khung 0 - 5 km cố định): 150.000đ</div>
            <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
              <a href="{HOTLINE_TEL}" class="btn-primary" style="padding:10px 22px; font-size:0.95rem;" aria-label="Gọi đặt xe ngay 0985 666 044">GỌI ĐẶT XE NGAY</a>
              <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" style="padding:10px 22px; font-size:0.95rem;" aria-label="Gửi địa chỉ qua Zalo 0985 666 044">GỬI ĐỊA CHỈ QUA ZALO</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION SERVICES -->
    <section class="section section-gray">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Dịch Vụ Chuyên Nghiệp</span>
          <h2 class="section-title">CÁC HÌNH THỨC LÁI XE HỘ PHỔ BIẾN</h2>
          <p class="section-lead">Đáp ứng mọi nhu cầu di chuyển của cá nhân, doanh nghiệp và du khách tại Đà Nẵng</p>
        </div>

        <div class="services-grid">
          <!-- S1: Ô tô -->
          <a href="/dich-vu/lai-xe-ho-o-to/" class="service-card" aria-label="Lái Xe Hộ Ô Tô Đà Nẵng">
            <div class="service-card-img-wrap">
              {picture_tag("04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png", "Dịch vụ lái hộ ô tô Đà Nẵng Như Ý Driver", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">Chủ lực</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Lái Xe Hộ Ô Tô Đà Nẵng</h3>
              <p class="service-card-desc">Tài xế lái chính xe ô tô của bạn đưa cả người và xe về an toàn. Thành thạo số sàn, tự động, xe sang gầm cao.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Từ 150.000đ</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>

          <!-- S2: Xe máy -->
          <a href="/dich-vu/lai-xe-ho-xe-may/" class="service-card" aria-label="Lái Xe Hộ Xe Máy Đà Nẵng">
            <div class="service-card-img-wrap">
              {picture_tag("05_Dich_Vu_Lai_Ho_Xe_May_Da_Nang.png", "Dịch vụ lái hộ xe máy Đà Nẵng Như Ý Driver", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">Tiết kiệm</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Lái Xe Hộ Xe Máy Đà Nẵng</h3>
              <p class="service-card-desc">Đã uống rượu bia có xe máy? Tài xế đưa bạn và xe về tận ngõ nhà, không lo gửi xe qua đêm trầy xước mất cắp.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Từ 110.000đ</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>

          <!-- S3: Bạn uống tôi lái -->
          <a href="/dich-vu/ban-uong-toi-lai/" class="service-card" aria-label="Dịch Vụ Bạn Uống Tôi Lái">
            <div class="service-card-img-wrap">
              {picture_tag("03_Lai_Xe_Ho_Sau_Khi_Uong_Ruou_Bia.png", "Bạn uống tôi lái Đà Nẵng an toàn sau tiệc", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">24/7 Xuyên đêm</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Dịch Vụ Bạn Uống Tôi Lái</h3>
              <p class="service-card-desc">Giải pháp an tâm tuyệt đối sau các bữa tiệc rượu, liên hoan, tất niên. Bảo vệ an toàn tính mạng và túi tiền trước mức phạt nồng độ cồn.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Có mặt sau 15p</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>

          <!-- S4: Theo giờ -->
          <a href="/dich-vu/thue-tai-xe-theo-gio/" class="service-card" aria-label="Thuê Tài Xế Theo Giờ">
            <div class="service-card-img-wrap">
              {picture_tag("06_Thue_Tai_Xe_Theo_Gio_Da_Nang.png", "Thuê tài xế theo giờ tại Đà Nẵng", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">Linh hoạt</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Thuê Tài Xế Theo Giờ</h3>
              <p class="service-card-desc">Linh hoạt theo lịch trình riêng. Phù hợp cho khách cần di chuyển nhiều điểm trong ngày, đi tiếp khách hoặc shopping nội đô.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Báo giá theo giờ</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>

          <!-- S5: Theo ngày -->
          <a href="/dich-vu/thue-tai-xe-theo-ngay/" class="service-card" aria-label="Thuê Tài Xế Theo Ngày">
            <div class="service-card-img-wrap">
              {picture_tag("07_Thue_Tai_Xe_Theo_Ngay_Da_Nang.png", "Thuê tài xế theo ngày tại Đà Nẵng", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">Trọn gói</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Thuê Tài Xế Theo Ngày</h3>
              <p class="service-card-desc">Dành cho chuyến công tác, city tour gia đình, dự sự kiện dài ngày. Tài xế đồng phục chỉn chu, phục vụ nhiệt tình chu đáo.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Lịch trình tự do</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>

          <!-- S6: Đi tỉnh -->
          <a href="/dich-vu/thue-tai-xe-di-tinh/" class="service-card" aria-label="Thuê Tài Xế Lái Xe Đi Tỉnh">
            <div class="service-card-img-wrap">
              {picture_tag("08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.png", "Thuê tài xế lái xe đi tỉnh từ Đà Nẵng", "service-card-img", 1536, 1024)}
              <span class="service-card-badge">Đường dài</span>
            </div>
            <div class="service-card-content">
              <h3 class="service-card-title">Thuê Tài Xế Lái Xe Đi Tỉnh</h3>
              <p class="service-card-desc">Xuất phát từ Đà Nẵng đi Hội An, Huế, Tam Kỳ, Quảng Ngãi... Tay lái đường trường kinh nghiệm, qua đèo hầm an toàn tuyệt đối.</p>
              <div class="service-card-footer">
                <span class="service-price-tag">Giá trọn gói</span>
                <span class="service-more-link">Chi tiết &rarr;</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 5-STEP PROCESS -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Nhanh Chóng & Đơn Giản</span>
          <h2 class="section-title">QUY TRÌNH 5 BƯỚC ĐẶT TÀI XẾ NHƯ Ý DRIVER</h2>
          <p class="section-lead">Không cần tải app phức tạp. Chỉ cần 1 cuộc gọi hoặc tin nhắn Zalo, tài xế sẽ có mặt ngay</p>
        </div>

        <div class="process-grid">
          <div class="process-step-card">
            <div class="step-number">01</div>
            <h3 class="step-title">Liên Hệ</h3>
            <p class="step-desc">Gọi hotline <a href="{HOTLINE_TEL}" aria-label="Gọi hotline Như Ý Driver 0985 666 044"><strong>{HOTLINE}</strong></a> hoặc nhắn tin qua <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" aria-label="Nhắn Zalo Như Ý Driver 0985 666 044">Zalo</a>.</p>
          </div>
          <div class="process-step-card">
            <div class="step-number">02</div>
            <h3 class="step-title">Gửi Vị Trí</h3>
            <p class="step-desc">Cung cấp điểm đón hiện tại và địa chỉ điểm đến mà bạn muốn về.</p>
          </div>
          <div class="process-step-card">
            <div class="step-number">03</div>
            <h3 class="step-title">Nhận Báo Giá</h3>
            <p class="step-desc">Tổng đài viên báo giá cước minh bạch chuẩn xác theo bảng giá cố định.</p>
          </div>
          <div class="process-step-card">
            <div class="step-number">04</div>
            <h3 class="step-title">Tài Xế Đến Đón</h3>
            <p class="step-desc">Tài xế mặc đồng phục đỏ đến sau 15–20 phút, nhận bàn giao chìa khóa xe.</p>
          </div>
          <div class="process-step-card">
            <div class="step-number">05</div>
            <h3 class="step-title">Về Nhà An Toàn</h3>
            <p class="step-desc">Tài xế lái chính xe đưa bạn về tận nơi an toàn và bàn giao lại tài sản.</p>
          </div>
        </div>

        <div style="margin-top: 40px; text-align: center;">
          {picture_tag("11_Quy_Trinh_Dat_Tai_Xe_Nhu_Y_Driver.png", "Quy trình đặt tài xế Như Ý Driver 5 bước phục vụ 24/7", "split-media-img", 1536, 1024)}
        </div>
      </div>
    </section>

    <!-- SECTION DRIVER TEAM (REAL PHOTOS) -->
    <section class="section section-navy">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge" style="color:var(--gold);">Đội Ngũ Thật – Hình Ảnh Thật</span>
            <h2 class="split-title" style="color:#ffffff;">ĐỘI NGŨ TÀI XẾ CHUYÊN NGHIỆP TẠI ĐÀ NẴNG</h2>
            <p class="split-desc" style="color:#cbd5e1;">
              Không dùng ảnh minh họa trừu tượng hay ảnh người nước ngoài. Như Ý Driver tự hào sở hữu đội ngũ tài xế bản địa Đà Nẵng mặc đồng phục vest đỏ chỉn chu, có hồ sơ tư pháp rõ ràng, tay lái vững vàng từ 5 năm trở lên.
            </p>
            <div class="split-checklist">
              <div class="split-check-item" style="color:#ffffff;">
                <svg class="split-check-icon" style="color:var(--gold);" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>Đồng phục nhận diện rõ ràng:</strong> Áo gile đỏ in logo Như Ý Driver và số Hotline <a href="{HOTLINE_TEL}" style="color:var(--gold); font-weight:700;" aria-label="Gọi hotline Như Ý Driver 0985 666 044">{HOTLINE}</a> trên ngực áo.</span>
              </div>
              <div class="split-check-item" style="color:#ffffff;">
                <svg class="split-check-icon" style="color:var(--gold);" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>Thành thạo mọi dòng xe:</strong> Thành thục từ số sàn, số tự động đến các dòng xe sang Mercedes, BMW, Audi, Porsche, Lexus...</span>
              </div>
              <div class="split-check-item" style="color:#ffffff;">
                <svg class="split-check-icon" style="color:var(--gold);" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span><strong>Tác phong lịch sự, bảo mật:</strong> Tôn trọng không gian riêng tư của khách hàng, trung thực và tận tụy.</span>
              </div>
            </div>
            <div>
              <a href="/gioi-thieu/" class="btn-outline-gold">Tìm hiểu thêm về đội ngũ &rarr;</a>
            </div>
          </div>

          <div class="split-media-wrap">
            {picture_tag("15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png", "Đội ngũ tài xế Như Ý Driver đồng phục đỏ chụp trước Cầu Rồng Đà Nẵng", "split-media-img", 1536, 1024)}
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION SERVICE AREA -->
    <section class="section section-gray">
      <div class="container">
        <div class="split-section reverse">
          <div class="split-content">
            <span class="split-badge">Mạng Lưới Phục Vụ</span>
            <h2 class="split-title">KHU VỰC PHỤC VỤ LÁI XE HỘ TẠI ĐÀ NẴNG</h2>
            <p class="split-desc">
              Tài xế Như Ý Driver túc trực 24/7 tại tất cả các cung đường ẩm thực, tụ điểm quán nhậu, nhà hàng, khách sạn lớn trên khắp các quận huyện Đà Nẵng:
            </p>
            <div class="split-checklist">
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Quận Hải Châu &amp; Thanh Khê:</strong> Bạch Đằng, Như Nguyệt, 2/9, Nguyễn Văn Linh, Điện Biên Phủ, biển Nguyễn Tất Thành (<a href="/khu-vuc/hai-chau/" style="color:var(--red); font-weight:700;">Hải Châu</a> | <a href="/khu-vuc/thanh-khe/" style="color:var(--red); font-weight:700;">Thanh Khê</a>)</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Quận Sơn Trà &amp; Ngũ Hành Sơn:</strong> Võ Nguyên Giáp, Phạm Văn Đồng, Hồ Nghinh, phố Tây An Thượng, Trường Sa (<a href="/khu-vuc/son-tra/" style="color:var(--red); font-weight:700;">Sơn Trà</a> | <a href="/khu-vuc/ngu-hanh-son/" style="color:var(--red); font-weight:700;">Ngũ Hành Sơn</a>)</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Liên Chiểu, Cẩm Lệ &amp; Hòa Vang:</strong> KCN Hòa Khánh, KĐT Hòa Xuân, sông Thăng Long, Bà Nà Suối Mơ (<a href="/khu-vuc/lien-chieu/" style="color:var(--red); font-weight:700;">Liên Chiểu</a> | <a href="/khu-vuc/cam-le/" style="color:var(--red); font-weight:700;">Cẩm Lệ</a> | <a href="/khu-vuc/hoa-vang/" style="color:var(--red); font-weight:700;">Hòa Vang</a>)</span>
              </div>
              <div class="split-check-item">
                <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                <span><strong>Tuyến đường dài toàn quốc:</strong> <a href="/khu-vuc/da-nang-di-hoi-an/" style="color:var(--navy); font-weight:600;">Hội An</a>, <a href="/khu-vuc/da-nang-di-hue/" style="color:var(--navy); font-weight:600;">Huế</a>, <a href="/khu-vuc/da-nang-di-quang-ngai/" style="color:var(--navy); font-weight:600;">Quảng Ngãi</a>, <a href="/dich-vu/thue-tai-xe-di-tinh/" style="color:var(--red); font-weight:700;">Nha Trang, Đà Lạt, Hà Nội, TP.HCM &rarr;</a></span>
              </div>
            </div>
            <div>
              <a href="/khu-vuc/" class="btn-primary" style="background-color:var(--navy);">XEM BẢN ĐỒ KHU VỰC PHỤC VỤ</a>
            </div>
          </div>

          <div class="split-media-wrap">
            {picture_tag("12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.png", "Bản đồ khu vực phục vụ lái xe hộ toàn thành phố Đà Nẵng Như Ý Driver", "split-media-img", 1536, 1024)}
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION FAQ -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Giải Đáp Thắc Mắc</span>
          <h2 class="section-title">CÂU HỎI THƯỜNG GẶP (FAQ)</h2>
          <p class="section-lead">Những thắc mắc phổ biến của khách hàng khi gọi tài xế lái xe hộ tại Đà Nẵng</p>
        </div>

        <div class="faq-wrap">
          {''.join(faq_items_html)}
        </div>
      </div>
    </section>

    <!-- SECTION BLOG HIGHLIGHTS -->
    <section class="section section-gray">
      <div class="container">
        <div class="section-header">
          <span class="section-subtitle">Cẩm Nang Lái Xe An Toàn</span>
          <h2 class="section-title">KIẾN THỨC & KINH NGHIỆM HỮU ÍCH</h2>
          <p class="section-lead">Thông tin quy định pháp luật nồng độ cồn và mẹo sử dụng dịch vụ thông minh</p>
        </div>

        <div class="blog-grid">
          <a href="/blog/lai-xe-ho-la-gi/" class="blog-card" aria-label="Lái Xe Hộ Là Gì? Quy Trình Hoạt Động & Khi Nào Nên Dùng?">
            <div class="blog-card-media">
              {picture_tag("17_Lai_Xe_Ho_La_Gi.png", "Lái xe hộ là gì", "blog-card-img", 1536, 1024)}
            </div>
            <div class="blog-card-body">
              <div class="blog-card-meta">
                <span class="blog-badge">Cẩm nang</span>
                <span>Kiến thức cơ bản</span>
              </div>
              <h3 class="blog-card-title">Lái Xe Hộ Là Gì? Quy Trình Hoạt Động & Khi Nào Nên Dùng?</h3>
              <p class="blog-card-desc">Tìm hiểu chi tiết về mô hình dịch vụ lái xe hộ, lợi ích vượt trội so với việc gửi xe qua đêm tại quán nhậu.</p>
              <span class="blog-read-more">Đọc tiếp &rarr;</span>
            </div>
          </a>

          <a href="/blog/lai-xe-ho-va-taxi-nen-chon-gi/" class="blog-card" aria-label="Lái Xe Hộ Hay Taxi: Lựa Chọn Nào Phù Hợp Với Bạn?">
            <div class="blog-card-media">
              {picture_tag("10_Lai_Xe_Ho_Va_Taxi_Nen_Chon_Dich_Vu_Nao.png", "Lái xe hộ và taxi nên chọn dịch vụ nào", "blog-card-img", 1536, 1024)}
            </div>
            <div class="blog-card-body">
              <div class="blog-card-meta">
                <span class="blog-badge">So sánh</span>
                <span>Kinh nghiệm</span>
              </div>
              <h3 class="blog-card-title">Lái Xe Hộ Hay Taxi: Lựa Chọn Nào Phù Hợp Với Bạn?</h3>
              <p class="blog-card-desc">Phân tích chi phí, sự tiện lợi khi so sánh giữa việc gọi taxi và thuê tài xế lái chính xe của mình về nhà.</p>
              <span class="blog-read-more">Đọc tiếp &rarr;</span>
            </div>
          </a>

          <a href="/blog/khi-nao-nen-goi-tai-xe-lai-ho/" class="blog-card" aria-label="7 Trường Hợp Bạn Nhất Định Nên Gọi Tài Xế Lái Hộ">
            <div class="blog-card-media">
              {picture_tag("18_Truong_Hop_Nen_Goi_Tai_Xe_Lai_Ho.png", "7 trường hợp nên gọi tài xế lái hộ", "blog-card-img", 1536, 1024)}
            </div>
            <div class="blog-card-body">
              <div class="blog-card-meta">
                <span class="blog-badge">Lời khuyên</span>
                <span>An toàn giao thông</span>
              </div>
              <h3 class="blog-card-title">7 Trường Hợp Bạn Nhất Định Nên Gọi Tài Xế Lái Hộ</h3>
              <p class="blog-card-desc">Đừng mạo hiểm tự cầm lái khi say rượu, buồn ngủ hay mệt mỏi. Hãy bảo vệ bạn và gia đình kịp thời.</p>
              <span class="blog-read-more">Đọc tiếp &rarr;</span>
            </div>
          </a>
        </div>

        <div style="text-align:center; margin-top:35px;">
          <a href="/blog/" class="btn-outline-gold" style="color:var(--navy); border-color:var(--navy);">Xem tất cả bài viết cẩm nang &rarr;</a>
        </div>
      </div>
    </section>

    <!-- FINAL CALL TO ACTION SECTION -->
    <section class="section" style="background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy) 100%); color:#ffffff; text-align:center;">
      <div class="container" style="max-width: 800px;">
        <h2 style="font-size:2.2rem; font-weight:900; margin-bottom:16px;">BẠN ĐANG CẦN TÀI XẾ LÁI XE HỘ NGAY BÂY GIỜ?</h2>
        <p style="font-size:1.1rem; color:#cbd5e1; margin-bottom:30px; line-height:1.6;">
          Đừng ngần ngại liên hệ! Tài xế Như Ý Driver luôn túc trực 24/7 và sẵn sàng xuất phát ngay sau khi nhận thông tin điểm đón.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="{HOTLINE_TEL}" class="btn-primary" style="font-size:1.15rem; padding:16px 36px;" aria-label="Gọi ngay hotline Như Ý Driver 0985 666 044">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
            GỌI NGAY: {HOTLINE}
          </a>
          <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" style="font-size:1.15rem; padding:16px 36px;" aria-label="Nhắn tin qua Zalo 0985 666 044">
            NHẮN TIN QUA ZALO
          </a>
        </div>
      </div>
    </section>
    '''

    title = "Lái Xe Hộ Đà Nẵng Giá Chỉ Từ 150K | Như Ý Driver Phục Vụ 24/7"
    meta_desc = "Dịch vụ lái xe hộ ô tô & xe máy tại Đà Nẵng 24/7. Tài xế lái chính xe của bạn đưa cả người và xe về an toàn. Giá ô tô từ 150K, có mặt sau 15-20 phút. Gọi ngay 0985 666 044."
    h1 = "LÁI XE HỘ ĐÀ NẴNG – GIÁ CHỈ TỪ 150K"

    html = render_page_shell("/", title, meta_desc, h1, body, og_image="/assets/images/02_Lai_Xe_Ho_Da_Nang_24_7.webp", schemas=[faq_schema])
    write_html("index.html", html)

if __name__ == '__main__':
    build_home()

