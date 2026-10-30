import glob
import re

for f in sorted(glob.glob('scripts/*.py')):
    c = open(f, encoding='utf-8').read()
    matches = set(re.findall(r'class=[\'"][^\'"]*card[^\'"]*[\'"]', c))
    if matches:
        print(f, matches)

