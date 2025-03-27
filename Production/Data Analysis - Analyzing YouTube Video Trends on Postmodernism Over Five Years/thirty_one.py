import requests
from bs4 import BeautifulSoup
import re

def fetch_stats(video_id):
    """
    Fetches video statistics from playboard.co given a video ID.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        dict: A dictionary containing video stats (views, published date, likes, comments), or None if request fails.
    """
    url = f'https://playboard.co/en/video/{video_id}'
    resp = requests.get(url, timeout=15)
    
    if resp.status_code != 200:
        return None

    soup = BeautifulSoup(resp.text, 'html.parser')
    info = {}

    # Extract views
    view_el = soup.find(string=lambda s: s and 'views' in s)
    if view_el:
        m = re.search(r'([\d,]+)\s+views', view_el)
        if m:
            info['views'] = int(m.group(1).replace(',', ''))

    # Extract published date
    pub_el = soup.find(string=lambda s: s and 'Published' in s)
    if pub_el:
        m = re.search(r'Published\s+(\d{4}\.\d{2}\.\d{2})', pub_el)
        if m:
            info['published'] = m.group(1)

    # Extract likes
    for box in soup.select('.score__box'):
        title_el = box.find('h2')
        if title_el and title_el.text.strip() == 'Likes':
            num = box.find(class_='score__num')
            if num:
                info['likes'] = int(num.text.replace(',', ''))
            break

    # Extract comments
    for box in soup.select('.score__box'):
        title_el = box.find('h2')
        if title_el and title_el.text.strip() == 'Comments':
            num = box.find(class_='score__num')
            if num:
                info['comments'] = int(num.text.replace(',', ''))
            break

    return info

# If this file is run as a script, it will execute the example, but it can also be imported as a module.
if __name__ == "__main__":
    video_id = '5D86_ptqd8I'
    print(fetch_stats(video_id))
