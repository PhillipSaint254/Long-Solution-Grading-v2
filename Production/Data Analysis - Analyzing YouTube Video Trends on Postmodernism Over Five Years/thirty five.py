import requests
from bs4 import BeautifulSoup

def fetch_stats(video_id):
    url = f'https://playboard.co/en/video/{video_id}'
    resp = requests.get(url, timeout=15)
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    info = {}
    # views
    view_el = soup.find(string=lambda s: s and 'views' in s)
    if view_el:
        # the string includes views and possibly number.
        import re
        m = re.search(r'([\d,]+)\s+views', view_el)
        if m:
            info['views'] = int(m.group(1).replace(',', ''))
    # published
    pub_el = soup.find(string=lambda s: s and 'Published' in s)
    if pub_el:
        m = re.search(r'Published\s+(\d{4}\.\d{2}\.\d{2})', pub_el)
        if m:
            info['published'] = m.group(1)
    # likes
    like_box = None
    for box in soup.select('.score__box'):
        title_el = box.find('h2')
        if title_el and title_el.text.strip() == 'Likes':
            like_box = box
            break
    if like_box:
        num = like_box.find(class_='score__num')
        if num:
            info['likes'] = int(num.text.replace(',',''))
    # comments
    com_box = None
    for box in soup.select('.score__box'):
        title_el = box.find('h2')
        if title_el and title_el.text.strip() == 'Comments':
            com_box = box
            break
    if com_box:
        num = com_box.find(class_='score__num')
        if num:
            info['comments'] = int(num.text.replace(',',''))
    return info

print(fetch_stats('5D86_ptqd8I'))
