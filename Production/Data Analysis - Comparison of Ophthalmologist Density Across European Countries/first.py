import requests

url = 'https://icoph.org/advocacy/data-on-ophthalmologists-worldwide/'
resp = requests.get(url)
print(resp.status_code, resp.headers.get('Content-Type')[:50])
