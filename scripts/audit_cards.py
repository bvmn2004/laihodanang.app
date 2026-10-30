import os
import sys
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

class CardParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.service_cards = 0
        self.blog_cards = 0
        self.non_anchor_cards = []
        self.cards_info = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        if 'service-card' in classes or 'blog-card' in classes:
            card_type = 'service-card' if 'service-card' in classes else 'blog-card'
            if card_type == 'service-card':
                self.service_cards += 1
            else:
                self.blog_cards += 1

            if tag != 'a':
                self.non_anchor_cards.append((tag, card_type, attrs_dict))
            else:
                self.cards_info.append({
                    'type': card_type,
                    'href': attrs_dict.get('href', ''),
                    'aria_label': attrs_dict.get('aria-label', '')
                })

def main():
    html_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if any(skip in root for skip in ['.git', 'node_modules', '.gemini', 'brain', 'scripts', 'research']):
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    if len(html_files) == 0:
        print("ERROR: No HTML files found! Aborting.")
        sys.exit(1)

    total_service = 0
    total_blog = 0
    total_non_anchor = 0
    missing_href = 0

    for hf in sorted(html_files):
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
        p = CardParser(hf)
        p.feed(content)
        total_service += p.service_cards
        total_blog += p.blog_cards
        if p.non_anchor_cards:
            total_non_anchor += len(p.non_anchor_cards)
            print(f"FAILED in {hf}: {p.non_anchor_cards}")
        for c in p.cards_info:
            if not c['href']:
                missing_href += 1
                print(f"Missing href in {hf}: {c}")

    print("\n========== CARD AUDIT SUMMARY ==========")
    print(f"Scanned {len(html_files)} HTML files")
    print(f"Total service cards: {total_service}")
    print(f"Total blog cards: {total_blog}")
    print(f"Total cards overall: {total_service + total_blog}")
    print(f"Non-anchor cards: {total_non_anchor} (Must be 0)")
    print(f"Cards missing href: {missing_href} (Must be 0)")
    print("=========================================\n")

    if total_non_anchor > 0 or missing_href > 0 or len(html_files) == 0:
        sys.exit(1)

if __name__ == '__main__':
    main()

