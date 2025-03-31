from bs4 import BeautifulSoup
import requests

url = 'https://icoph.org/advocacy/data-on-ophthalmologists-worldwide/'
resp = requests.get(url)
print(resp.status_code, resp.headers.get('Content-Type')[:50])

soup = BeautifulSoup(resp.text, 'html.parser')
# find the table with this header
table = soup.find('table')
print(table is not None)
