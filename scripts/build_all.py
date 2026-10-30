import sys
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

scripts = [
    "scripts/generate_favicons.py",
    "scripts/generate_home.py",
    "scripts/generate_main_pages.py",
    "scripts/generate_services.py",
    "scripts/generate_locations.py",
    "scripts/generate_blog.py",
    "scripts/generate_seo_assets.py"
]

print("Starting full site rebuild...")
for s in scripts:
    script_path = PROJECT_ROOT / s
    res = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"FAILED running {s}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"✓ {s} completed successfully.")

print("All pages and assets rebuilt successfully!")

