import requests
from bs4 import BeautifulSoup

url = 'https://db-engines--com.zipv6.dsjfzj.nanning.gov.cn/en/ranking'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
print(resp.status_code, len(resp.text))
print(resp.text[:200])
