import re
from first import get_r

r = get_r()
m = re.search(r'apolloState":\s*({.*?})\s*};', r.text)
if m:
    print("found")
