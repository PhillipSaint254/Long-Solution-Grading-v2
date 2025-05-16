from ten import get_html_ny
import re

html_ny = get_html_ny()
for m in re.finditer(r'\$\d+', html_ny):
    if int(m.group()[1:]) < 100:  # choose small numbers
        start = max(m.start()-40, 0)
        print(html_ny[start:m.start()+40])
        break
