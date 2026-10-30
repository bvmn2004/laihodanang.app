import csv
import glob
import sys
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

all_keywords = []
for f in sorted(Path('research/keywords').glob('*.csv')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for r in reader:
            if r and len(r) >= 3:
                kw = r[0].strip('"\ufeff ').lower()
                source = r[1].strip()
                intent = r[2].strip()
                all_keywords.append((kw, source, intent))

print(f"Total extracted keyword entries: {len(all_keywords)}")
unique_kws = {}
for kw, src, intent in all_keywords:
    if kw not in unique_kws:
        unique_kws[kw] = (src, intent)

print(f"Unique keywords: {len(unique_kws)}")

intents = Counter([intent for _, _, intent in all_keywords])
print("\n=== SEARCH INTENTS ===")
for it, cnt in intents.most_common():
    print(f"  {it:30} : {cnt}")

# Let's see topic categories
categories = defaultdict(list)
for kw, (src, intent) in unique_kws.items():
    if any(k in kw for k in ['bảng giá', 'giá', 'chi phí', 'bao nhiêu', 'cước']):
        categories['Pricing / Bảng giá'].append(kw)
    elif any(k in kw for k in ['ô tô', 'o to', 'xe hoi', 'xe hơi', 'oto']):
        categories['Ô tô'].append(kw)
    elif any(k in kw for k in ['xe máy', 'xe may', 'xe máy hộ', 'xe om']):
        categories['Xe máy'].append(kw)
    elif any(k in kw for k in ['nhậu', 'say', 'uống bia', 'rượu', 'bia', 'sau tiệc', 'bạn uống']):
        categories['Sau nhậu / Bạn uống tôi lái'].append(kw)
    elif any(k in kw for k in ['hải châu', 'sơn trà', 'thanh khê', 'ngũ hành sơn', 'liên chiểu', 'cẩm lệ', 'hòa vang']):
        categories['Khu vực quận huyện Đà Nẵng'].append(kw)
    elif any(k in kw for k in ['hội an', 'huế', 'quảng ngãi', 'đi tỉnh', 'liên tỉnh', 'đường dài']):
        categories['Đi tỉnh / Hội An / Huế / Quảng Ngãi'].append(kw)
    elif any(k in kw for k in ['theo giờ', 'theo ngày', 'thuê tài xế riêng', 'theo chuyến']):
        categories['Thuê theo giờ / ngày'].append(kw)
    elif any(k in kw for k in ['app', 'ứng dụng', 'đặt xe', 'số điện thoại', 'hotline', 'gọi']):
        categories['Đặt xe / Hotline / App'].append(kw)
    elif any(k in kw for k in ['là gì', 'quy trình', 'thủ tục', 'kinh nghiệm', 'lưu ý', 'chuẩn bị']):
        categories['Kiến thức / Cẩm nang / FAQ'].append(kw)
    else:
        categories['Chung / Dịch vụ lái xe hộ'].append(kw)

print("\n=== KEYWORD CLUSTERS ===")
for cat, kwlist in sorted(categories.items(), key=lambda x: -len(x[1])):
    print(f"  {cat:35} : {len(kwlist):3} keywords")
    for sample in kwlist[:3]:
        print(f"    - {sample}")

