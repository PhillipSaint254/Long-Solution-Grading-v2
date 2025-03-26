import requests

headers = {'User-Agent': 'Mozilla/5.0'}
resp = requests.get('https://socialcounts.org/api/youtube-video', params={'id':'5D86_ptqd8I'}, headers=headers)
print(resp.status_code)
print(resp.headers.get('content-type'))
print(resp.text[:200])
