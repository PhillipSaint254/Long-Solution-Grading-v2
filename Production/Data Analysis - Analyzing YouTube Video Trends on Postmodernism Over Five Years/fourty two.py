import requests, datetime

videos2023=[]
for p in [1,3,4]:
    resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':p,'filter':'videos'})
    data=resp.json()
    for item in data['items']:
        vid = item['url'].split('v=')[-1]
        uploaded_ms = item.get('uploaded')
        if not uploaded_ms:
            continue
        year = datetime.utcfromtimestamp(uploaded_ms/1000.0).year
        if year == 2023:
            videos2023.append((vid, item['title'], year))

print(videos2023)
