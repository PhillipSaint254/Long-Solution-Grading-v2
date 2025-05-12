from first import get_feed

feed = get_feed()
print(feed.entries[-1].title, feed.entries[-1].published)
