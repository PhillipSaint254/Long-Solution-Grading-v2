from bs4 import BeautifulSoup
import requests

url = 'https://icoph.org/advocacy/data-on-ophthalmologists-worldwide/'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
# find the table with this header
table = soup.find('table')

data = []
for row in table.find_all('tr')[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
    # sometimes we get empty rows
    if cells:
        data.append(cells)
        
# Get all country names
countries = [row[0] for row in data]
# Print a selection of those in Europe through manual check
europe_list = []
for name in countries:
    # detect known ones by manual list
    if name in ['Austria','Belgium']:
        europe_list.append(name)
print(europe_list)
