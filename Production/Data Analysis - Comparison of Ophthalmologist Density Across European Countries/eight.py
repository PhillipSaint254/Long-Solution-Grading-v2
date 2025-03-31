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
        
# Define a list of European countries per above
europe_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 
    'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino',
    'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 
    'Ukraine', 'United Kingdom', 'Vatican City'
]

# Now filter
europe_data = [row for row in data if row[0] in europe_countries]
print(len(europe_data), europe_data[:5])
