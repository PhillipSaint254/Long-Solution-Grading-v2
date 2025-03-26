import requests

resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':1,'filter':'videos'})
print(resp.status_code)
print(resp.text[:100])
