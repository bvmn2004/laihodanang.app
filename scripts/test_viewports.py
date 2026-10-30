import os
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "research", "screenshots"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

VIEWPORTS = [
    (320, 640, "mobile_320"),
    (375, 667, "mobile_375"),
    (390, 844, "mobile_390"),
    (430, 932, "mobile_430"),
    (768, 1024, "tablet_768"),
    (820, 1180, "tablet_820"),
    (1024, 768, "laptop_1024"),
    (1280, 800, "laptop_1280"),
    (1366, 768, "laptop_1366"),
    (1440, 900, "desktop_1440"),
    (1920, 1080, "desktop_1920"),
]

def capture_screenshots():
    print(f"Testing responsive layouts across {len(VIEWPORTS)} viewports...")
    print(f"Using Edge binary: {EDGE_PATH}")
    print(f"Saving screenshots to: {OUTPUT_DIR}")

    success_count = 0
    for w, h, name in VIEWPORTS:
        out_file = os.path.join(OUTPUT_DIR, f"{name}.png")
        cmd = [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            f"--window-size={w},{h}",
            f"--screenshot={out_file}",
            "http://localhost:8080/"
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, timeout=15)
            if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
                print(f"  ✓ [{w}x{h}] {name}.png captured ({os.path.getsize(out_file)//1024} KB)")
                success_count += 1
            else:
                print(f"  ✗ [{w}x{h}] {name}.png failed or empty")
        except Exception as e:
            print(f"  ✗ [{w}x{h}] Error: {e}")

    print(f"\nCaptured {success_count}/{len(VIEWPORTS)} screenshots successfully.")

if __name__ == '__main__':
    capture_screenshots()

