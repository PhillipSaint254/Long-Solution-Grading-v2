from ten import get_html_ny
import re

html_ny = get_html_ny()
print(re.findall(r'\$\d+', html_ny)[:10])
