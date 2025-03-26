import requests

resp = requests.get('https://pipedapi.kavin.rocks/streams/5D86_ptqd8I')
print(resp.status_code)
data=resp.json()
print(data.keys())
print(data['likes'], data['dislikes'])
# check if views present
print('views' in data, data.get('views'))
