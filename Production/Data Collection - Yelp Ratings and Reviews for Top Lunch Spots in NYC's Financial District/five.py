import requests

def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
    }

if __name__ == "__main__":
    headers = get_headers()
    response = requests.get("https://www.yelp.com/biz/la-parisienne-new-york-5", headers=headers)
    print(response.status_code)
