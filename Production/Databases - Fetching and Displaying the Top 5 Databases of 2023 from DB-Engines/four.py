import requests

# Fetch the DB-Engines rank for a 2023 date (December 2023)
url = 'https://db-engines.com/en/ranking'
params = {'date': '2023-12-01'}
headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get(url, params=params, headers=headers)
print(resp.status_code, len(resp.text))
# Let's check a snippet
print(resp.text[:500])
