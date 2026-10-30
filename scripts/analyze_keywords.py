import csv
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open('research/keywords_combined.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total unique keywords: {len(rows)}")

keywords = [r['Từ khóa'] for r in rows]

# Let's inspect frequency of some words
words = Counter()
for kw in keywords:
    for w in kw.lower().split():
        words[w] += 1

print("\nTop 30 frequent words in keywords:")
for w, count in words.most_common(30):
    print(f"  {w}: {count}")

# Check sample keywords by categories
categories = {
    'da_nang': [k for k in keywords if 'đà nẵng' in k.lower() or 'da nang' in k.lower()],
    'o_to': [k for k in keywords if 'ô tô' in k.lower() or 'oto' in k.lower() or 'xe hơi' in k.lower() or 'ôto' in k.lower()],
    'xe_may': [k for k in keywords if 'xe máy' in k.lower() or 'xe may' in k.lower()],
    'ruou_bia': [k for k in keywords if any(x in k.lower() for x in ['rượu', 'bia', 'uống', 'say', 'tiệc', 'nhậu'])],
    'gia_ca': [k for k in keywords if any(x in k.lower() for x in ['giá', 'nhiêu tiền', 'bảng giá', 'chi phí', '150k', 'rẻ'])],
    'theo_gio_ngay': [k for k in keywords if any(x in k.lower() for x in ['giờ', 'ngày', 'đêm', '24/7', '247', '24h'])],
    'tuyen_duong': [k for k in keywords if any(x in k.lower() for x in ['hải châu', 'sơn trà', 'hội an', 'huế', 'quảng ngãi', 'tỉnh', 'liên chiểu', 'thanh khê'])],
    'thong_tin_cau_hoi': [k for k in keywords if any(x in k.lower() for x in ['là gì', 'như thế nào', 'thế nào', 'sao', 'có nên', 'review', 'kinh nghiệm', 'chuẩn bị', 'quy trình', 'khác'])],
    'tuyen_dung_or_unrelated': [k for k in keywords if any(x in k.lower() for x in ['tuyển', 'tuyển dụng', 'việc làm', 'đăng ký lái', 'làm tài xế', 'hồ sơ tài xế', 'bằng lái', 'thi bằng', 'b2', 'học lái'])]
}

print("\nCategory counts:")
for cat, kw_list in categories.items():
    print(f"  {cat}: {len(kw_list)} keywords")

