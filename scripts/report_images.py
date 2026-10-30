import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join('assets', 'images')
files = os.listdir(img_dir)

ext_stats = {}
total_size = 0

for f in files:
    ext = os.path.splitext(f)[1].lower()
    sz = os.path.getsize(os.path.join(img_dir, f))
    total_size += sz
    if ext not in ext_stats:
        ext_stats[ext] = {'count': 0, 'size': 0}
    ext_stats[ext]['count'] += 1
    ext_stats[ext]['size'] += sz

print("=== ASSETS/IMAGES SUMMARY ===")
print(f"Total image files on disk: {len(files)}")
for ext, data in sorted(ext_stats.items()):
    mb = data['size'] / (1024 * 1024)
    kb = data['size'] / 1024
    print(f"  {ext.upper():5} : {data['count']:2} files | {mb:6.2f} MB ({kb:8.1f} KB)")
print(f"Total storage on disk: {total_size / (1024*1024):.2f} MB")

# Calculate HTML page weight impact:
# When pages serve WebP instead of PNG:
png_size = ext_stats.get('.png', {}).get('size', 0)
webp_size = ext_stats.get('.webp', {}).get('size', 0)
savings_mb = (png_size - webp_size) / (1024 * 1024)
savings_pct = ((png_size - webp_size) / png_size) * 100 if png_size else 0

print("\n=== WEB PERFORMANCE OPTIMIZATION ===")
print(f"Legacy PNG total weight: {png_size / (1024*1024):.2f} MB")
print(f"Modern WebP total weight: {webp_size / (1024*1024):.2f} MB")
print(f"Bandwidth saved per full site scan: {savings_mb:.2f} MB ({savings_pct:.1f}% reduction)")

