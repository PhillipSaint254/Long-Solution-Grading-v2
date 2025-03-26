import requests

resp = requests.get('https://www.youtube.com/watch?v=5D86_ptqd8I')
print(resp.status_code)
print(len(resp.text))
print(resp.text[:1000])
