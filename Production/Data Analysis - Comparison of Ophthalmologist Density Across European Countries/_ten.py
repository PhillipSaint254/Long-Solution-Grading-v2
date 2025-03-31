from bs4 import BeautifulSoup
import requests

def get_data():
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
    return data

if __name__ == "__main__":
    data = get_data()
    print(f"Data: {data}")
    # Look for "Russian" in countries
    # print([r for r in data if 'Russia' in r[0]])
    