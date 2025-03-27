import requests

# Let's fetch page 1 (we did) and look for those with year 2023
resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':1,'filter':'videos'})
data=resp.json()
from datetime import datetime

videos2023=[]
for item in data['items']:
    vid = item['url'].split('v=')[-1]
    uploaded_ms = item.get('uploaded')
    if not uploaded_ms:
        continue
    year = datetime.utcfromtimestamp(uploaded_ms/1000.0).year
    if year == 2023:
        videos2023.append((vid, item['title'], year))

print(videos2023)
