import requests
from five import get_headers

headers = get_headers()
response = requests.get("https://m.yelp.com/biz/la-parisienne-new-york-5", headers=headers)
print(response.status_code)
