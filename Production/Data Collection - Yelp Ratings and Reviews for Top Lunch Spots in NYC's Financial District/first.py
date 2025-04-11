import requests, re

def get_response():
    return requests.get("https://www.yelp.com/biz/la-parisienne-new-york-5")

if __name__ == "__main__":
    response = get_response()
    print(response.status_code)
