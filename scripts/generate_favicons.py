import os
import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_LOGO = PROJECT_ROOT / "assets" / "images" / "logo.png"

if not SRC_LOGO.exists():
    print(f"ERROR: Source logo not found at {SRC_LOGO}")
    sys.exit(1)

print(f"Reading source logo: {SRC_LOGO}")
with Image.open(SRC_LOGO) as img:
    # Ensure RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
    orig_w, orig_h = img.size
    print(f"Original logo dimensions: {orig_w}x{orig_h}")

    # 1. Standard PNG favicons (16, 32, 48, 96)
    standard_png_sizes = [
        ("favicon-16x16.png", 16),
        ("favicon-32x32.png", 32),
        ("favicon-48x48.png", 48),
        ("favicon-96x96.png", 96),
    ]

    for fname, sz in standard_png_sizes:
        out_path = PROJECT_ROOT / fname
        resized = img.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(out_path, format="PNG", optimize=True)
        print(f"✓ Created {fname} ({sz}x{sz}, {out_path.stat().st_size} bytes)")

    # 2. favicon.ico with multi-resolution (16, 32, 48)
    ico_path = PROJECT_ROOT / "favicon.ico"
    # To ensure highest quality in ICO, resize specifically for each size
    ico_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    ico_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    ico_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
    
    # Save as multi-resolution ICO
    ico_48.save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[ico_16, ico_32]
    )
    print(f"✓ Created favicon.ico (16, 32, 48px, {ico_path.stat().st_size} bytes)")

    # 3. Apple Touch Icon (180x180)
    # Give slight padding (logo scaled to 160x160 on 180x180 white canvas) to protect against iOS squircle mask
    apple_size = 180
    apple_inner = 160
    apple_canvas = Image.new("RGB", (apple_size, apple_size), (255, 255, 255))
    apple_logo = img.resize((apple_inner, apple_inner), Image.Resampling.LANCZOS)
    offset = (apple_size - apple_inner) // 2
    apple_canvas.paste(apple_logo, (offset, offset))
    apple_path = PROJECT_ROOT / "apple-touch-icon.png"
    apple_canvas.save(apple_path, format="PNG", optimize=True)
    print(f"✓ Created apple-touch-icon.png ({apple_size}x{apple_size}, {apple_path.stat().st_size} bytes)")

    # 4. Android Chrome icons (192x192, 512x512) - standard (purpose: any)
    android_sizes = [
        ("android-chrome-192x192.png", 192, 172),
        ("android-chrome-512x512.png", 512, 460),
    ]
    for fname, sz, inner_sz in android_sizes:
        canvas = Image.new("RGB", (sz, sz), (255, 255, 255))
        resized_logo = img.resize((inner_sz, inner_sz), Image.Resampling.LANCZOS)
        offset = (sz - inner_sz) // 2
        canvas.paste(resized_logo, (offset, offset))
        out_path = PROJECT_ROOT / fname
        canvas.save(out_path, format="PNG", optimize=True)
        print(f"✓ Created {fname} ({sz}x{sz}, {out_path.stat().st_size} bytes)")

    # 5. Maskable Icons (192x192, 512x512) - purpose: maskable
    # Safe zone: central circle of diameter 80% (i.e. 10% margin on all 4 sides)
    # For 192x192: 80% = 153.6 -> use 148px (inner margin 22px)
    # For 512x512: 80% = 409.6 -> use 396px (inner margin 58px)
    maskable_sizes = [
        ("icon-maskable-192x192.png", 192, 148),
        ("icon-maskable-512x512.png", 512, 396),
    ]
    for fname, sz, inner_sz in maskable_sizes:
        canvas = Image.new("RGB", (sz, sz), (255, 255, 255))
        resized_logo = img.resize((inner_sz, inner_sz), Image.Resampling.LANCZOS)
        offset = (sz - inner_sz) // 2
        canvas.paste(resized_logo, (offset, offset))
        out_path = PROJECT_ROOT / fname
        canvas.save(out_path, format="PNG", optimize=True)
        print(f"✓ Created {fname} ({sz}x{sz}, safe-zone inner {inner_sz}px, {out_path.stat().st_size} bytes)")

    # 6. Windows mstile (150x150)
    mstile_size = 150
    mstile_inner = 130
    mstile_canvas = Image.new("RGB", (mstile_size, mstile_size), (255, 255, 255))
    mstile_logo = img.resize((mstile_inner, mstile_inner), Image.Resampling.LANCZOS)
    offset = (mstile_size - mstile_inner) // 2
    mstile_canvas.paste(mstile_logo, (offset, offset))
    mstile_path = PROJECT_ROOT / "mstile-150x150.png"
    mstile_canvas.save(mstile_path, format="PNG", optimize=True)
    print(f"✓ Created mstile-150x150.png ({mstile_size}x{mstile_size}, {mstile_path.stat().st_size} bytes)")

print("\nAll 11 icon files generated successfully from assets/images/logo.png!")

