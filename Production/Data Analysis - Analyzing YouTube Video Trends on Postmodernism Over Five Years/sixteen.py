import requests

resp = requests.get('https://invidious.fdn.fr/api/v1/search', params={'q':'postmodernism', 'page':1})
print(resp.status_code, resp.headers.get('content-type'))
print(resp.text[:200])
