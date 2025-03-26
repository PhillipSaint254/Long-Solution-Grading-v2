import requests

for p in range(1,6):
    resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':p,'filter':'videos'})
    print(p, resp.status_code, len(resp.text))
    if resp.status_code != 200:
        print(resp.text[:200])
    else:
        data = resp.json()
        print('Items:', len(data['items']))
