import requests

resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':1,'filter':'videos'})
resp.status_code, resp.headers.get('content-type'), resp.text[:200]
