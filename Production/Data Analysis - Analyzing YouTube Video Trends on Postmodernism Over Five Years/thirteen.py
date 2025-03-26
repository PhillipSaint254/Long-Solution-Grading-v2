import requests

resp = requests.get('https://pipedapi.kavin.rocks/video/5D86_ptqd8I')
print(resp.status_code)
print(resp.headers.get('content-type'))
print(resp.text[:200])
