import requests
from bs4 import BeautifulSoup

resp = requests.get('http://feeds.feedburner.com/LinkedInBlog', headers={'User-Agent':'Mozilla/5.0'})
# parse the response as XML
from lxml import etree

root = etree.fromstring(resp.content)
# find first five items
items = root.findall('.//item')[:5]
for it in items:
    title = it.findtext('title')
    link = it.findtext('link')
    pubDate = it.findtext('pubDate')
    # get description
    desc = it.findtext('description')
    print(title, pubDate, link)
    print(desc[:150], '\n')

