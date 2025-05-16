import requests

def get_url_params():
    return 'https://api.duckduckgo.com/', params = {'q': 'site:forbes.com intitle:"coupon redemption"', 'format': 'json'}

def get_resp():
    url, params = get_url_params()    
    return requests.get(url, params=params)

if __name__ == "__main__":
    resp = get_resp()
    print(resp.status_code, resp.headers.get('content-type')[:50], resp.text[:200])
    