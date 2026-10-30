import os
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PHONE_PATTERN = re.compile(r'0985[\s\.]?666[\s\.]?044')

class AnchorAuditParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.anchor_depth = 0
        self.nested_anchors = 0
        self.tel_links = []
        self.zalo_links = []
        self.raw_phones = []
        self.current_tag = None
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        self.current_attrs = attrs_dict

        if tag == 'a':
            if self.anchor_depth > 0:
                self.nested_anchors += 1
            self.anchor_depth += 1
            href = attrs_dict.get('href', '')
            if href.startswith('tel:'):
                self.tel_links.append((href, attrs_dict.get('aria-label')))
            if 'zalo.me' in href:
                self.zalo_links.append((href, attrs_dict.get('aria-label')))

    def handle_endtag(self, tag):
        if tag == 'a':
            self.anchor_depth = max(0, self.anchor_depth - 1)
        self.current_tag = None

    def handle_data(self, data):
        # Ignore script or style tags
        if self.current_tag in ['script', 'style']:
            return
        if PHONE_PATTERN.search(data):
            if self.anchor_depth == 0:
                self.raw_phones.append(data.strip())

def audit():
    html_files = []
    for dirpath, _, filenames in os.walk(PROJECT_ROOT):
        if any(skip in dirpath for skip in ['.git', 'node_modules', '.gemini', 'brain', 'scripts', 'research']):
            continue
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))

    print(f"Auditing {len(html_files)} HTML files using standard HTMLParser...")

    if len(html_files) == 0:
        print("ERROR: No HTML files found! Aborting.")
        sys.exit(1)

    total_nested = 0
    total_tel = 0
    total_tel_without_aria = 0
    total_zalo = 0
    total_raw = 0
    raw_files = []

    for file_path in html_files:
        rel_path = os.path.relpath(file_path, PROJECT_ROOT)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        parser = AnchorAuditParser(rel_path)
        parser.feed(content)

        total_nested += parser.nested_anchors
        total_tel += len(parser.tel_links)
        for href, aria in parser.tel_links:
            if not aria:
                total_tel_without_aria += 1
        total_zalo += len(parser.zalo_links)
        if parser.raw_phones:
            total_raw += len(parser.raw_phones)
            raw_files.append((rel_path, parser.raw_phones))

    print("\n================ AUDIT RESULTS ================")
    print(f"Total HTML files scanned: {len(html_files)}")
    print(f"Total clickable tel: links: {total_tel}")
    print(f"Total tel: links missing aria-label: {total_tel_without_aria}")
    print(f"Total Zalo links: {total_zalo}")
    print(f"Nested <a> tags: {total_nested} (Must be 0)")
    print(f"Raw unlinked phone numbers: {total_raw}")
    if raw_files:
        print("\nDetail of raw unlinked phone numbers found:")
        for rpath, texts in raw_files:
            print(f"  In {rpath}:")
            for t in texts[:5]:
                print(f"    - {t}")
    print("===============================================")

    if total_nested > 0 or len(html_files) == 0:
        sys.exit(1)

if __name__ == '__main__':
    audit()
