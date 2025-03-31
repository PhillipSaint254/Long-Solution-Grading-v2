from bs4 import BeautifulSoup
import requests

url = 'https://icoph.org/advocacy/data-on-ophthalmologists-worldwide/'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
# find the table with this header
table = soup.find('table')

# Extract headers
headers = [th.get_text(strip=True) for th in table.find_all('th')]
print(headers)
