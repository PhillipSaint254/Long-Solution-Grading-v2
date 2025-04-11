import requests

response = requests.get("https://yelpapi.doordash.com/v3/businesses/la-parisienne-new-york-5")
print(response.status_code)
