import os
import glob
import json
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]
src_dir = r"C:\Users\admin\OneDrive\Pictures\card\ảnh làm web"
dst_dir = str(PROJECT_ROOT / "assets" / "images")

os.makedirs(dst_dir, exist_ok=True)

image_descriptions = {
    "logo.png": {
        "alt": "Logo Lái Xe Hộ Như Ý Driver Đà Nẵng 24/7 Hotline 0985 666 044",
        "role": "Brand Logo",
        "target_pages": ["All pages (Header & Footer)"]
    },
    "qr zalo.jpg": {
        "alt": "Mã QR Zalo 0985 666 044 đặt tài xế lái xe hộ Như Ý Driver",
        "role": "Zalo QR Code Booking",
        "target_pages": ["/lien-he/", "Contact Modal", "Footer"]
    },
    "01_Bang_Gia_Lai_Xe_Ho_Da_Nang_2026.png": {
        "alt": "Bảng giá lái xe hộ Đà Nẵng 2026 Như Ý Driver ô tô từ 150K",
        "role": "Pricing Chart with Driver",
        "target_pages": ["/bang-gia/", "/"]
    },
    "01_Bang_Gia_Lai_Xe_Ho_Da_Nang_2026_No_Driver.png": {
        "alt": "Chi tiết bảng giá cước lái xe hộ nội thành Đà Nẵng 24/7 ô tô từ 150.000đ",
        "role": "Detailed Pricing Table Infographic",
        "target_pages": ["/bang-gia/"]
    },
    "02_Lai_Xe_Ho_Da_Nang_24_7.png": {
        "alt": "Dịch vụ lái xe hộ Đà Nẵng 24/7 gọi là có mặt sau 15-20 phút Như Ý Driver",
        "role": "Hero Banner / 24-7 Support",
        "target_pages": ["/", "/dich-vu/"]
    },
    "02_Lai_Xe_Ho_Da_Nang_247.png": {
        "alt": "Quy trình 3 bước lái xe hộ ô tô Đà Nẵng đặt nhanh đón đúng giờ",
        "role": "Car Process Banner",
        "target_pages": ["/dich-vu/lai-xe-ho-o-to/"]
    },
    "03_Lai_Xe_Ho_Sau_Khi_Uong_Ruou_Bia.png": {
        "alt": "Đã uống rượu bia hãy để tài xế lái xe hộ đưa bạn và xe về an toàn Đà Nẵng",
        "role": "After Party / Safe Driving Hero",
        "target_pages": ["/dich-vu/ban-uong-toi-lai/", "/dich-vu/lai-xe-ho-sau-tiec/"]
    },
    "04_Dich_Vu_Lai_Ho_O_To_Da_Nang.png": {
        "alt": "Dịch vụ lái hộ ô tô Đà Nẵng đặt nhanh đến đúng giờ báo giá rõ ràng",
        "role": "Car Service Hero",
        "target_pages": ["/dich-vu/lai-xe-ho-o-to/"]
    },
    "05_Dich_Vu_Lai_Ho_Xe_May_Da_Nang.png": {
        "alt": "Dịch vụ lái hộ xe máy Đà Nẵng đưa khách và xe về tận nhà an toàn",
        "role": "Motorbike Service Hero",
        "target_pages": ["/dich-vu/lai-xe-ho-xe-may/"]
    },
    "06_Thue_Tai_Xe_Theo_Gio_Da_Nang.png": {
        "alt": "Thuê tài xế theo giờ tại Đà Nẵng linh hoạt theo lịch trình riêng",
        "role": "Hourly Driver Hero",
        "target_pages": ["/dich-vu/thue-tai-xe-theo-gio/"]
    },
    "07_Thue_Tai_Xe_Theo_Ngay_Da_Nang.png": {
        "alt": "Thuê tài xế theo ngày tại Đà Nẵng phục vụ công tác du lịch sự kiện",
        "role": "Daily Driver Hero",
        "target_pages": ["/dich-vu/thue-tai-xe-theo-ngay/"]
    },
    "08_Thue_Tai_Xe_Lai_Xe_Di_Tinh.png": {
        "alt": "Thuê tài xế lái xe đi tỉnh xuất phát từ Đà Nẵng đi Hội An Huế",
        "role": "Interprovincial Driver Hero",
        "target_pages": ["/dich-vu/thue-tai-xe-di-tinh/"]
    },
    "09_Huong_Dan_Dat_Tai_Xe_Nhu_Y_Driver.png": {
        "alt": "Hướng dẫn 3 bước đặt tài xế Như Ý Driver qua hotline và Zalo",
        "role": "Booking Guide Infographic",
        "target_pages": ["/blog/quy-trinh-dat-tai-xe-nhu-y-driver/", "/"]
    },
    "10_Lai_Xe_Ho_Va_Taxi_Nen_Chon_Dich_Vu_Nao.png": {
        "alt": "So sánh lái xe hộ và taxi nên chọn dịch vụ nào khi đi uống rượu bia",
        "role": "Comparison Infographic",
        "target_pages": ["/blog/lai-xe-ho-va-taxi-nen-chon-gi/"]
    },
    "11_Quy_Trinh_Dat_Tai_Xe_Nhu_Y_Driver.png": {
        "alt": "Quy trình 5 bước đặt tài xế lái xe hộ Như Ý Driver Đà Nẵng 24/7",
        "role": "5-step Process Timeline",
        "target_pages": ["/", "/gioi-thieu/"]
    },
    "12_Khu_Vuc_Phuc_Vu_Lai_Xe_Ho_Da_Nang.png": {
        "alt": "Bản đồ khu vực phục vụ lái xe hộ khắp các quận huyện Đà Nẵng",
        "role": "Service Area Map Infographic",
        "target_pages": ["/khu-vuc/", "/"]
    },
    "13_Lien_He_Nhu_Y_Driver.png": {
        "alt": "Thông tin liên hệ Như Ý Driver Hotline 0985 666 044 phục vụ 24/7",
        "role": "Contact Banner",
        "target_pages": ["/lien-he/"]
    },
    "14_Tai_Xe_Nhan_Chia_Khoa_Tu_Khach.png": {
        "alt": "Khách hàng bàn giao chìa khóa ô tô cho tài xế Như Ý Driver an tâm trên mọi nẻo đường",
        "role": "Key Handover Trust Image",
        "target_pages": ["/gioi-thieu/", "/dich-vu/thue-tai-xe-giao-nhan-xe/"]
    },
    "15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png": {
        "alt": "Đội ngũ tài xế chuyên nghiệp Như Ý Driver chụp trước Cầu Rồng Đà Nẵng",
        "role": "Driver Team Official Photo",
        "target_pages": ["/gioi-thieu/", "/"]
    },
    "16_Bang_Gia_Lai_Xe_May_Ho.png": {
        "alt": "Bảng giá lái xe máy hộ Đà Nẵng Như Ý Driver từ 110.000đ",
        "role": "Motorbike Pricing Banner",
        "target_pages": ["/bang-gia/", "/dich-vu/lai-xe-ho-xe-may/"]
    },
    "16_Bang_Gia_Lai_Xe_OTo_Ho.png": {
        "alt": "Bảng giá lái xe ô tô hộ Đà Nẵng Như Ý Driver từ 150.000đ",
        "role": "Car Pricing Banner",
        "target_pages": ["/bang-gia/", "/dich-vu/lai-xe-ho-o-to/"]
    },
    "17_Lai_Xe_Ho_La_Gi.png": {
        "alt": "Lái xe hộ là gì quy trình hoạt động và những điều cần biết",
        "role": "Blog Hero: Lái xe hộ là gì",
        "target_pages": ["/blog/lai-xe-ho-la-gi/"]
    },
    "18_Truong_Hop_Nen_Goi_Tai_Xe_Lai_Ho.png": {
        "alt": "7 trường hợp nên gọi tài xế lái hộ thay vì tự lái xe khi mệt mỏi say rượu",
        "role": "Blog Hero: 7 trường hợp",
        "target_pages": ["/blog/khi-nao-nen-goi-tai-xe-lai-ho/"]
    },
    "19_Chuan_Bi_Khi_Ban_Giao_Xe.png": {
        "alt": "Cần chuẩn bị gì khi bàn giao chìa khóa và phương tiện cho tài xế lái hộ",
        "role": "Blog Hero: Bàn giao xe",
        "target_pages": ["/blog/chuan-bi-khi-ban-giao-xe/"]
    },
    "20_Dat_Tai_Xe_Lai_Ho_Ban_Dem.png": {
        "alt": "Kinh nghiệm đặt tài xế lái xe hộ ban đêm an toàn tại Đà Nẵng",
        "role": "Blog Hero: Ban đêm",
        "target_pages": ["/blog/dat-tai-xe-lai-ho-ban-dem/"]
    },
    "21_Buon_Ngu_Khi_Lai_Xe.png": {
        "alt": "Cảnh báo buồn ngủ khi đang lái xe ban đêm và giải pháp dừng xe gọi tài xế",
        "role": "Blog Hero: Buồn ngủ",
        "target_pages": ["/blog/buon-ngu-khi-lai-xe/"]
    },
    "22_Uong_Ruou_Bia_Mang_Theo_Xe_May.png": {
        "alt": "Giải pháp đưa cả người và xe máy về an toàn sau khi uống rượu bia",
        "role": "Blog Hero: Xe máy uống rượu",
        "target_pages": ["/blog/uong-ruou-bia-mang-theo-xe-may/"]
    },
    "23_Di_Tiec_Bang_O_To_Da_Nang.png": {
        "alt": "Kinh nghiệm đi tiệc bằng ô tô tại Đà Nẵng và chuẩn bị phương án về nhà",
        "role": "Blog Hero: Đi tiệc ô tô",
        "target_pages": ["/blog/di-tiec-bang-o-to-da-nang/"]
    },
    "24_Thue_Tai_Xe_Theo_Gio_Hay_Theo_Ngay.png": {
        "alt": "Nên thuê tài xế theo giờ hay theo ngày lựa chọn theo lịch trình",
        "role": "Blog Hero: Giờ hay ngày",
        "target_pages": ["/blog/thue-tai-xe-theo-gio-hay-theo-ngay/"]
    },
    "25_Thue_Xe_Tu_Lai_Goi_Tai_Xe.png": {
        "alt": "Thuê xe tự lái có thể gọi tài xế lái thay không lưu ý hợp đồng bảo hiểm",
        "role": "Blog Hero: Thuê xe tự lái",
        "target_pages": ["/blog/thue-xe-tu-lai-goi-tai-xe/"]
    },
    "26_Tai_Xe_Dua_Don_Doi_Tac.png": {
        "alt": "Dịch vụ thuê tài xế riêng đưa đón đối tác VIP tại Đà Nẵng",
        "role": "Service Hero: Đối tác VIP",
        "target_pages": ["/dich-vu/thue-tai-xe-dua-don-doi-tac/"]
    },
    "27_Tai_Xe_Phu_Vu_Tiec_Cuoi_Su_Kien.png": {
        "alt": "Tài xế chuyên nghiệp phục vụ tiệc cưới sự kiện hội nghị Đà Nẵng",
        "role": "Service Hero: Tiệc cưới sự kiện",
        "target_pages": ["/dich-vu/thue-tai-xe-tiec-cuoi-su-kien/"]
    },
    "28_Thue_Tai_Xe_Da_Nang_Di_Hoi_An.png": {
        "alt": "Thuê tài xế lái xe từ Đà Nẵng đi Hội An trọn gói đúng giờ",
        "role": "Route Hero: Đà Nẵng - Hội An",
        "target_pages": ["/khu-vuc/da-nang-di-hoi-an/", "/blog/thue-tai-xe-da-nang-di-hoi-an/"]
    },
    "29_Thue_Tai_Xe_Da_Nang_Di_Hue.png": {
        "alt": "Thuê tài xế lái xe từ Đà Nẵng đi Huế vượt đèo Hải Vân an toàn",
        "role": "Route Hero: Đà Nẵng - Huế",
        "target_pages": ["/khu-vuc/da-nang-di-hue/", "/blog/thue-tai-xe-da-nang-di-hue/"]
    },
    "30_Lai_Xe_Ho_Hai_Chau_Da_Nang.png": {
        "alt": "Dịch vụ lái xe hộ quận Hải Châu Đà Nẵng 24/7 ô tô và xe máy",
        "role": "District Hero: Hải Châu",
        "target_pages": ["/khu-vuc/hai-chau/"]
    },
    "31_Lai_Xe_Ho_Son_Tra_Da_Nang.png": {
        "alt": "Dịch vụ lái xe hộ quận Sơn Trà Đà Nẵng 24/7 tuyến biển và quán nhậu",
        "role": "District Hero: Sơn Trà",
        "target_pages": ["/khu-vuc/son-tra/"]
    },
    "Doi_Ngu_Tai_Xe_Nhu_Y_Driver.png": {
        "alt": "Tài xế Như Ý Driver đồng phục đỏ túc trực 24/7 tại Đà Nẵng",
        "role": "Team Banner Alternative 1",
        "target_pages": ["/gioi-thieu/"]
    },
    "Doi_Ngu_Tai_Xe_Nhu_Y_Driver_1.png": {
        "alt": "Đội ngũ tài xế Như Ý Driver lịch sự thân thiện hỗ trợ khách hàng",
        "role": "Team Banner Alternative 2",
        "target_pages": ["/gioi-thieu/"]
    },
    "Icon_Car_Key.png": {
        "alt": "Icon giao nhận chìa khóa an tâm",
        "role": "Feature Icon: Key",
        "target_pages": ["All pages"]
    },
    "Icon_Clock_24_7.png": {
        "alt": "Icon phục vụ 24/7 có mặt sau 15-20 phút",
        "role": "Feature Icon: 24/7 Clock",
        "target_pages": ["All pages"]
    },
    "Icon_Location.png": {
        "alt": "Icon khu vực phục vụ nội thành và ngoại thành Đà Nẵng",
        "role": "Feature Icon: Location",
        "target_pages": ["All pages"]
    },
    "Icon_Phone.png": {
        "alt": "Icon gọi hotline 0985 666 044",
        "role": "Feature Icon: Phone",
        "target_pages": ["All pages"]
    },
    "Icon_Zalo.png": {
        "alt": "Icon nhắn tin đặt tài xế Zalo 0985 666 044",
        "role": "Feature Icon: Zalo",
        "target_pages": ["All pages"]
    }
}

manifest = []

for filename in os.listdir(src_dir):
    src_file = os.path.join(src_dir, filename)
    if not os.path.isfile(src_file):
        continue
    
    # Copy file to assets/images
    dst_file = os.path.join(dst_dir, filename)
    
    try:
        with Image.open(src_file) as img:
            w, h = img.size
            fmt = img.format
            file_size_kb = round(os.path.getsize(src_file) / 1024, 1)
            
            # Save original to dst_dir
            img.save(dst_file)
            
            # Save WebP version for web optimization
            name_no_ext, _ = os.path.splitext(filename)
            webp_name = f"{name_no_ext}.webp"
            webp_dst = os.path.join(dst_dir, webp_name)
            
            # If RGBA or P convert appropriately
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img_conv = img.convert("RGBA")
            else:
                img_conv = img.convert("RGB")
            
            img_conv.save(webp_dst, "WEBP", quality=85, method=6)
            webp_size_kb = round(os.path.getsize(webp_dst) / 1024, 1)
            
            desc = image_descriptions.get(filename, {
                "alt": f"Hình ảnh {name_no_ext} Như Ý Driver Đà Nẵng",
                "role": "Minh họa dịch vụ",
                "target_pages": ["Website"]
            })
            
            manifest.append({
                "filename": filename,
                "webp_filename": webp_name,
                "path": f"/assets/images/{filename}",
                "webp_path": f"/assets/images/{webp_name}",
                "width": w,
                "height": h,
                "original_format": fmt,
                "original_size_kb": file_size_kb,
                "webp_size_kb": webp_size_kb,
                "compression_ratio": f"{round((1 - webp_size_kb / file_size_kb) * 100, 1)}%",
                "alt": desc["alt"],
                "role": desc["role"],
                "target_pages": desc["target_pages"]
            })
            print(f"Processed {filename}: {w}x{h}, {file_size_kb}KB -> WebP {webp_size_kb}KB")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

manifest_path = str(PROJECT_ROOT / "research" / "image-manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nSaved image manifest with {len(manifest)} images to {manifest_path}")

