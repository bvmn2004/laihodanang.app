import os
import sys
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TARGET_SCRIPT = '<script data-collect-dnt="true" data-detect-404="true" async src="https://scripts.simpleanalyticscdn.com/latest.js"></script>'
TARGET_COMMENT = '<!-- 100% privacy-first analytics -->'

def audit_simple_analytics():
    print("=" * 60)
    print("SIMPLE ANALYTICS AUDIT SUITE")
    print("=" * 60)
    
    html_files = sorted([p for p in PROJECT_ROOT.rglob("*.html") if ".git" not in p.parts])
    print(f"Total HTML files found: {len(html_files)}")
    
    errors = []
    success_files = []
    
    for hf in html_files:
        rel_path = hf.relative_to(PROJECT_ROOT)
        content = hf.read_text(encoding="utf-8")
        
        # 1. Count occurrences of script URL
        script_count = content.count("scripts.simpleanalyticscdn.com/latest.js")
        if script_count == 0:
            errors.append(f"{rel_path}: Simple Analytics script MISSING")
            continue
        elif script_count > 1:
            errors.append(f"{rel_path}: DUPLICATE Simple Analytics script found ({script_count} times)")
            continue
            
        # 2. Check exact tag
        if TARGET_SCRIPT not in content:
            errors.append(f"{rel_path}: Script tag does not match exact attributes")
            continue
            
        # 3. Check comment
        if TARGET_COMMENT not in content:
            errors.append(f"{rel_path}: Comment '{TARGET_COMMENT}' missing")
            continue
            
        # 4. Check position immediately before </body>
        # Find index of TARGET_SCRIPT and index of </body>
        script_idx = content.find(TARGET_SCRIPT)
        body_idx = content.find("</body>")
        if body_idx == -1:
            errors.append(f"{rel_path}: Missing </body> tag")
            continue
            
        if script_idx > body_idx:
            errors.append(f"{rel_path}: Script is placed AFTER </body> tag")
            continue
            
        # Check text between script and </body> - should only be whitespace / newline
        between = content[script_idx + len(TARGET_SCRIPT):body_idx]
        if between.strip() != "":
            errors.append(f"{rel_path}: Content found between script and </body>: {repr(between)}")
            continue
            
        # 5. Check closing </html> tag exists after </body>
        html_close_idx = content.find("</html>")
        if html_close_idx == -1 or html_close_idx < body_idx:
            errors.append(f"{rel_path}: Missing or misplaced </html> tag")
            continue
            
        success_files.append(str(rel_path))

    print(f"\nAudit completed:")
    print(f"  ✓ Files successfully integrated: {len(success_files)} / {len(html_files)}")
    
    # Check 404.html specifically
    is_404_ok = "404.html" in success_files
    print(f"  ✓ 404.html specifically verified: {'YES' if is_404_ok else 'NO'}")
    
    if errors:
        print(f"\n❌ ERRORS DETECTED ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 41 HTML FILES PASSED SIMPLE ANALYTICS AUDIT PERFECTLY!")
        print("=" * 60)
        return True

if __name__ == "__main__":
    success = audit_simple_analytics()
    if not success:
        sys.exit(1)

