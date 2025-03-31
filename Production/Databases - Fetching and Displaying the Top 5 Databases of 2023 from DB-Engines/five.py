import requests

headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get('https://db-engines.com/en/ranking', headers=headers)
print(resp.status_code, resp.text[:100])
