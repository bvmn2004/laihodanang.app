import os
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://laihodanang.app"

pages = [
    # Main pages
    {"url": "/", "priority": "1.0", "changefreq": "daily"},
    {"url": "/gioi-thieu/", "priority": "0.8", "changefreq": "monthly"},
    {"url": "/bang-gia/", "priority": "0.95", "changefreq": "weekly"},
    {"url": "/dich-vu/", "priority": "0.9", "changefreq": "weekly"},
    {"url": "/khu-vuc/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/lien-he/", "priority": "0.85", "changefreq": "monthly"},
    {"url": "/blog/", "priority": "0.85", "changefreq": "daily"},
    
    # Services
    {"url": "/dich-vu/lai-xe-ho-o-to/", "priority": "0.9", "changefreq": "weekly"},
    {"url": "/dich-vu/lai-xe-ho-xe-may/", "priority": "0.9", "changefreq": "weekly"},
    {"url": "/dich-vu/ban-uong-toi-lai/", "priority": "0.9", "changefreq": "weekly"},
    {"url": "/dich-vu/lai-xe-ho-sau-tiec/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/dich-vu/thue-tai-xe-theo-gio/", "priority": "0.8", "changefreq": "weekly"},
    {"url": "/dich-vu/thue-tai-xe-theo-ngay/", "priority": "0.8", "changefreq": "weekly"},
    {"url": "/dich-vu/thue-tai-xe-di-tinh/", "priority": "0.8", "changefreq": "weekly"},
    {"url": "/dich-vu/thue-tai-xe-dua-don-doi-tac/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/dich-vu/thue-tai-xe-tiec-cuoi-su-kien/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/dich-vu/thue-tai-xe-giao-nhan-xe/", "priority": "0.7", "changefreq": "monthly"},
    
    # Local & Routes
    {"url": "/khu-vuc/hai-chau/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/thanh-khe/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/son-tra/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/ngu-hanh-son/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/lien-chieu/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/cam-le/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/hoa-vang/", "priority": "0.85", "changefreq": "weekly"},
    {"url": "/khu-vuc/da-nang-di-hoi-an/", "priority": "0.8", "changefreq": "weekly"},
    {"url": "/khu-vuc/da-nang-di-hue/", "priority": "0.8", "changefreq": "weekly"},
    {"url": "/khu-vuc/da-nang-di-quang-ngai/", "priority": "0.75", "changefreq": "weekly"},

    # Blog posts
    {"url": "/blog/lai-xe-ho-la-gi/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/lai-xe-ho-va-taxi-nen-chon-gi/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/khi-nao-nen-goi-tai-xe-lai-ho/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/quy-trinh-dat-tai-xe-nhu-y-driver/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/chuan-bi-khi-ban-giao-xe/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/dat-tai-xe-lai-ho-ban-dem/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/buon-ngu-khi-lai-xe/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/uong-ruou-bia-mang-theo-xe-may/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/di-tiec-bang-o-to-da-nang/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/thue-tai-xe-theo-gio-hay-theo-ngay/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/thue-xe-tu-lai-goi-tai-xe/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/thue-tai-xe-da-nang-di-hoi-an/", "priority": "0.75", "changefreq": "monthly"},
    {"url": "/blog/thue-tai-xe-da-nang-di-hue/", "priority": "0.75", "changefreq": "monthly"}
]

now_str = "2026-10-30"

sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for p in pages:
    sitemap_xml.append('  <url>')
    sitemap_xml.append(f'    <loc>{BASE_URL}{p["url"]}</loc>')
    sitemap_xml.append(f'    <lastmod>{now_str}</lastmod>')
    sitemap_xml.append(f'    <changefreq>{p["changefreq"]}</changefreq>')
    sitemap_xml.append(f'    <priority>{p["priority"]}</priority>')
    sitemap_xml.append('  </url>')
sitemap_xml.append('</urlset>')

with open(PROJECT_ROOT / "sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))
print(f"Generated sitemap.xml with {len(pages)} URLs")

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

with open(PROJECT_ROOT / "robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("Generated robots.txt")

with open(PROJECT_ROOT / "CNAME", "w", encoding="utf-8") as f:
    f.write("laihodanang.app\n")
print("Generated CNAME (laihodanang.app)")

# GitHub Pages .nojekyll to prevent Jekyll from skipping static asset folders
(PROJECT_ROOT / ".nojekyll").touch(exist_ok=True)
print("Created .nojekyll for GitHub Pages")

