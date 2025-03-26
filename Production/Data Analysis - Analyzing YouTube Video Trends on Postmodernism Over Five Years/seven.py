import requests

resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'test','page':1,'filter':'videos'})
print(resp.status_code, resp.text[:100])
