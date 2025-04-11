import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get("https://www.yelp.com/biz/la-parisienne-new-york-5", headers=headers)
print(response.status_code)