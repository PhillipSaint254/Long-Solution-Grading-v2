from _six import get_html_ny
import re

html_ny = get_html_ny()
print(re.findall(r'/cars-api/[^"]+', html_ny)[:10])
