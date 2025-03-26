import requests

resp = requests.get('https://api.invidious.io/instances')
print(resp.status_code, resp.headers.get('content-type'))
print(resp.text[:200])
