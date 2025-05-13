from twenty_three import get_text, get_matches

matches = get_matches()
text = get_text()
for m in matches:
    snippet = text[m.start()-200:m.start()+200]
    print(snippet)
