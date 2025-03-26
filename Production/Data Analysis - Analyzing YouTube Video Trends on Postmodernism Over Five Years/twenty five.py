import requests
from datetime import datetime

def get_videos(query, pages=3):
    results=[]
    for p in range(1, pages+1):
        resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':query,'page':p,'filter':'videos'})
        data=resp.json()
        for item in data['items']:
            vid = item['url'].split('v=')[-1]
            uploaded_ms = item['uploaded']  # maybe not present? but in the earlier we saw 'uploaded'
            # some items might not contain 'uploaded'
            year = None
            if uploaded_ms:
                dt = datetime.utcfromtimestamp(uploaded_ms/1000.0)
                year = dt.year
            results.append({
                'id': vid,
                'title': item['title'],
                'views': item['views'],
                'uploaded_ms': uploaded_ms,
                'year': year
            })
    return results

videos = get_videos('postmodernism', pages=5)
# filter years
recent = [v for v in videos if v['year'] and v['year'] >= 2020]  # past five years include 2020-2024
print(len(videos), len(recent), recent[:5])
