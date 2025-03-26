import requests

resp = requests.get('https://invidious.privacyredirect.com/api/v1/search', params={'q':'postmodernism','page':1})
print(resp.status_code)
print(resp.headers.get('content-type'))
print(resp.text[:200])
