import os
import sys
from site_components import (
    BASE_URL, BRAND_NAME, HOTLINE, HOTLINE_TEL, ZALO_URL, picture_tag, render_breadcrumbs, render_related_topics
)
from site_builder_core import render_page_shell, write_html

sys.stdout.reconfigure(encoding='utf-8')

SERVICES_DATA = [
    {
        "slug": "lai-xe-ho-o-to",
        "title": "Lái Xe Hộ Ô Tô Đà Nẵng Giá Chỉ Từ 150K | Có Mặt Sau 15 Phút",
        "h1": "DỊCH VỤ LÁI XE HỘ Ô TÔ TẠI ĐÀ NẴNG – TÀI XẾ 24/7",
        "meta_desc": "Dịch vụ tài xế lái xe hộ ô tô tại Đà Nẵng sau tiệc rượu bia, đi tiếp khách hoặc mệt mỏi. Giá chỉ từ 150K. Tài xế kinh nghiệm mọi dòng xe, có mặt sau 15 phút. Gọi 0985 666 044.",
        "image": "04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png",
        "og_image": "/assets/images/04_Dich_Vu_Lai_Ho_O_To_Da_Nang.webp",
        "lead": "Giải pháp an toàn và văn minh hàng đầu dành cho chủ xe ô tô tại Đà Nẵng. Tài xế chuyên nghiệp của Như Ý Driver sẽ điều khiển chính chiếc xe của bạn đưa bạn và xe về nhà an toàn.",
        "price_summary": "150.000đ (0 - 5 km) | 200.000đ (5 - 10 km) | +15.000đ/km tiếp theo",
        "features": [
            "Lái thuần thục mọi dòng xe: Số sàn (MT), số tự động (AT), Sedan, SUV gầm cao, xe bán tải và xe sang châu Âu (Mercedes, BMW, Audi, Lexus, Porsche...).",
            "Có mặt siêu tốc: Chỉ từ 15 – 20 phút tại khắp các quận Hải Châu, Sơn Trà, Thanh Khê, Cẩm Lệ, Ngũ Hành Sơn, Liên Chiểu.",
            "Tài xế hồ sơ trong sạch, lái xe điềm đạm, giữ khoảng cách an toàn, không phóng nhanh vượt ẩu.",
            "Bảo hiểm trách nhiệm chuyến đi, cam kết chịu 100% trách nhiệm nếu xảy ra sự cố do lỗi tài xế."
        ],
        "detailed_content": """
        <h2>Tại sao chủ xe ô tô tại Đà Nẵng luôn chọn Như Ý Driver?</h2>
        <p>Chiếc ô tô không chỉ là tài sản giá trị mà còn là phương tiện gắn bó hàng ngày của bạn và gia đình. Việc giao chìa khóa cho một tài xế xa lạ luôn cần sự tin cậy cao độ. Tại <strong>Như Ý Driver</strong>, chúng tôi tuyển chọn và đào tạo đội ngũ tài xế với tiêu chuẩn khắt khe nhất Đà Nẵng:</p>
        <ul>
          <li><strong>Kinh nghiệm thực chiến dày dặn:</strong> 100% tài xế có bằng lái B2, C trở lên với ít nhất 5 năm cầm lái liên tục, am hiểu sâu sắc cơ chế hoạt động của các hệ thống trợ lực lái, phanh điện tử và hộp số phức tạp.</li>
          <li><strong>Tác phong lịch sự, chu đáo:</strong> Đồng phục áo đỏ chỉnh tề, thái độ nhã nhặn, tôn trọng không gian riêng tư của khách hàng, sẵn sàng hỗ trợ mở cửa, xếp hành lý.</li>
          <li><strong>Bảo vệ xe cẩn thận:</strong> Kiểm tra kỹ tình trạng thân vỏ, số km, đồ đạc trên xe trước khi khởi hành và bàn giao đầy đủ khi xe về gara nhà bạn.</li>
        </ul>

        <h2>Quy trình đặt tài xế lái hộ ô tô nhanh chóng</h2>
        <ol>
          <li><strong>Liên hệ tổng đài:</strong> Gọi ngay Hotline <a href="tel:0985666044" aria-label="Gọi Như Ý Driver 0985 666 044"><strong>0985 666 044</strong></a> hoặc gửi vị trí qua <a href="https://zalo.me/0985666044" target="_blank" rel="noopener nofollow">Zalo 0985 666 044</a>.</li>
          <li><strong>Báo giá minh bạch:</strong> Nhân viên xác nhận loại xe, điểm đón, điểm đến và báo giá cước chính xác theo khung giá niêm yết (từ 150K).</li>
          <li><strong>Tài xế tiếp cận:</strong> Tài xế gần nhất di chuyển đến vị trí quán nhậu, nhà hàng hoặc khách sạn của bạn trong vòng 15 – 20 phút.</li>
          <li><strong>Hành trình an toàn:</strong> Bạn thoải mái nghỉ ngơi, chợp mắt ở hàng ghế sau trong khi tài xế đưa bạn và xế yêu về tận cổng nhà an toàn.</li>
        </ol>
        """
    },
    {
        "slug": "lai-xe-ho-xe-may",
        "title": "Lái Xe Hộ Xe Máy Đà Nẵng Giá Chỉ Từ 110K | Nhanh Chóng 24/7",
        "h1": "DỊCH VỤ LÁI XE HỘ XE MÁY TẠI ĐÀ NẴNG – AN TOÀN, TIẾT KIỆM",
        "meta_desc": "Dịch vụ chở bạn và xe máy về nhà an toàn sau tiệc rượu bia tại Đà Nẵng. Giá chỉ từ 110K. Tài xế đến tận quán nhậu đón, không lo bỏ xe lại. Gọi 0985 666 044.",
        "image": "05_Dich_Vu_Lai_Ho_Xe_May_Da_Nang.png",
        "og_image": "/assets/images/05_Dich_Vu_Lai_Ho_Xe_May_Da_Nang.webp",
        "lead": "Uống bia rượu nhưng đi xe máy? Đừng lo lắng chuyện gửi xe lại qua đêm hay nguy cơ bị phạt nồng độ cồn. Tài xế Như Ý Driver sẽ chở bạn và chính chiếc xe máy của bạn về tận nhà.",
        "price_summary": "110.000đ (0 - 5 km) | 130.000đ (5 - 7 km) | 170.000đ (7 - 10 km)",
        "features": [
            "Không lo mất mát tài sản hay hư hỏng xe khi phải gửi lại quán nhậu qua đêm.",
            "Phương án di chuyển linh hoạt: Tài xế đi xe công nghệ hoặc có xe hỗ trợ đi cùng để chở cả người và xe về.",
            "Cước phí siêu tiết kiệm: Chỉ từ 110K cho chặng đường dưới 5km nội đô Đà Nẵng.",
            "Phục vụ xuyên đêm 24/7 kể cả ngày lễ, mưa gió hay lúc tàn tiệc rạng sáng."
        ],
        "detailed_content": """
        <h2>Giải pháp hoàn hảo: Về nhà an toàn, xe máy có mặt tại nhà sáng hôm sau</h2>
        <p>Nhiều người đi dự tiệc bằng xe máy thường rơi vào thế khó xử: nếu bắt taxi về thì phải bỏ xe lại quán, lo sợ mất cắp, trầy xước hoặc sáng hôm sau không có phương tiện đi làm; nếu tự lái xe về thì nguy cơ tai nạn giao thông và mức phạt nồng độ cồn xe máy lên tới 8 triệu đồng cùng tước bằng lái 24 tháng.</p>
        <p><strong>Dịch vụ lái xe hộ xe máy của Như Ý Driver</strong> sinh ra để giải quyết triệt để nỗi băn khoăn này. Chỉ với 1 cuộc gọi, tài xế của chúng tôi sẽ đến tận bàn tiệc, nhận chìa khóa và điều khiển chiếc xe máy chở bạn về nhà an toàn tuyệt đối.</p>

        <h2>Bảng cước lái hộ xe máy rõ ràng</h2>
        <ul>
          <li><strong>0 – 5 km:</strong> 110.000đ (phù hợp hầu hết các lộ trình di chuyển nội quận Hải Châu, Thanh Khê, Sơn Trà).</li>
          <li><strong>5 – 7 km:</strong> 130.000đ.</li>
          <li><strong>7 – 10 km:</strong> 170.000đ.</li>
          <li><strong>Trên 10 km:</strong> Cộng thêm 10.000đ cho mỗi km tiếp theo.</li>
          <li><strong>Sau 23h đêm:</strong> Phụ phí 50.000đ/chuyến để hỗ trợ tài xế trực đêm tận tâm.</li>
        </ul>
        """
    },
    {
        "slug": "ban-uong-toi-lai",
        "title": "Bạn Uống Tôi Lái Đà Nẵng 24/7 | Tài Xế Đến Sau 15 Phút Giá Từ 150K",
        "h1": "DỊCH VỤ BẠN UỐNG TÔI LÁI ĐÀ NẴNG – VĂN MINH & AN TOÀN",
        "meta_desc": "Dịch vụ bạn uống tôi lái tại Đà Nẵng. Uống rượu bia không lái xe, đã có tài xế Như Ý Driver đưa bạn và xe về tận nhà an toàn 24/7. Gọi hotline 0985 666 044.",
        "image": "03_Lai_Xe_Ho_Sau_Khi_Uong_Ruou_Bia.png",
        "og_image": "/assets/images/03_Lai_Xe_Ho_Sau_Khi_Uong_Ruou_Bia.webp",
        "lead": "Chiến dịch 'Bạn uống – Tôi lái' lan tỏa lối sống văn minh, có trách nhiệm với gia đình và xã hội. Thưởng thức trọn vẹn niềm vui bên bàn tiệc, việc lái xe an toàn hãy để Như Ý Driver lo.",
        "price_summary": "Ô tô từ 150K | Xe máy từ 110K | Có mặt sau 15–20 phút",
        "features": [
            "Bảo vệ 100% bằng lái và điểm số giấy phép lái xe theo luật giao thông mới nhất.",
            "Tránh xa nguy cơ tai nạn, bảo vệ an toàn tính mạng cho chính bạn và người đi đường.",
            "Thoải mái nâng ly giao lưu cùng đối tác, sếp và bạn bè mà không canh cánh nỗi lo đường về.",
            "Đội ngũ tài xế túc trực sẵn tại các tụ điểm ẩm thực lớn nhất Đà Nẵng."
        ],
        "detailed_content": """
        <h2>'Đã uống rượu bia – Tuyệt đối không lái xe'</h2>
        <p>Tại một thành phố du lịch và giao thương năng động như Đà Nẵng, những bữa tiệc gặp mặt đối tác, liên hoan công ty hay sum họp gia đình là điều không thể thiếu. Tuy nhiên, sau vài ly bia hay chén rượu, khả năng phản xạ và xử lý tình huống của người lái xe giảm đi nghiêm trọng.</p>
        <p>Với tinh thần 'Bạn uống – Tôi lái', <strong>Như Ý Driver</strong> đóng vai trò là người bạn đồng hành tin cậy, sẵn sàng túc trực ngoài quán để cầm vô lăng đưa bạn và xế cưng vượt qua mọi cung đường về tới tổ ấm bình an.</p>
        """
    },
    {
        "slug": "lai-xe-ho-sau-tiec",
        "title": "Lái Xe Hộ Sau Tiệc Rượu Bia Tại Đà Nẵng | Đưa Người Say Về Nhà",
        "h1": "DỊCH VỤ LÁI XE HỘ SAU TIỆC RƯỢU BIA TẠI ĐÀ NẴNG",
        "meta_desc": "Dịch vụ đưa đón người say sau tiệc rượu bia tại Đà Nẵng. Tài xế chăm sóc chu đáo, đưa cả người và xe về gara an toàn, bàn giao chìa khóa tận tay người nhà. Hotline: 0985 666 044.",
        "image": "23_Di_Tiec_Bang_O_To_Da_Nang.png",
        "og_image": "/assets/images/23_Di_Tiec_Bang_O_To_Da_Nang.webp",
        "lead": "Chuyên phục vụ các trường hợp khách hàng quá chén, mệt mỏi sau tiệc cưới, sinh nhật, tất niên, tân gia tại Đà Nẵng. Tài xế chu đáo, điềm đạm, hỗ trợ dìu khách và đưa xe vào gara an toàn.",
        "price_summary": "Giá minh bạch từ 150K (ô tô) & 110K (xe máy) | Trực 24/7",
        "features": [
            "Hỗ trợ người say tận tình: Dìu khách lên xe, chuẩn bị túi nôn, nước lọc và khăn lạnh khi cần.",
            "Bàn giao chìa khóa và tài sản tận tay người thân tại nhà, đảm bảo sự an tâm tuyệt đối.",
            "Lái xe cẩn thận, êm dịu, hạn chế tối đa cảm giác xóc nảy gây say xe cho người đang mệt.",
            "Không bao giờ phàn nàn, phục vụ với thái độ cảm thông và trách nhiệm nghề nghiệp cao nhất."
        ],
        "detailed_content": """
        <h2>Chăm sóc chu đáo khi bạn không còn đủ tỉnh táo</h2>
        <p>Trong nhiều cuộc vui tiếp khách quan trọng, việc uống quá chén là điều khó tránh khỏi. Khi cơ thể mệt mỏi, phản xạ chậm lại, việc cố gắng tự lái xe là cực kỳ nguy hiểm cho bản thân và cộng đồng.</p>
        <p>Khi gọi Như Ý Driver, bạn hoàn toàn có thể yên tâm ngả lưng ngủ một giấc trên xe. Bác tài của chúng tôi sẽ lái xe với tốc độ ổn định, êm ái nhất, đưa bạn về đến nhà, cất xe gọn gàng vào gara và bàn giao chìa khóa cho người thân trong gia đình.</p>
        """
    },
    {
        "slug": "thue-tai-xe-theo-gio",
        "title": "Thuê Tài Xế Theo Giờ Đà Nẵng Giá Tốt | Linh Hoạt Theo Lịch Trình",
        "h1": "DỊCH VỤ THUÊ TÀI XẾ THEO GIỜ TẠI ĐÀ NẴNG",
        "meta_desc": "Thuê tài xế lái xe theo giờ tại Đà Nẵng đưa đón tiếp khách, đi công việc, shopping, dự tiệc. Linh hoạt từ 1-4 giờ, giá trọn gói tiết kiệm. Đặt tài xế gọi 0985 666 044.",
        "image": "06_Thue_Tai_Xe_Theo_Gio_Da_Nang.png",
        "og_image": "/assets/images/06_Thue_Tai_Xe_Theo_Gio_Da_Nang.webp",
        "lead": "Giải pháp kinh tế và linh hoạt tối ưu dành cho khách hàng cần tài xế phục vụ theo từng khung giờ cụ thể trong ngày: đi gặp nhiều đối tác, đi mua sắm, đưa đón con cái hoặc dự hội thảo.",
        "price_summary": "Gói linh hoạt: 200.000đ (2 giờ đầu) | 80.000đ cho mỗi giờ tiếp theo",
        "features": [
            "Tự do sắp xếp lịch trình di chuyển đến nhiều điểm khác nhau trong khoảng thời gian đã thuê.",
            "Tài xế luôn túc trực bên xe, sẵn sàng mở cửa và xuất phát ngay khi bạn hoàn thành công việc.",
            "Không phải loay hoay tìm bãi đỗ xe hay canh cánh việc vi phạm dừng đỗ nơi phố cấm.",
            "Tác phong đúng giờ tuyệt đối, lịch thiệp và giữ bí mật thông tin công việc của khách hàng."
        ],
        "detailed_content": """
        <h2>Thuê tài xế theo giờ – Tối ưu chi phí cho ngày bận rộn</h2>
        <p>Nếu bạn có một buổi chiều cần đi tiếp 3 – 4 đối tác tại nhiều địa điểm khác nhau khắp Đà Nẵng, việc mỗi chặng gọi một chuyến xe vừa tốn kém thời gian chờ đợi vừa gây bất tiện. Thuê tài xế riêng theo giờ lái chính chiếc xe của bạn là giải pháp thông minh vượt trội.</p>
        <p>Tài xế Như Ý Driver sẽ đưa bạn đến từng điểm hẹn, đợi bạn làm việc và đưa bạn sang điểm tiếp theo đúng lộ trình, giúp công việc của bạn diễn ra suôn sẻ, chuyên nghiệp và đẳng cấp.</p>
        """
    },
    {
        "slug": "thue-tai-xe-theo-ngay",
        "title": "Thuê Tài Xế Theo Ngày Đà Nẵng | Du Lịch, Công Tác, Sự Kiện",
        "h1": "DỊCH VỤ THUÊ TÀI XẾ THEO NGÀY TẠI ĐÀ NẴNG",
        "meta_desc": "Thuê tài xế riêng theo ngày tại Đà Nẵng (gói 8h - 10h/ngày). Phục vụ du lịch Bà Nà, Hội An, Huế, tiếp khách công tác. Báo giá trọn gói minh bạch. Hotline: 0985 666 044.",
        "image": "07_Thue_Tai_Xe_Theo_Ngay_Da_Nang.png",
        "og_image": "/assets/images/07_Thue_Tai_Xe_Theo_Ngay_Da_Nang.webp",
        "lead": "Dịch vụ tài xế riêng trọn gói cả ngày dành cho các chuyến du lịch gia đình, đoàn công tác dài ngày hoặc các sự kiện quan trọng tại Đà Nẵng và các tỉnh lân cận.",
        "price_summary": "600.000đ – 800.000đ / ngày (8 - 10 tiếng) | Thỏa thuận phát sinh",
        "features": [
            "Phục vụ trọn gói 8 đến 10 tiếng mỗi ngày theo toàn quyền điều phối lộ trình của khách hàng.",
            "Thông thạo mọi điểm tham quan, danh lam thắng cảnh, quán ăn ngon đặc sản tại Đà Nẵng, Hội An, Huế.",
            "Tác phong đúng giờ tuyệt đối, trang phục gọn gàng, nhiệt tình hỗ trợ khuân vác hành lý.",
            "Hợp đồng và hóa đơn dịch vụ minh bạch cho các đơn vị doanh nghiệp."
        ],
        "detailed_content": """
        <h2>Trải nghiệm du lịch và công tác Đà Nẵng đẳng cấp với tài xế riêng</h2>
        <p>Bạn tự lái xe từ các tỉnh khác đến Đà Nẵng du lịch nhưng muốn nghỉ ngơi để ngắm cảnh, thưởng thức hải sản và bia mát lạnh? Hãy thuê tài xế theo ngày của Như Ý Driver.</p>
        <p>Bạn sẽ không phải lo lắng về việc tìm chỗ đậu xe, canh chừng biển cấm hay áp lực lái xe giữa phố đông giờ cao điểm. Mọi việc đã có tài xế giàu kinh nghiệm đảm nhiệm trọn vẹn.</p>
        """
    },
    {
        "slug": "thue-tai-xe-di-tinh",
        "title": "Thuê Tài Xế Lái Xe Đường Dài Đi Tỉnh Toàn Quốc Từ Đà Nẵng | Như Ý Driver",
        "h1": "DỊCH VỤ THUÊ TÀI XẾ LÁI XE ĐI TỈNH & ĐƯỜNG DÀI TOÀN QUỐC TỪ ĐÀ NẴNG",
        "meta_desc": "Dịch vụ thuê tài xế lái chính xe của khách đi tỉnh từ Đà Nẵng: Hội An, Huế, Quảng Ngãi, Quảng Trị, Quảng Bình, Hà Tĩnh, Nghệ An, Hà Nội, Quy Nhơn, Nha Trang, Đà Lạt, TP.HCM. Báo giá trọn gói minh bạch. Hotline 0985 666 044.",
        "image": "08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.png",
        "og_image": "/assets/images/08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.webp",
        "lead": "Chuyên cung cấp tài xế lái chính ô tô riêng của khách hàng đi các tỉnh thành trên toàn quốc xuất phát từ Đà Nẵng. Tay lái vững vàng, thông thuộc cao tốc Bắc – Nam, đường đèo dốc hiểm trở, phục vụ chuyến 1 chiều và khứ hồi nhiều ngày với quy chuẩn an toàn cao nhất.",
        "price_summary": "Báo giá trọn gói theo lộ trình & loại xe | Cam kết không phát sinh",
        "features": [
            "Tài xế lái chính xe của bạn: Cầm lái an toàn các dòng xe số sàn, số tự động, Sedan, SUV, Crossover, MPV 7 chỗ, Bán tải.",
            "Đón tận nơi tại Đà Nẵng, trả tận địa chỉ yêu cầu tại tất cả các tỉnh thành trên toàn quốc.",
            "Báo giá trọn gói trước chuyến đi: Minh bạch cước lái xe, chi phí lưu đêm, vé xe khách/tàu quay về cho tài xế.",
            "Cam kết an toàn tuyệt đối: Quy chuẩn nghỉ ngơi khoa học, phương án 2 tài xế cho chặng đường dài >500km."
        ],
        "detailed_content": """
        <h2>Giải pháp hoàn hảo: Thuê tài xế lái chính xe của bạn đi đường dài toàn quốc</h2>
        <p>Khác với việc thuê xe trọn gói (thuê cả xe lẫn người lái), dịch vụ của <strong>Như Ý Driver</strong> là cử tài xế chuyên nghiệp, giàu kinh nghiệm lái chính chiếc ô tô riêng của bạn (hoặc xe cơ quan, xe doanh nghiệp) để thực hiện chuyến đi liên tỉnh. Dịch vụ này cực kỳ phù hợp khi:</p>
        <ul>
          <li>Bạn muốn di chuyển liên tỉnh bằng chính chiếc xe quen thuộc, tiện nghi của gia đình nhưng không muốn chịu áp lực mệt mỏi, căng thẳng khi phải cầm vô lăng liên tục nhiều giờ.</li>
          <li>Bạn cần chuyển ô tô từ Đà Nẵng vào TP.HCM, ra Hà Nội, lên Tây Nguyên hoặc về quê mà không có thời gian tự lái xe đường dài.</li>
          <li>Bạn đi công tác, tiếp đối tác tại các tỉnh và cần tài xế lịch thiệp cầm lái để bạn tranh thủ xử lý công việc, nghỉ ngơi trên xe.</li>
          <li>Chuyến đi có sử dụng rượu bia trong các buổi tiệc chiêu đãi tại tỉnh bạn và bạn cần tài xế đưa về Đà Nẵng an toàn xuyên đêm.</li>
        </ul>

        <h2>Danh sách các tuyến đường dài tiêu biểu xuất phát từ Đà Nẵng</h2>
        <p>Như Ý Driver nhận phục vụ các chuyến đi từ Đà Nẵng đến tất cả các tỉnh thành trên cả nước. Dưới đây là các tuyến phổ biến được khách hàng đặt nhiều nhất:</p>

        <div style="overflow-x:auto; margin:24px 0;">
          <table style="width:100%; border-collapse:collapse; font-size:0.925rem;">
            <thead>
              <tr style="background:var(--navy); color:#fff; text-align:left;">
                <th style="padding:10px 14px; border:1px solid #cbd5e1;">Tuyến đường tiêu biểu</th>
                <th style="padding:10px 14px; border:1px solid #cbd5e1;">Cự ly</th>
                <th style="padding:10px 14px; border:1px solid #cbd5e1;">Thời gian dự kiến</th>
                <th style="padding:10px 14px; border:1px solid #cbd5e1;">Lộ trình & Tiêu chuẩn phục vụ</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Hội An (Quảng Nam)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~30 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~45 phút</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Tuyến biển Võ Nguyên Giáp &ndash; Lạc Long Quân hoặc ĐT607. Phục vụ ăn tối, dạo phố cổ, đón về trong đêm.</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Huế (Thừa Thiên Huế)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~100 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~2 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Qua Hầm Hải Vân hoặc ngắm cảnh Đèo Hải Vân &ndash; Lăng Cô. Phục vụ công tác, thăm thân, cưới hỏi trong ngày.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Quảng Ngãi</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~140 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~1h45 &ndash; 2h</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Chạy cao tốc Đà Nẵng &ndash; Quảng Ngãi êm ái. Phục vụ KKT Dung Quất, KCN VSIP, Cảng Sa Kỳ (đi Lý Sơn).</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Quảng Trị</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~170 &ndash; 230 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~3.5 &ndash; 4.5 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Cao tốc Cam Lộ &ndash; La Sơn, QL1A hoặc đường 9 đi Lao Bảo. Phục vụ công tác cửa khẩu, viếng nghĩa trang liệt sĩ.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Quảng Bình (Đồng Hới / Phong Nha)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~270 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~5 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Trục QL1A &amp; cao tốc Bắc Nam. Du lịch hang động Phong Nha &ndash; Kẻ Bàng, viếng Mộ Đại tướng, công tác.</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Hà Tĩnh</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~370 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~6.5 &ndash; 7.5 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Tuyến cao tốc và QL1A qua hầm Đèo Ngang. Về quê, công tác KKT Vũng Áng, đền Chợ Củi, Ngã ba Đồng Lộc.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Nghệ An (TP. Vinh / Cửa Lò)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~420 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~7.5 &ndash; 8.5 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Hành trình liên tỉnh Bắc Trung Bộ. Tài xế nghỉ dừng chân kỹ thuật giữa chặng đảm bảo an toàn tuyệt đối.</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Quy Nhơn (Bình Định)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~310 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~5.5 &ndash; 6 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Cao tốc ĐN &ndash; QN kết nối QL1A qua Sa Huỳnh. Phục vụ du lịch biển Kỳ Co &ndash; Eo Gió, công tác cảng Quy Nhơn.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Nha Trang (Khánh Hòa)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~520 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~9 &ndash; 10 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Hành trình >500km. Bố trí kíp 2 tài xế hoặc dừng nghỉ đêm chặng giữa theo yêu cầu của khách hàng.</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Đà Lạt (Lâm Đồng)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~650 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~11 &ndash; 12 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Cung đường vượt đèo Tây Nguyên (Đèo Khánh Lê / An Khê &ndash; Mang Yang). Tài xế dày dạn kinh nghiệm đèo dốc sương mù.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; Hà Nội (Thủ đô)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~760 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~13 &ndash; 15 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Tuyến đường dài xuyên Bắc. Bố trí 2 tài xế luân phiên hoặc nghỉ đêm chặng giữa, bàn giao xe tận nơi tại Hà Nội.</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Đà Nẵng &harr; TP. Hồ Chí Minh (Sài Gòn)</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~950 &ndash; 1.000 km</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">~18 &ndash; 20 giờ</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;">Hành trình xuyên Việt vào miền Nam. Đội ngũ 2 tài xế thay nhau cầm lái, bàn giao xe tận các quận TP.HCM.</td>
              </tr>
              <tr>
                <td style="padding:10px 14px; border:1px solid #cbd5e1; font-weight:700;">Các tỉnh thành khác toàn quốc</td>
                <td style="padding:10px 14px; border:1px solid #cbd5e1;" colspan="3">Kon Tum, Gia Lai, Đắk Lắk, Bình Thuận, Ninh Bình, Thanh Hóa, Hải Phòng... Báo giá theo yêu cầu cụ thể.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>Quy định dịch vụ, chính sách chi phí và tiêu chuẩn an toàn</h2>
        <p>Để đảm bảo quyền lợi tối đa cho khách hàng và sự an toàn của toàn bộ hành trình, Như Ý Driver công khai rõ ràng các điều khoản dịch vụ đường dài:</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin:20px 0;">
          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:0;">1. Tài xế lái chính xe của khách hàng</h3>
          <p style="color:#475569; font-size:0.95rem;">
            Khách hàng chuẩn bị sẵn phương tiện đã đủ điều kiện lưu hành (đăng kiểm còn hạn, bảo hiểm bắt buộc TNDS còn hiệu lực). Tài xế của Như Ý Driver chịu trách nhiệm điều khiển xe an toàn, chấp hành tuyệt đối luật giao thông đường bộ.
          </p>

          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:16px;">2. Đón tận nơi &ndash; Trả đúng điểm hẹn</h3>
          <p style="color:#475569; font-size:0.95rem;">
            Tài xế đến tận nhà riêng, cơ quan, khách sạn tại Đà Nẵng để nhận xe và đón bạn đúng giờ đã hẹn. Khi đến tỉnh đích, tài xế đưa bạn và xe đến đúng địa chỉ chính xác, hỗ trợ mang vác hành lý vào nhà.
          </p>

          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:16px;">3. Báo giá trọn gói minh bạch trước khi xuất phát</h3>
          <p style="color:#475569; font-size:0.95rem;">
            Hai bên thống nhất tổng chi phí dịch vụ trước khi xe lăn bánh thông qua tin nhắn Zalo hoặc hợp đồng dịch vụ. Cam kết tuyệt đối không phát sinh phụ phí vô lý trong suốt hành trình.
          </p>

          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:16px;">4. Phân biệt chuyến 1 chiều và chuyến khứ hồi</h3>
          <ul style="color:#475569; font-size:0.95rem; margin-bottom:0;">
            <li><strong>Chuyến 1 chiều (One-way):</strong> Tài xế đưa xe và bạn đến điểm đích tại tỉnh bạn, hoàn thành bàn giao xe. Khách hàng hỗ trợ chi phí vé tàu hỏa hoặc vé xe khách giường nằm để tài xế trở về lại Đà Nẵng (hoặc đã gộp trọn gói trong báo giá).</li>
            <li><strong>Chuyến khứ hồi (Round-trip):</strong> Tài xế phục vụ đưa đi và đưa về lại Đà Nẵng trong ngày hoặc nhiều ngày. Với chuyến nhiều ngày, khách hàng hỗ trợ nơi nghỉ và bữa ăn cho tài xế hoặc thanh toán phụ cấp lưu trú theo mức thỏa thuận (thông thường 300.000đ – 400.000đ/đêm).</li>
          </ul>

          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:16px;">5. Phí cầu đường BOT, cao tốc và bến bãi</h3>
          <p style="color:#475569; font-size:0.95rem;">
            Phí qua trạm thu phí BOT, cao tốc được thanh toán trực tiếp qua thẻ ETC (VETC hoặc ePass) gắn trên kính xe của khách hàng. Phí gửi xe bến bãi tại điểm đến do khách hàng thanh toán thực tế (hoặc thỏa thuận gộp vào báo giá trọn gói).
          </p>

          <h3 style="color:var(--navy); font-size:1.15rem; margin-top:16px;">6. Tiêu chuẩn nghỉ ngơi &amp; Chế độ an toàn cho chặng dài >500km</h3>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:0;">
            Theo quy định an toàn giao thông, người lái xe không được lái liên tục quá 4 giờ và không quá 10 giờ/ngày. Trên các chặng dài, tài xế sẽ dừng nghỉ kỹ thuật 15 – 20 phút sau mỗi 3 – 4 giờ di chuyển tại các trạm dừng chân cao tốc. Đối với các cung đường dài từ 500km trở lên (Đà Nẵng đi Hà Nội, TP.HCM, Nha Trang, Đà Lạt), chúng tôi bố trí <strong>kíp 2 tài xế luân phiên</strong> hoặc tư vấn lộ trình chia làm 2 chặng có nghỉ đêm nhằm đảm bảo 100% sự an toàn, tỉnh táo cho suốt hành trình.
          </p>
        </div>

        <h2>Quy trình 5 bước đặt tài xế đường dài tại Như Ý Driver</h2>
        <ol>
          <li><strong>Bước 1 &ndash; Tiếp nhận thông tin:</strong> Quý khách gọi Hotline <a href="tel:0985666044" aria-label="Gọi Như Ý Driver 0985 666 044"><strong>0985 666 044</strong></a> hoặc nhắn tin <a href="https://zalo.me/0985666044" target="_blank" rel="noopener nofollow">Zalo 0985 666 044</a> cung cấp lộ trình (Điểm đi, điểm đến, thời gian xuất phát, loại xe, chuyến 1 chiều hay khứ hồi).</li>
          <li><strong>Bước 2 &ndash; Khảo sát &amp; Báo giá trọn gói:</strong> Điều hành tính toán cự ly, thời gian, phương án vé về của tài xế và gửi báo giá trọn gói bằng văn bản qua Zalo.</li>
          <li><strong>Bước 3 &ndash; Điều phối tài xế phù hợp:</strong> Cử tài xế chuyên tuyến đường trường, có sức khỏe tốt và kinh nghiệm đúng dòng xe của quý khách.</li>
          <li><strong>Bước 4 &ndash; Khởi hành an toàn:</strong> Tài xế đến đúng giờ hẹn, cùng quý khách kiểm tra ngoại quan xe và bắt đầu chuyến hành trình an toàn, chu đáo.</li>
          <li><strong>Bước 5 &ndash; Nghiệm thu &amp; Thanh toán:</strong> Đến nơi đúng hẹn, hỗ trợ quý khách dỡ hành lý, bàn giao chìa khóa và hoàn tất thanh toán cước phí.</li>
        </ol>
        """
    },
    {
        "slug": "thue-tai-xe-dua-don-doi-tac",
        "title": "Thuê Tài Xế Đưa Đón Đối Tác Đà Nẵng | Chuyên Nghiệp, Bảo Mật",
        "h1": "THUÊ TÀI XẾ ĐƯA ĐÓN ĐỐI TÁC & KHÁCH VIP TẠI ĐÀ NẴNG",
        "meta_desc": "Dịch vụ tài xế lái xe riêng đưa đón đối tác, chuyên gia, lãnh đạo tại Đà Nẵng. Tác phong lịch thiệp, đón sân bay đúng giờ, bảo mật thông tin tối đa. Hotline: 0985 666 044.",
        "image": "26_Tai_Xe_Dua_Don_Doi_Tac.png",
        "og_image": "/assets/images/26_Tai_Xe_Dua_Don_Doi_Tac.webp",
        "lead": "Khẳng định sự chuyên nghiệp và uy tín của doanh nghiệp khi đón tiếp đối tác, chuyên gia, khách VIP tại Đà Nẵng. Tài xế chỉnh tề, lịch thiệp, thông thạo đường phố và nghi thức ngoại giao.",
        "price_summary": "Báo giá theo lịch trình đón sân bay & phục vụ sự kiện",
        "features": [
            "Đón sân bay quốc tế Đà Nẵng đúng giờ, cầm biển đón tên khách sang trọng và lịch sự.",
            "Tác phong chỉn chu: Áo sơ mi/đồng phục gọn gàng, thái độ hòa nhã, mở cửa xe và xếp hành lý chu đáo.",
            "Lái xe điềm tĩnh, êm ái, am hiểu các điểm đến khách sạn 5 sao, sân golf, nhà hàng VIP tại Đà Nẵng & Hội An.",
            "Cam kết bảo mật tuyệt đối mọi thông tin công việc, cuộc trò chuyện của khách hàng trên xe."
        ],
        "detailed_content": """
        <h2>Tạo ấn tượng chuyên nghiệp ngay từ điểm đón sân bay Đà Nẵng</h2>
        <p>Khi đón tiếp những đối tác kinh doanh quan trọng, việc cử một tài xế riêng chu đáo điều khiển chiếc xe sang trọng của doanh nghiệp ra sân bay đón khách là chi tiết đắt giá thể hiện sự hiếu khách và vị thế của công ty.</p>
        <p>Đội ngũ tài xế phục vụ VIP của Như Ý Driver được đào tạo bài bản về tác phong nghi thức: từ cách chào hỏi, mở cửa xe, điều chỉnh nhiệt độ điều hòa phù hợp cho đến sự kín đáo, giữ yên lặng tuyệt đối khi khách hàng đang đàm thoại công việc.</p>
        """
    },
    {
        "slug": "thue-tai-xe-tiec-cuoi-su-kien",
        "title": "Thuê Tài Xế Tiệc Cưới & Sự Kiện Đà Nẵng | Đúng Giờ, Lịch Lãm",
        "h1": "DỊCH VỤ TÀI XẾ LÁI XE TIỆC CƯỚI & SỰ KIỆN TẠI ĐÀ NẴNG",
        "meta_desc": "Thuê tài xế lái xe hoa rước dâu, xe đón họ hàng hai bên trong ngày cưới tại Đà Nẵng. Đúng giờ tuyệt đối, trang phục trang trọng, lái xe cẩn thận. Hotline: 0985 666 044.",
        "image": "27_Tai_Xe_Phu_Vu_Tiec_Cuoi_Su_Kien.png",
        "og_image": "/assets/images/27_Tai_Xe_Phu_Vu_Tiec_Cuoi_Su_Kien.webp",
        "lead": "Ngày trọng đại thêm trọn vẹn và an tâm với đội ngũ tài xế lái xe hoa, xe đưa đón họ hàng hai bên. Lái xe cẩn trọng, đúng giờ hoàng đạo và trang phục trang trọng, lịch lãm.",
        "price_summary": "Gói rước dâu & sự kiện: Báo giá trọn gói linh hoạt theo buổi",
        "features": [
            "Cam kết có mặt trước giờ hoàng đạo ít nhất 30 phút để chuẩn bị xe tươm tất.",
            "Trang phục trang trọng, thắt cà vạt lịch sự, tác phong vui tươi, hòa nhã trong ngày vui.",
            "Lái xe hoa giữ tốc độ ổn định, giữ khoảng cách đoàn xe rước dâu đẹp mắt và an toàn.",
            "Phục vụ chở cô dâu chú rể chụp ảnh ngoại cảnh tại các thắng cảnh đẹp của Đà Nẵng."
        ],
        "detailed_content": """
        <h2>An tâm trọn vẹn trong ngày vui trăm năm</h2>
        <p>Trong ngày cưới, gia đình và họ hàng hai bên luôn bận rộn với rất nhiều nghi lễ. Việc người thân trong nhà phải tự cầm lái xe hoa hay xe chở họ vừa gây mệt mỏi, vừa dễ gặp sự cố trễ giờ hoàng đạo do áp lực căng thẳng.</p>
        <p>Giao phó nhiệm vụ cầm lái cho tài xế chuyên nghiệp của Như Ý Driver giúp gia đình hai bên hoàn toàn thảnh thơi trò chuyện, tận hưởng trọn vẹn từng khoảnh khắc hạnh phúc của đôi uyên ương.</p>
        """
    },
    {
        "slug": "thue-tai-xe-giao-nhan-xe",
        "title": "Tài Xế Giao Nhận Xe Gara & Đăng Kiểm Đà Nẵng | Uy Tín, Tin Cậy",
        "h1": "DỊCH VỤ TÀI XẾ GIAO NHẬN XE GARA & ĐĂNG KIỂM TẠI ĐÀ NẴNG",
        "meta_desc": "Dịch vụ tài xế nhận xe tận nhà đưa đi bảo dưỡng gara, đi đăng kiểm, giao xe mới tại Đà Nẵng. Biên bản bàn giao rõ ràng, an tâm tuyệt đối. Hotline: 0985 666 044.",
        "image": "14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.png",
        "og_image": "/assets/images/14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.webp",
        "lead": "Tiết kiệm tối đa thời gian quý báu của bạn. Tài xế Như Ý Driver sẽ đến tận nhà hoặc cơ quan nhận xe, mang xe đi đăng kiểm, bảo dưỡng định kỳ tại hãng và giao lại tận tay bạn.",
        "price_summary": "Báo giá theo từng lượt giao nhận xe hoặc gói trọn gói đăng kiểm",
        "features": [
            "Lập biên bản bàn giao xe chi tiết: chụp ảnh 4 góc xe, ghi nhận số km ODO, lượng xăng và đồ đạc trên xe.",
            "Đưa xe đi đăng kiểm tại các trung tâm đăng kiểm Đà Nẵng (50-01S, 50-02S...), xếp hàng chờ thủ tục thay bạn.",
            "Đưa xe đến gara chính hãng (Toyota, Hyundai, Kia, Mazda, Ford, Mercedes...) bảo dưỡng đúng lịch.",
            "Hỗ trợ các thủ tục kiểm tra tại hãng bảo dưỡng xe nếu được ủy quyền."
        ],
        "detailed_content": """
        <h2>Giải pháp tiết kiệm thời gian cho người sở hữu xe bận rộn</h2>
        <p>Xe đến hạn bảo dưỡng định kỳ hoặc hạn đăng kiểm nhưng bạn quá bận rộn với công việc cơ quan? Bạn mua xe mới tại đại lý nhưng chưa tự tin cầm lái qua phố đông về nhà?</p>
        <p>Như Ý Driver sẽ cử tài xế chuyên nghiệp đến tận nơi nhận chìa khóa, thực hiện đúng các hạng mục bạn yêu cầu và bàn giao xe tận tay với sự minh bạch tuyệt đối.</p>
        """
    }
]

def build_services_hub():
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/dich-vu/", "title": "Dịch Vụ"}
    ])

    cards_html = []
    for s in SERVICES_DATA:
        card_title = s["h1"].split("–")[0].strip()
        cards_html.append(f'''
        <a href="/dich-vu/{s['slug']}/" class="service-card" aria-label="{card_title}">
          <div class="service-card-img-wrap">
            {picture_tag(s["image"], s["title"], "service-card-img", 1536, 1024)}
            <span class="service-card-badge">{s["price_summary"].split("|")[0].strip()}</span>
          </div>
          <div class="service-card-content">
            <h2 class="service-card-title">{card_title}</h2>
            <p class="service-card-desc">{s["lead"]}</p>
            <div class="service-card-footer">
              <span class="service-price-tag">{s["price_summary"].split("|")[0].strip()}</span>
              <span class="service-more-link">Chi tiết dịch vụ &rarr;</span>
            </div>
          </div>
        </a>
        ''')

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">HỆ THỐNG DỊCH VỤ LÁI XE HỘ CHUYÊN NGHIỆP TẠI ĐÀ NẴNG</h1>
        <p class="page-hero-desc">
          Như Ý Driver cung cấp đầy đủ các giải pháp tài xế lái xe theo yêu cầu: Lái hộ ô tô, xe máy, đưa người say về nhà, thuê theo giờ, theo ngày và đường dài đi tỉnh toàn quốc.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="services-grid">
          {''.join(cards_html)}
        </div>
      </div>
    </section>

    <!-- SECTION PRICING CTA -->
    <section class="section section-gray" style="text-align:center;">
      <div class="container" style="max-width:800px;">
        <h2 style="font-size:1.8rem; font-weight:800; color:var(--navy); margin-bottom:12px;">BẠN MUỐN BIẾT CHI PHÍ CỤ THỂ CHO CHUYẾN ĐI?</h2>
        <p style="color:var(--text-muted); font-size:1rem; margin-bottom:24px;">
          Tham khảo bảng giá chi tiết niêm yết công khai của chúng tôi hoặc sử dụng công cụ tính cước nhanh trực tuyến.
        </p>
        <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
          <a href="/bang-gia/" class="btn-primary" style="background:var(--navy);">XEM BẢNG GIÁ 2026</a>
          <a href="{HOTLINE_TEL}" class="btn-primary" aria-label="Gọi báo giá {HOTLINE}">GỌI BÁO GIÁ {HOTLINE}</a>
        </div>
      </div>
    </section>
    '''

    title = "Dịch Vụ Lái Xe Hộ Tại Đà Nẵng | Ô Tô, Xe Máy, Theo Giờ & Đi Tỉnh"
    meta_desc = "Tổng hợp các dịch vụ lái xe hộ của Như Ý Driver: lái hộ ô tô, xe máy, đưa người say về nhà, thuê tài xế theo giờ, theo ngày, đi tỉnh. Phục vụ 24/7. Hotline: 0985 666 044."
    h1 = "HỆ THỐNG DỊCH VỤ LÁI XE HỘ CHUYÊN NGHIỆP TẠI ĐÀ NẴNG"

    html = render_page_shell("/dich-vu/", title, meta_desc, h1, body, og_image="/assets/images/02_Lai_Xe_Ho_Da_Nang_24_7.webp", schemas=[breadcrumb_schema])
    write_html("dich-vu/index.html", html)

def build_single_service(s):
    crumbs, breadcrumb_schema = render_breadcrumbs([
        {"url": "/", "title": "Trang Chủ"},
        {"url": "/dich-vu/", "title": "Dịch Vụ"},
        {"url": f"/dich-vu/{s['slug']}/", "title": s["h1"].split("–")[0].strip()}
    ])

    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": s["h1"].split("–")[0].strip(),
        "provider": {
            "@type": "AutomotiveBusiness",
            "name": BRAND_NAME,
            "telephone": HOTLINE,
            "url": BASE_URL
        },
        "areaServed": {"@type": "AdministrativeArea", "name": "Đà Nẵng"},
        "description": s["meta_desc"],
        "offers": {
            "@type": "Offer",
            "priceCurrency": "VND",
            "price": "150000" if "150" in s["price_summary"] else "110000",
            "availability": "https://schema.org/InStock",
            "validFrom": "2026-01-01"
        }
    }

    features_html = "".join([f'''
    <div class="split-check-item">
      <svg class="split-check-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
      <span>{f}</span>
    </div>
    ''' for f in s["features"]])

    other_services = [other for other in SERVICES_DATA if other["slug"] != s["slug"]][:3]
    other_services_html = "".join([f'''
    <a href="/dich-vu/{osrv['slug']}/" class="service-card" aria-label="{osrv['title']}">
      <div class="service-card-img-wrap">
        {picture_tag(osrv["image"], osrv["title"], "service-card-img", 1536, 1024)}
        <span class="service-card-badge">{osrv["price_summary"].split("|")[0].strip()}</span>
      </div>
      <div class="service-card-content">
        <h3 class="service-card-title">{osrv["title"]}</h3>
        <p class="service-card-desc">{osrv["lead"]}</p>
        <div class="service-card-footer">
          <span class="service-price-tag">{osrv["price_summary"].split("|")[0].strip()}</span>
          <span class="service-more-link">Chi tiết &rarr;</span>
        </div>
      </div>
    </a>
    ''' for osrv in other_services])

    districts = [
        ("Quận Hải Châu", "/khu-vuc/hai-chau/"),
        ("Quận Thanh Khê", "/khu-vuc/thanh-khe/"),
        ("Quận Sơn Trà", "/khu-vuc/son-tra/"),
        ("Quận Ngũ Hành Sơn", "/khu-vuc/ngu-hanh-son/"),
        ("Quận Liên Chiểu", "/khu-vuc/lien-chieu/"),
        ("Quận Cẩm Lệ", "/khu-vuc/cam-le/"),
        ("Huyện Hòa Vang", "/khu-vuc/hoa-vang/"),
        ("Tài xế đi Hội An", "/khu-vuc/da-nang-di-hoi-an/"),
        ("Tài xế đi Huế", "/khu-vuc/da-nang-di-hue/"),
        ("Tài xế đi Quảng Ngãi", "/khu-vuc/da-nang-di-quang-ngai/")
    ]
    districts_topics = render_related_topics(districts, "Khu vực phục vụ trọng điểm")

    service_topics = [
        ("Bảng giá lái xe hộ ô tô 150K", "/bang-gia/"),
        ("Lái xe hộ xe máy từ 110K", "/dich-vu/lai-xe-ho-xe-may/"),
        ("Bạn uống tôi lái 24/7", "/dich-vu/ban-uong-toi-lai/"),
        ("Lái xe hộ sau tiệc rượu", "/dich-vu/lai-xe-ho-sau-tiec/"),
        ("Thuê tài xế theo giờ", "/dich-vu/thue-tai-xe-theo-gio/"),
        ("Cẩm nang khi nào nên gọi tài xế", "/blog/khi-nao-nen-goi-tai-xe-lai-ho/"),
        ("Quy trình đặt tài xế Như Ý Driver", "/blog/quy-trinh-dat-tai-xe-nhu-y-driver/"),
        ("Liên hệ hotline 0985 666 044", "/lien-he/")
    ]
    topics_html = render_related_topics(service_topics, "Chủ đề tìm kiếm liên quan")

    body = f'''
    <section class="page-hero">
      <div class="container">
        {crumbs}
        <h1 class="page-hero-title">{s["h1"]}</h1>
        <p class="page-hero-desc">{s["lead"]}</p>
        <div style="display:inline-flex; gap:12px; margin-top:10px; flex-wrap:wrap;">
          <a href="{HOTLINE_TEL}" class="btn-primary" style="padding:10px 22px;" aria-label="Gọi ngay hotline {HOTLINE}">GỌI NGAY: {HOTLINE}</a>
          <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" style="padding:10px 22px;" aria-label="Đặt xe qua Zalo {HOTLINE}">ĐẶT QUA ZALO</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split-section">
          <div class="split-content">
            <span class="split-badge">Ưu Điểm Nổi Bật</span>
            <h2 class="split-title">ĐẶC ĐIỂM DỊCH VỤ TẠI NHƯ Ý DRIVER</h2>
            <div class="split-checklist">
              {features_html}
            </div>
            <div style="background:var(--gold-bg); padding:16px; border-radius:var(--radius-md); border-left:4px solid var(--gold); margin-top:16px;">
              <strong style="color:#78350f;">Mức giá tham khảo:</strong>
              <div style="color:var(--red); font-size:1.2rem; font-weight:800; margin-top:4px;">{s["price_summary"]}</div>
            </div>
          </div>
          <div class="split-media-wrap">
            {picture_tag(s["image"], s["title"], "split-media-img", 1536, 1024, lazy=False)}
          </div>
        </div>

        <div class="post-content" style="margin-top:50px; max-width:850px;">
          {s["detailed_content"]}

          <div class="post-cta-banner">
            <h3 style="color:#fff; font-size:1.6rem; font-weight:800; margin-bottom:12px;">ĐẶT TÀI XẾ NHANH – CÓ MẶT SAU 15–20 PHÚT</h3>
            <p style="color:#cbd5e1; margin-bottom:20px;">Tài xế Như Ý Driver đồng phục đỏ sẵn sàng xuất phát đón bạn bất kỳ lúc nào.</p>
            <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
              <a href="{HOTLINE_TEL}" class="btn-primary" aria-label="Gọi ngay {HOTLINE}">GỌI NGAY {HOTLINE}</a>
              <a href="{ZALO_URL}" target="_blank" rel="noopener nofollow" class="btn-zalo" aria-label="Chat Zalo đặt xe ngay">CHAT ZALO ĐẶT XE</a>
              <a href="/bang-gia/" class="btn-outline-gold">XEM TOÀN BỘ BẢNG GIÁ</a>
            </div>
          </div>

          {topics_html}
          {districts_topics}
        </div>

        <div class="related-section-wrap" style="max-width:850px; margin-left:auto; margin-right:auto;">
          <h2 class="related-section-heading">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/></svg>
            <span>DỊCH VỤ LIÊN QUAN TẠI ĐÀ NẴNG</span>
          </h2>
          <div class="services-grid">
            {other_services_html}
          </div>
        </div>
      </div>
    </section>
    '''

    html = render_page_shell(f"/dich-vu/{s['slug']}/", s["title"], s["meta_desc"], s["h1"], body, og_image=s["og_image"], schemas=[breadcrumb_schema, service_schema])
    write_html(f"dich-vu/{s['slug']}/index.html", html)

def main():
    print("Generating services hub and all single service pages...")
    build_services_hub()
    for s in SERVICES_DATA:
        build_single_service(s)
        print(f"  ✓ Built /dich-vu/{s['slug']}/index.html")

if __name__ == '__main__':
    main()
