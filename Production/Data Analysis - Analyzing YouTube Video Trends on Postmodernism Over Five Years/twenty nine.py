import requests
from bs4 import BeautifulSoup

def fetch_stats(video_id):
    url = f'https://playboard.co/en/video/{video_id}'
    resp = requests.get(url, timeout=15)
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    # parse views
    # find element that contains text like ' views' and a preceding number
    # Might glean from the part containing a number and 'views', 'Published' etc.
    # Let's find Published date and views: perhaps in a block
    info = {}
    # find a span containing 'views' and then the preceding text (the number)
    # by scanning for any text that matches r'([\d,]+) views'
    import re
    match = re.search(r'([\d,]+)\s+views', resp.text)
    if match:
        info['views'] = int(match.group(1).replace(',', ''))
    # find published date: pattern 'Published YYYY.MM.DD' or 'Published YYYY' etc
    match = re.search(r'Published\s+(\d{4}\.\d{2}\.\d{2})', resp.text)
    if match:
        info['published'] = match.group(1)
    # find likes: appears as a number in a <div> next to 'Likes'. pattern: '## Likes' and below a number
    # Better to find an element with text 'Likes' and then find the next number.
    # Search for a number inside <div> after a heading of 'Likes'
    like_match = re.search(r'## Likes\s+([\d,]+)', resp.text)
    if like_match:
        info['likes'] = int(like_match.group(1).replace(',', ''))
    else:
        # sometimes the heading may be hidden? try a different pattern
        pass
    # find comments: '## Comments' etc
    com_match = re.search(r'## Comments\s+([\d,]+)', resp.text)
    if com_match:
        info['comments'] = int(com_match.group(1).replace(',', ''))
    return info

print(fetch_stats('5D86_ptqd8I'))
