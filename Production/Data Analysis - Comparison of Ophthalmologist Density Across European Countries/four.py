from bs4 import BeautifulSoup
import requests

url = 'https://icoph.org/advocacy/data-on-ophthalmologists-worldwide/'
resp = requests.get(url)
print(resp.status_code, resp.headers.get('Content-Type')[:50])

soup = BeautifulSoup(resp.text, 'html.parser')
# find the table with this header
table = soup.find('table')

data = []
for row in table.find_all('tr')[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
    # sometimes we get empty rows
    if cells:
        data.append(cells)
        
print(data[:5])
