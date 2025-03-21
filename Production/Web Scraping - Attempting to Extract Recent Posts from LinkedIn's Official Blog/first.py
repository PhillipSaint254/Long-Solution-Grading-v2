import requests

resp = requests.get('https://blog.linkedin.com/feed', headers={'User-Agent':'Mozilla/5.0'})
print(resp.status_code)
print(resp.headers.get('content-type'))
print(resp.text[:200])
