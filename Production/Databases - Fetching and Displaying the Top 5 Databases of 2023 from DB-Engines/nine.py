import requests
from bs4 import BeautifulSoup

URL = 'https://db-engines.com/en/ranking?date=2023-12-01'

resp = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
print(f"Response: {resp.text}")
soup = BeautifulSoup(resp.text, 'html.parser')

# find the main ranking table and take the first 5 rows
table = soup.find('table', {'class': 'body'}).tbody
table = soup.find("table")
top5 = []
print(f"Table: {table}")
for row in table.find_all('tr')[:5]:
    cells = row.find_all('td')
    rank = cells[0].text.strip()
    name = cells[1].text.strip()
    score = cells[3].text.strip()   # score column
    top5.append((rank, name, score))

# display results
for r, name, score in top5:
    print(f"{r}. {name} — Score: {score}")
