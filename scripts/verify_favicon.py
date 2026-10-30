import os
import sys
import json
from pathlib import Path
from PIL import Image, IcoImagePlugin

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_ICONS = {
    "favicon.ico": {"format": "ICO", "sizes": {(16, 16), (32, 32), (48, 48)}},
    "favicon-16x16.png": {"format": "PNG", "size": (16, 16)},
    "favicon-32x32.png": {"format": "PNG", "size": (32, 32)},
    "favicon-48x48.png": {"format": "PNG", "size": (48, 48)},
    "favicon-96x96.png": {"format": "PNG", "size": (96, 96)},
    "apple-touch-icon.png": {"format": "PNG", "size": (180, 180)},
    "android-chrome-192x192.png": {"format": "PNG", "size": (192, 192)},
    "android-chrome-512x512.png": {"format": "PNG", "size": (512, 512)},
    "icon-maskable-192x192.png": {"format": "PNG", "size": (192, 192)},
    "icon-maskable-512x512.png": {"format": "PNG", "size": (512, 512)},
    "mstile-150x150.png": {"format": "PNG", "size": (150, 150)}
}

ORIGINAL_LOGO_PATH = PROJECT_ROOT / "assets" / "images" / "logo.png"
# Original logo was 1254x1254 RGB and around 1,051,842 bytes
ORIGINAL_LOGO_EXPECTED_SIZE = (1254, 1254)

def run_audit():
    errors = []
    print("=" * 60)
    print("FAVICON & APP ICON AUDIT SUITE")
    print("=" * 60)

    # 1. Audit Original Logo integrity
    print("\n[1] Checking Original Logo Integrity...")
    if not ORIGINAL_LOGO_PATH.exists():
        errors.append(f"Original logo missing at {ORIGINAL_LOGO_PATH}")
    else:
        with Image.open(ORIGINAL_LOGO_PATH) as img:
            if img.size != ORIGINAL_LOGO_EXPECTED_SIZE:
                errors.append(f"Original logo size changed! Expected {ORIGINAL_LOGO_EXPECTED_SIZE}, got {img.size}")
            else:
                print(f"  ✓ Original logo intact: {ORIGINAL_LOGO_PATH.name} ({img.size[0]}x{img.size[1]}, {img.format}, {ORIGINAL_LOGO_PATH.stat().st_size} bytes)")

    # 2. Audit All 11 Icon Files
    print("\n[2] Checking 11 Icon Files on Disk...")
    for filename, specs in EXPECTED_ICONS.items():
        file_path = PROJECT_ROOT / filename
        if not file_path.exists():
            errors.append(f"Missing icon file: {filename}")
            continue

        file_size = file_path.stat().st_size
        if file_size <= 0:
            errors.append(f"Empty icon file (0 bytes): {filename}")
            continue

        try:
            with Image.open(file_path) as img:
                # Check format
                if img.format != specs["format"]:
                    errors.append(f"{filename} wrong format: expected {specs['format']}, got {img.format}")

                # Check dimensions / sizes
                if specs["format"] == "ICO":
                    # Check ICO sizes
                    sizes = getattr(img, 'info', {}).get('sizes', set())
                    if not sizes or not specs["sizes"].issubset(sizes):
                        errors.append(f"favicon.ico missing expected resolutions: expected {specs['sizes']}, got {sizes}")
                    else:
                        print(f"  ✓ {filename}: ICO format valid, resolutions {sizes}, {file_size} bytes")
                else:
                    if img.size != specs["size"]:
                        errors.append(f"{filename} wrong size: expected {specs['size']}, got {img.size}")
                    else:
                        print(f"  ✓ {filename}: {img.format} {img.size[0]}x{img.size[1]}, {file_size} bytes")
        except Exception as e:
            errors.append(f"Error opening image {filename}: {e}")

    # 3. Audit site.webmanifest
    print("\n[3] Checking site.webmanifest...")
    manifest_path = PROJECT_ROOT / "site.webmanifest"
    if not manifest_path.exists():
        errors.append("site.webmanifest is missing!")
    else:
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest_data = json.load(f)
            
            # Check required fields
            req_fields = ["name", "short_name", "start_url", "display", "background_color", "theme_color", "icons"]
            for rf in req_fields:
                if rf not in manifest_data:
                    errors.append(f"site.webmanifest missing field: {rf}")

            # Check icons in manifest
            icons = manifest_data.get("icons", [])
            if len(icons) < 4:
                errors.append(f"site.webmanifest expected at least 4 icons, found {len(icons)}")

            for ic in icons:
                src = ic.get("src", "")
                rel_icon = src.lstrip("/")
                icon_file = PROJECT_ROOT / rel_icon
                if not icon_file.exists():
                    errors.append(f"Manifest icon '{src}' does not exist on disk at {icon_file}")
                else:
                    print(f"  ✓ Manifest icon verified: {src} ({ic.get('sizes')}, {ic.get('purpose')})")
            
            print(f"  ✓ site.webmanifest is valid JSON with short_name='{manifest_data.get('short_name')}', theme_color='{manifest_data.get('theme_color')}'")
        except Exception as e:
            errors.append(f"Failed to parse site.webmanifest: {e}")

    # 4. Audit 41 HTML Files for Icon Tags & Old Tag Absence
    print("\n[4] Checking All 41 HTML Pages for Favicon & App Icon Tags...")
    html_files = [p for p in PROJECT_ROOT.rglob("*.html") if ".git" not in p.parts]
    print(f"  Found {len(html_files)} HTML files to audit.")

    required_snippets = [
        '<!-- Official Nhu Y Driver Favicon -->',
        '<link rel="icon" href="/favicon.ico" sizes="any">',
        '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">',
        '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">',
        '<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">',
        '<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">',
        '<!-- Apple Devices -->',
        '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">',
        '<!-- Android & PWA -->',
        '<link rel="manifest" href="/site.webmanifest">',
        '<!-- Browser Theme -->',
        '<meta name="application-name" content="Như Ý Driver">',
        '<meta name="apple-mobile-web-app-title" content="Như Ý Driver">',
        '<meta name="theme-color" content="#c32932">',
        '<meta name="msapplication-TileColor" content="#c32932">',
        '<meta name="msapplication-TileImage" content="/mstile-150x150.png">'
    ]

    forbidden_snippets = [
        '<link rel="icon" type="image/webp" href="/assets/images/logo.webp">',
        '<link rel="apple-touch-icon" href="/assets/images/logo.webp">',
        '<meta name="theme-color" content="#0B1730">'
    ]

    html_pass_count = 0
    for hf in html_files:
        content = hf.read_text(encoding="utf-8")
        rel_path = hf.relative_to(PROJECT_ROOT)

        # Check required snippets
        missing = [snip for snip in required_snippets if snip not in content]
        if missing:
            errors.append(f"File {rel_path} is missing {len(missing)} required icon tags: {missing[0]}...")

        # Check forbidden snippets
        found_forbidden = [f_snip for f_snip in forbidden_snippets if f_snip in content]
        if found_forbidden:
            errors.append(f"File {rel_path} contains forbidden obsolete tags: {found_forbidden}")

        if not missing and not found_forbidden:
            html_pass_count += 1

    print(f"  ✓ {html_pass_count}/{len(html_files)} HTML pages passed all icon tag audits perfectly.")

    # 5. Audit robots.txt for Google Favicon bot compliance
    print("\n[5] Checking robots.txt for Favicon Accessibility...")
    robots_file = PROJECT_ROOT / "robots.txt"
    if robots_file.exists():
        robots_content = robots_file.read_text(encoding="utf-8")
        if "Disallow: /favicon" in robots_content or "Disallow: /android" in robots_content:
            errors.append("robots.txt blocks favicon indexing!")
        else:
            print("  ✓ robots.txt allows search crawlers full access to root favicons.")
    else:
        errors.append("robots.txt missing!")

    print("\n" + "=" * 60)
    if errors:
        print(f"AUDIT FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  ❌ {err}")
        sys.exit(1)
    else:
        print("ALL FAVICON & APP ICON AUDIT CHECKS PASSED PERFECTLY (100%)!")
        print("=" * 60)

if __name__ == "__main__":
    run_audit()

