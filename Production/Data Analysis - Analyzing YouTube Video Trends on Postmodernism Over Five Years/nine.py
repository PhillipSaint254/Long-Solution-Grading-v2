import requests

resp = requests.get('https://pipedapi.kavin.rocks/video', params={'id':'5D86_ptqd8I'})
data = resp.json()
print(data.keys())
print(data['title'], data['views'], data['likes'], data['comments'])  # erroneous
