import os
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

class FloatingContactParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.fc_count = 0
        self.in_fc = False
        self.fb_link = None
        self.zalo_link = None
        self.call_link = None
        self.zalo_img = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'floating-contact':
            self.fc_count += 1
            self.in_fc = True

        if self.in_fc:
            classes = attrs_dict.get('class', '').split()
            if tag == 'a':
                if 'fb-btn' in classes:
                    self.fb_link = attrs_dict.get('href')
                elif 'zalo-btn' in classes:
                    self.zalo_link = attrs_dict.get('href')
                elif 'call-btn' in classes:
                    self.call_link = attrs_dict.get('href')
            elif tag == 'img' and 'zalo-icon-img' in classes:
                self.zalo_img = attrs_dict.get('src')

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_fc:
            pass

def audit_floating_contact():
    html_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if any(skip in root for skip in ['.git', 'node_modules', '.gemini', 'brain', 'scripts', 'research']):
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    print(f"Auditing floating contact across {len(html_files)} HTML files...")

    if len(html_files) == 0:
        print("ERROR: No HTML files found! Aborting.")
        sys.exit(1)

    all_passed = True
    missing_fc = []
    multiple_fc = []
    bad_links = []
    bad_images = []

    for hf in sorted(html_files):
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()

        p = FloatingContactParser(hf)
        p.feed(content)

        if p.fc_count == 0:
            missing_fc.append(hf)
            all_passed = False
        elif p.fc_count > 1:
            multiple_fc.append((hf, p.fc_count))
            all_passed = False

        if p.fb_link != "https://www.facebook.com/laixehodanang247/":
            bad_links.append((hf, 'fb', p.fb_link))
            all_passed = False

        if p.zalo_link != "https://zalo.me/0985666044":
            bad_links.append((hf, 'zalo', p.zalo_link))
            all_passed = False

        if p.call_link != "tel:0985666044":
            bad_links.append((hf, 'call', p.call_link))
            all_passed = False

        if p.zalo_img != "/assets/images/zalo-icon.svg":
            bad_images.append((hf, p.zalo_img))
            all_passed = False

    # Check image on disk
    img_path = PROJECT_ROOT / "assets" / "images" / "zalo-icon.svg"
    img_exists = img_path.is_file()

    print("\n================ FLOATING CONTACT AUDIT ================")
    print(f"Total HTML files audited: {len(html_files)}")
    print(f"Pages with exactly 1 #floating-contact: {len(html_files) - len(missing_fc) - len(multiple_fc)} / {len(html_files)}")
    print(f"Missing #floating-contact: {len(missing_fc)}")
    print(f"Multiple #floating-contact: {len(multiple_fc)}")
    print(f"Invalid links: {len(bad_links)}")
    print(f"Zalo icon image exists on disk: {img_exists} ({img_path})")
    
    passed = all_passed and img_exists and len(html_files) > 0
    print(f"Overall status: {'[PASS] 100% PERFECT PASS' if passed else '[FAIL] FAILED'}")
    print("========================================================\n")

    if not passed:
        sys.exit(1)

if __name__ == '__main__':
    audit_floating_contact()
