import glob
import os
import re
import sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

class ImgTagParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self.images.append(dict(attrs))

html_files = [f for f in glob.glob('**/*.html', recursive=True) if 'node_modules' not in f and 'research' not in f]

missing_attrs = []
total_imgs = 0

for hf in sorted(html_files):
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    p = ImgTagParser(hf)
    p.feed(content)
    total_imgs += len(p.images)
    for img in p.images:
        src = img.get('src', '')
        w = img.get('width')
        h = img.get('height')
        loading = img.get('loading')
        decoding = img.get('decoding')
        fetchpriority = img.get('fetchpriority')
        
        # Check if missing dimensions or loading/decoding
        issues = []
        if not w:
            issues.append('missing width')
        if not h:
            issues.append('missing height')
        if not loading and not fetchpriority:
            issues.append('missing loading/fetchpriority')
        if not decoding and not fetchpriority:
            issues.append('missing decoding')

        if issues:
            missing_attrs.append((hf, src, issues, img))

print(f"Total HTML files: {len(html_files)}")
print(f"Total <img> tags: {total_imgs}")
print(f"Images with missing attributes: {len(missing_attrs)}")

# Group by src
from collections import defaultdict
grouped = defaultdict(list)
for hf, src, issues, img in missing_attrs:
    grouped[src].append((hf, issues))

for src, occurrences in grouped.items():
    print(f"\nSRC: {src} ({len(occurrences)} occurrences)")
    print(f"  Issues: {occurrences[0][1]}")
    print(f"  Sample page: {occurrences[0][0]}")

