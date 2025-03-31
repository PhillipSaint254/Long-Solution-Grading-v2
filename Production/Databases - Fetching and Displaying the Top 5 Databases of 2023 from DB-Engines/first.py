import requests

url = 'http://web.archive.org/cdx/search/cdx'
params = {
    'url': 'https://db-engines.com/en/ranking',
    'output': 'json',
    'from': '2023',
    'to': '2023',
    'filter': 'statuscode:200',
    'collapse': 'digest',
    'limit': '10'
}
resp = requests.get(url, params=params)
print(resp.status_code, resp.headers.get('Content-Type'), resp.text[:200])
