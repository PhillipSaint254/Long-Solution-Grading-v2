import requests

resp = requests.get('https://socialcounts.org/api/youtube-video', params={'id':'5D86_ptqd8I'})
print(resp.status_code, resp.headers.get('content-type'))
print(resp.text[:200])
