import requests

resp = requests.get('https://pipedapi.in.projectsegfau.lt/video', params={'id':'5D86_ptqd8I'})
print(resp.status_code)
print(resp.headers.get('content-type'))
print(resp.text[:200])
