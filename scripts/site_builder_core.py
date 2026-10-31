import os
import sys
import json
from pathlib import Path
from site_components import (
    BASE_URL, BRAND_NAME, HOTLINE, HOTLINE_TEL, ZALO_URL,
    FACEBOOK_URL, EMAIL, AREA, picture_tag, get_header, get_footer, render_breadcrumbs
)

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def render_page_shell(path, title, meta_desc, h1, body_content, og_image="/assets/images/02_Lai_Xe_Ho_Da_Nang_24_7.webp", schemas=None, is_article=False):
    canonical_url = f"{BASE_URL}{path}"
    og_img_url = f"{BASE_URL}{og_image}" if not og_image.startswith("http") else og_image
    
    # Base LocalBusiness Schema
    base_schemas = [{
        "@context": "https://schema.org",
        "@type": "AutomotiveBusiness",
        "@id": f"{BASE_URL}/#business",
        "name": BRAND_NAME,
        "alternateName": "Như Ý Driver",
        "url": BASE_URL,
        "logo": f"{BASE_URL}/assets/images/logo.webp",
        "image": f"{BASE_URL}/assets/images/15_Doi_Ngu_Tai_Xe_Nhu_Y_Driver.webp",
        "telephone": HOTLINE,
        "email": EMAIL,
        "priceRange": "Từ 110.000đ",
        "currenciesAccepted": "VND",
        "paymentAccepted": "Cash, Bank Transfer",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Đà Nẵng",
            "addressRegion": "Đà Nẵng",
            "addressCountry": "VN"
        },
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Đà Nẵng"},
            {"@type": "AdministrativeArea", "name": "Hải Châu"},
            {"@type": "AdministrativeArea", "name": "Sơn Trà"},
            {"@type": "AdministrativeArea", "name": "Thanh Khê"},
            {"@type": "AdministrativeArea", "name": "Ngũ Hành Sơn"},
            {"@type": "AdministrativeArea", "name": "Liên Chiểu"},
            {"@type": "AdministrativeArea", "name": "Cẩm Lệ"},
            {"@type": "AdministrativeArea", "name": "Hòa Vang"},
            {"@type": "AdministrativeArea", "name": "Hội An"},
            {"@type": "AdministrativeArea", "name": "Huế"}
        ],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        },
        "sameAs": [
            FACEBOOK_URL
        ]
    }]

    if schemas:
        base_schemas.extend(schemas)

    schema_json_ld = "\n".join([f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False, indent=2)}</script>' for s in base_schemas])

    header_html = get_header(path)
    footer_html = get_footer()

    is_404 = (path == "/404.html" or path == "404.html" or path == "/404/")
    robots_content = "noindex, nofollow" if is_404 else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">' if not is_404 else ''

    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  {canonical_tag}
  <meta name="robots" content="{robots_content}">

  <!-- Open Graph -->
  <meta property="og:locale" content="vi_VN">
  <meta property="og:type" content="{'article' if is_article else 'website'}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="{BRAND_NAME}">
  <meta property="og:image" content="{og_img_url}">
  <meta property="og:image:width" content="1536">
  <meta property="og:image:height" content="1024">
  <meta property="og:image:alt" content="{title}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="{og_img_url}">

  <!-- Official Nhu Y Driver Favicon -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">

  <!-- Apple Devices -->
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

  <!-- Android & PWA -->
  <link rel="manifest" href="/site.webmanifest">

  <!-- Browser Theme -->
  <meta name="application-name" content="Như Ý Driver">
  <meta name="apple-mobile-web-app-title" content="Như Ý Driver">
  <meta name="theme-color" content="#c32932">
  <meta name="msapplication-TileColor" content="#c32932">
  <meta name="msapplication-TileImage" content="/mstile-150x150.png">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="/assets/css/style.css">

  <!-- Structured Data -->
  {schema_json_ld}
</head>
<body>
  {header_html}

  <main id="main-content">
    {body_content}
  </main>

  {footer_html}

  <!-- Scripts -->
  <script src="/assets/js/main.js" defer></script>

  <!-- 100% privacy-first analytics -->
  <script data-collect-dnt="true" data-detect-404="true" async src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
</body>
</html>'''

def write_html(rel_path, content):
    full_path = PROJECT_ROOT / rel_path
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {rel_path}")

print("Site builder core loaded.")

