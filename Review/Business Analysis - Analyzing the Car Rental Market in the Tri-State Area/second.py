from first import get_r
import re

def get_pattern():
    r = get_r()
    return re.findall(r'\$[0-9]+', r.text)

if __name__ == "__main__":
    pattern = get_pattern()
    print(pattern[:20])
