import glob
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in glob.glob('**/*.html', recursive=True) if 'node_modules' not in f and 'research' not in f]

types_found = set()
errors = []

for hf in sorted(html_files):
    with open(hf, 'r', encoding='utf-8') as f:
        c = f.read()
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL)
    for s in scripts:
        data = json.loads(s)
        types_found.add(data.get('@type'))
        if '16.0678' in s or '108.2208' in s:
            errors.append(f'Prohibited coordinates in {hf}')
        if 'aggregateRating' in s:
            errors.append(f'Fake rating in {hf}')
        if 'geo' in data:
            errors.append(f'Geo coordinates in {hf}')
        if data.get('@type') == 'AutomotiveBusiness':
            if data.get('paymentAccepted') != 'Cash, Bank Transfer':
                errors.append(f'Payment error in {hf}: {data.get("paymentAccepted")}')
            if data.get('priceRange') != 'Từ 110.000đ':
                errors.append(f'Price range error in {hf}: {data.get("priceRange")}')

print(f"Total HTML files inspected: {len(html_files)}")
print(f"Schema types found: {sorted(types_found)}")
print(f"Total Schema Errors: {len(errors)}")
if errors:
    for e in errors:
        print(f"  ❌ {e}")
else:
    print("✅ All schemas strictly compliant with user specifications!")

