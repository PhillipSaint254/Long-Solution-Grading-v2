import requests, json

turo_api = "https://turo.com/api/vehicles?country=US&region=NY"
r = requests.get(turo_api)
print(r.status_code)
