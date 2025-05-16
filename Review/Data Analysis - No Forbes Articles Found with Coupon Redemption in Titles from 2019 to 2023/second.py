import requests 
from first import get_url_params

def get_resp():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url, params = get_url_params()
    return requests.get(url, params=params, headers=headers)

if __name__ == "__main__":
    resp = get_resp()
    print(resp.status_code, resp.headers.get('content-type'), resp.text[:200])

