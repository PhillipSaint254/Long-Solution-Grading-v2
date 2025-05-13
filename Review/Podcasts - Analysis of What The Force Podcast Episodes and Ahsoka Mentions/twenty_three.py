from twenty_two import get_text
import re

def get_matches():
    text = get_text()
    return list(re.finditer(r'(?i)ahsoka', text))

if __name__ == "__main__":
    matches = get_matches()
    print(len(matches), matches[:5])
    