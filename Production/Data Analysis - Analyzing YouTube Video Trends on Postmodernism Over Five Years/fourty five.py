import requests, datetime

videos2023=[]
for p in range(1,21):
    try:
        resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':p,'filter':'videos'}, timeout=10)
        if resp.status_code != 200:
            continue
        data=resp.json()
        for item in data['items']:
            vid = item['url'].split('v=')[-1]
            uploaded_ms = item.get('uploaded')
            if not uploaded_ms:
                continue
            year = datetime.utcfromtimestamp(uploaded_ms/1000.0).year
            if year == 2023:
                videos2023.append((vid, item['title'], year))
    except Exception as e:
        continue

print(videos2023)
