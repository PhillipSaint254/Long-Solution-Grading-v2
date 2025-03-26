import requests

resp = requests.get('https://invidious.io/api/v1/instances')
print(resp.status_code, resp.headers.get('content-type'))
print(resp.text[:200])
