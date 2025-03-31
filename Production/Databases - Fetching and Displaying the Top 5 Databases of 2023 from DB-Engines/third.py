import requests

params = {
    'url': 'https://db-engines.com/en/ranking',
    'output': 'json',
    'from': '2023',
    'to': '2023',
    'filter': 'statuscode:200',
    'collapse': 'digest',
    'limit': '10'
}
url = 'https://web.archive.org/cdx/search/cdx'

headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get(url, params=params, headers=headers)
print(resp.status_code, resp.text[:200])
