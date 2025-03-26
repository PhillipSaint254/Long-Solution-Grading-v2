import requests

resp = requests.get('https://pipedapi.inventaire.io/video', params={'id':'5D86_ptqd8I'})
print(resp.status_code)
print(resp.text[:200])
