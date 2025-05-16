from first import get_r
import re

r = get_r()
print(re.findall(r'"price":\s*([0-9]+)', r.text)[:10])
