import glob
import os
import csv
import sys
import re
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

def normalize_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    csv_files = glob.glob('research/keywords/tu-khoa-2026-10-30*.csv')
    print(f"Total CSV files found: {len(csv_files)}")
    
    all_rows = []
    keyword_dict = {}  # normalized lower keyword -> combined data
    
    for file_path in csv_files:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row_idx, row in enumerate(reader):
                if not row or len(row) < 1:
                    continue
                kw = normalize_text(row[0])
                if not kw:
                    continue
                source = normalize_text(row[1]) if len(row) > 1 else ""
                intent = normalize_text(row[2]) if len(row) > 2 else ""
                cluster = normalize_text(row[3]) if len(row) > 3 else ""
                score = normalize_text(row[4]) if len(row) > 4 else ""
                
                kw_lower = kw.lower()
                if kw_lower not in keyword_dict:
                    keyword_dict[kw_lower] = {
                        'keyword': kw,
                        'sources': set([source] if source else []),
                        'files': set([filename]),
                        'intents': set([intent] if intent else []),
                        'clusters': set([cluster] if cluster else []),
                        'scores': [score] if score else []
                    }
                else:
                    if source:
                        keyword_dict[kw_lower]['sources'].add(source)
                    keyword_dict[kw_lower]['files'].add(filename)
                    if intent:
                        keyword_dict[kw_lower]['intents'].add(intent)
                    if cluster:
                        keyword_dict[kw_lower]['clusters'].add(cluster)
                    if score:
                        keyword_dict[kw_lower]['scores'].append(score)

    print(f"Total unique keywords extracted: {len(keyword_dict)}")
    
    # Save combined raw data
    combined_csv = 'research/keywords_combined.csv'
    with open(combined_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Từ khóa', 'Nguồn', 'Ý định', 'Cụm chủ đề gốc', 'Điểm cơ hội (gốc)', 'Files xuất hiện'])
        for kw_lower, data in sorted(keyword_dict.items(), key=lambda x: x[0]):
            writer.writerow([
                data['keyword'],
                ", ".join(sorted(data['sources'])),
                ", ".join(sorted(data['intents'])),
                ", ".join(sorted(data['clusters'])),
                ", ".join(sorted(data['scores'])),
                ", ".join(sorted(data['files']))
            ])
    print(f"Saved combined keywords to {combined_csv}")

if __name__ == '__main__':
    main()

