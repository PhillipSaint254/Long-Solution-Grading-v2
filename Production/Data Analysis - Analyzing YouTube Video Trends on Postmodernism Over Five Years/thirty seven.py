import requests, datetime
from .thirty_one import fetch_stats

videos=[]
for p in [1,3,4]:
    resp = requests.get('https://pipedapi.kavin.rocks/search', params={'q':'postmodernism','page':p,'filter':'videos'})
    data=resp.json()
    for item in data['items']:
        vid = item['url'].split('v=')[-1]
        uploaded_ms = item.get('uploaded')
        year = datetime.utcfromtimestamp(uploaded_ms/1000.0).year if uploaded_ms else None
        videos.append({
            'id': vid,
            'title': item['title'],
            'views': item['views'],
            'uploaded_ms': uploaded_ms,
            'year': year
        })

# filter by years 2020-2024
recent = [v for v in videos if v['year'] and 2020 <= v['year'] <= 2024]

unique_ids = {}
for v in recent:
    vid = v['id']
    if vid not in unique_ids:
        unique_ids[vid] = v

print(len(unique_ids))

stats_list = []
for vid, v in unique_ids.items():
    s = fetch_stats(vid)
    if s is None:
        print(f"Failed for {vid} ({v['title']})")
        continue
    if 'published' in s:
        year = int(s['published'].split('.')[0])
    else:
        year = v['year']
    stats_list.append({
        'id': vid,
        'title': v['title'],
        'year': year,
        'views': s.get('views'),
        'likes': s.get('likes'),
        'comments': s.get('comments')
    })
    print(vid, year, s)

print(len(stats_list))
