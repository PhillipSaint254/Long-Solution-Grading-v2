import requests
from bs4 import BeautifulSoup

url = 'https://db-engines.com/en/ranking'
params = {'date': '2023-12-01'}
headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get(url, params=params, headers=headers, timeout=30)
print(resp.status_code, len(resp.text))
# If status code not 200, print text.

print(resp.text[:100])
