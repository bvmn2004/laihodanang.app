import os
import sys
import glob
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

class HTMLValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.h1_count = 0
        self.h1_text = ""
        self.in_h1 = False
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.canonical = ""
        self.has_floating_contact = False
        self.links = []
        self.images = []
        self.raw_img_tags = []
        self.schemas = []
        self.raw_scripts = []
        self.in_script_ld = False
        self.script_data = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'floating-contact':
            self.has_floating_contact = True

        if tag == 'h1':
            self.h1_count += 1
            self.in_h1 = True
        elif tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            if attrs_dict.get('name') == 'description':
                self.meta_desc = attrs_dict.get('content', '')
        elif tag == 'link':
            if attrs_dict.get('rel') == 'canonical':
                self.canonical = attrs_dict.get('href', '')
        elif tag == 'a':
            href = attrs_dict.get('href')
            if href:
                self.links.append((href, attrs_dict.get('aria-label')))
        elif tag == 'img':
            self.raw_img_tags.append(attrs_dict)
            src = attrs_dict.get('src')
            if src:
                self.images.append(src)
        elif tag == 'source':
            srcset = attrs_dict.get('srcset')
            if srcset:
                self.images.append(srcset)
        elif tag == 'script':
            if attrs_dict.get('type') == 'application/ld+json':
                self.in_script_ld = True
                self.script_data = ""

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False
        elif tag == 'title':
            self.in_title = False
        elif tag == 'script' and self.in_script_ld:
            self.in_script_ld = False
            raw_text = self.script_data.strip()
            self.raw_scripts.append(raw_text)
            try:
                data = json.loads(raw_text)
                self.schemas.append(data)
            except Exception as e:
                self.schemas.append(f"JSON-LD ERROR: {e}")

    def handle_data(self, data):
        if self.in_h1:
            self.h1_text += data
        elif self.in_title:
            self.title += data
        elif self.in_script_ld:
            self.script_data += data

def main():
    html_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if any(skip in root for skip in ['.git', 'node_modules', '.gemini', 'brain', 'scripts', 'research']):
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    html_files = sorted(html_files)
    print(f"Total HTML files found to inspect: {len(html_files)}")

    if len(html_files) == 0:
        print("CRITICAL ERROR: Zero HTML files found! Aborting.")
        sys.exit(1)

    errors = []
    warnings = []
    all_titles = set()
    all_canonicals = set()
    scanned_urls = set()

    for html_file in html_files:
        rel_path = os.path.relpath(html_file, PROJECT_ROOT).replace('\\', '/')
        if rel_path == 'index.html':
            scanned_urls.add('/')
        elif rel_path.endswith('/index.html'):
            scanned_urls.add('/' + rel_path[:-10])
        elif rel_path.endswith('.html'):
            scanned_urls.add('/' + rel_path)

        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        parser = HTMLValidator(rel_path)
        parser.feed(content)

        # Strict domain check: NO foreign domain allowed
        if 'laixehodanang.me' in content or 'laihodanang.me' in content:
            errors.append(f"[{rel_path}] Contains unapproved foreign domain (must strictly be https://laihodanang.app/)")

        # 1. H1 check
        if parser.h1_count != 1:
            errors.append(f"[{rel_path}] H1 count error: found {parser.h1_count} h1 tags (must be exactly 1)")

        # 2. Title check
        if not parser.title.strip():
            errors.append(f"[{rel_path}] Missing <title>")
        elif parser.title in all_titles:
            warnings.append(f"[{rel_path}] Duplicate title: {parser.title}")
        all_titles.add(parser.title)

        # 3. Meta description check
        if not parser.meta_desc.strip():
            errors.append(f"[{rel_path}] Missing meta description")

        # 4. Canonical and Robots check
        if rel_path == '404.html':
            if parser.canonical.strip():
                errors.append(f"[{rel_path}] 404 page should not have a canonical tag")
            if 'noindex' not in content:
                errors.append(f"[{rel_path}] 404 page must have noindex tag")
        else:
            if not parser.canonical.strip():
                errors.append(f"[{rel_path}] Missing canonical URL")
            elif parser.canonical:
                if not parser.canonical.startswith('https://laihodanang.app/'):
                    errors.append(f"[{rel_path}] Canonical URL does not use https://laihodanang.app/ : {parser.canonical}")
                if parser.canonical in all_canonicals:
                    errors.append(f"[{rel_path}] Duplicate canonical URL: {parser.canonical}")
                all_canonicals.add(parser.canonical)

        # 5. Floating contact check
        if not parser.has_floating_contact:
            errors.append(f"[{rel_path}] Missing #floating-contact component")

        # 6. Check images existence and attributes
        for img in parser.images:
            if img.startswith('/'):
                img_path = PROJECT_ROOT / img.lstrip('/')
                if not img_path.is_file():
                    errors.append(f"[{rel_path}] Image missing on disk: {img} -> {img_path}")

        for img_attrs in parser.raw_img_tags:
            src = img_attrs.get('src', '')
            alt = img_attrs.get('alt')
            w = img_attrs.get('width')
            h = img_attrs.get('height')
            decoding = img_attrs.get('decoding')
            loading = img_attrs.get('loading')
            fetchpriority = img_attrs.get('fetchpriority')

            if alt is None:
                errors.append(f"[{rel_path}] <img> missing alt attribute: {src}")
            if not w or not h:
                errors.append(f"[{rel_path}] <img> missing width/height: {src} (w={w}, h={h})")
            if not decoding:
                errors.append(f"[{rel_path}] <img> missing decoding='async': {src}")
            if not loading and not fetchpriority:
                errors.append(f"[{rel_path}] <img> missing loading='lazy' or fetchpriority='high': {src}")

        # 7. Check internal links
        for link, aria in parser.links:
            if link.startswith('/') and not link.startswith('//'):
                clean_link = link.split('#')[0].split('?')[0]
                if clean_link == '/':
                    target_file = PROJECT_ROOT / 'index.html'
                elif clean_link.endswith('/'):
                    target_file = PROJECT_ROOT / clean_link.lstrip('/') / 'index.html'
                else:
                    target_file = PROJECT_ROOT / clean_link.lstrip('/')
                
                if not target_file.exists():
                    errors.append(f"[{rel_path}] Broken internal link: {link} -> {target_file}")
            elif link.startswith('tel:'):
                if link != 'tel:0985666044':
                    warnings.append(f"[{rel_path}] Non-standard telephone link: {link}")
            elif 'zalo.me' in link:
                if link != 'https://zalo.me/0985666044':
                    warnings.append(f"[{rel_path}] Non-standard Zalo link: {link}")

        # 8. Check Schema JSON-LD
        for raw_s in parser.raw_scripts:
            # Check prohibited coordinates
            if "16.0678" in raw_s or "108.2208" in raw_s:
                errors.append(f"[{rel_path}] Prohibited unverified coordinates found in Schema: 16.0678 / 108.2208")
            if "GeoCoordinates" in raw_s:
                errors.append(f"[{rel_path}] GeoCoordinates schema should not be present without physical verified address")
            if "aggregateRating" in raw_s or "ratingValue" in raw_s or "Review" in raw_s:
                errors.append(f"[{rel_path}] Fake review/rating found in Schema")

        for s in parser.schemas:
            if isinstance(s, str) and s.startswith("JSON-LD ERROR"):
                errors.append(f"[{rel_path}] {s}")
            elif isinstance(s, dict):
                # Validate AutomotiveBusiness
                if s.get('@type') == 'AutomotiveBusiness':
                    price_range = s.get('priceRange', '')
                    if '-' in price_range or '500' in price_range:
                        errors.append(f"[{rel_path}] AutomotiveBusiness priceRange contains unverified max bound: {price_range}")
                    pm = s.get('paymentAccepted', '')
                    if any(unconf in pm.lower() for unconf in ['momo', 'zalopay', 'credit card']):
                        errors.append(f"[{rel_path}] AutomotiveBusiness paymentAccepted contains unverified methods: {pm}")

    # 9. Audit Sitemap.xml
    sitemap_path = PROJECT_ROOT / "sitemap.xml"
    if not sitemap_path.is_file():
        errors.append("sitemap.xml is missing from project root!")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root_el = tree.getroot()
            namespaces = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            sitemap_urls = set()
            for loc in root_el.findall('sm:url/sm:loc', namespaces):
                url = loc.text.strip().replace('https://laihodanang.app', '')
                if not url:
                    url = '/'
                sitemap_urls.add(url)

            # Check that all sitemap URLs correspond to an HTML file
            for surl in sitemap_urls:
                if surl == '/':
                    target = PROJECT_ROOT / 'index.html'
                elif surl.endswith('/'):
                    target = PROJECT_ROOT / surl.lstrip('/') / 'index.html'
                else:
                    target = PROJECT_ROOT / surl.lstrip('/')
                if not target.exists():
                    errors.append(f"sitemap.xml URL does not exist as file: {surl} -> {target}")

            # Check all non-404 HTML files are in sitemap
            expected_pages = {u for u in scanned_urls if u != '/404.html'}
            missing_from_sitemap = expected_pages - sitemap_urls
            if missing_from_sitemap:
                for mp in missing_from_sitemap:
                    errors.append(f"Page missing from sitemap.xml: {mp}")

            print(f"Sitemap check: {len(sitemap_urls)} URLs verified against filesystem.")
        except Exception as e:
            errors.append(f"Failed to parse sitemap.xml: {e}")

    # 10. Audit robots.txt
    robots_path = PROJECT_ROOT / "robots.txt"
    if not robots_path.is_file():
        errors.append("robots.txt is missing from project root!")
    else:
        with open(robots_path, 'r', encoding='utf-8') as f:
            robots_content = f.read()
        if "sitemap.xml" not in robots_content.lower():
            errors.append("robots.txt does not declare Sitemap URL")
        if "disallow: /404.html" in robots_content.lower():
            errors.append("robots.txt should not contain 'Disallow: /404.html' so crawlers can access 404 status/noindex")

    # 11. Audit GitHub Pages config (.nojekyll and CNAME)
    nojekyll_path = PROJECT_ROOT / ".nojekyll"
    if not nojekyll_path.exists():
        errors.append(".nojekyll is missing (required for GitHub Pages static serving)")

    cname_path = PROJECT_ROOT / "CNAME"
    if not cname_path.is_file():
        errors.append("CNAME file is missing from project root!")
    else:
        with open(cname_path, 'r', encoding='utf-8') as f:
            cname_content = f.read().strip()
        if cname_content != "laihodanang.app":
            errors.append(f"CNAME content mismatch: expected 'laihodanang.app', found '{cname_content}'")

    # Output report
    print("\n" + "="*50)
    print("VERIFICATION RESULTS")
    print("="*50)
    print(f"Total HTML files checked: {len(html_files)}")
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")

    if errors:
        print("\nERRORS FOUND:")
        for err in errors:
            print(f"  ❌ {err}")
        print("==================================================")
        sys.exit(1)
    else:
        print(f"\n  [PASS] ALL {len(html_files)} HTML FILES PASSED VALIDATION PERFECTLY!")
        print("  - Zero broken links")
        print("  - Zero missing images on disk")
        print("  - All <img> tags have width, height, decoding, and loading/fetchpriority")
        print("  - All Schema JSON-LD clean of coordinates, fake ratings, or unverified payments")
        print("  - All pages contain #floating-contact")
        print("  - Exactly 1 H1 per page")
        print("  - Sitemap and robots.txt fully synchronized")
        print("==================================================")
        sys.exit(0)

if __name__ == '__main__':
    main()
