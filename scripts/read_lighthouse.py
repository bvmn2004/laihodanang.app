import json

with open("research/lighthouse-report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

print("="*40)
print("LIGHTHOUSE AUDIT SCORES")
print("="*40)
for cat_id, cat in report.get("categories", {}).items():
    score = round(cat.get("score", 0) * 100)
    print(f"  {cat.get('title')}: {score}/100")
print("="*40)

