import requests, re
response = requests.get("https://www.yelp.com/biz/la-parisienne-new-york-5")
print(response.status_code)
