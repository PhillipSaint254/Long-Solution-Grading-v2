import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}
resp = requests.get('https://db-engines.com/en/ranking', headers=headers, timeout=30)
print(resp.status_code, resp.text[:200])
