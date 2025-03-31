from bs4 import BeautifulSoup
import requests

def get_countries():
    return [
        'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
        'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 
        'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
        'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania',
        'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
        'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino',
        'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 
        'Ukraine', 'United Kingdom', 'Vatican City'
    ]
        
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
    