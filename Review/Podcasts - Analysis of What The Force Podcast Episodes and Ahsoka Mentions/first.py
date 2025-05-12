import feedparser

def get_feed():
    return feedparser.parse("https://whattheforce.ca/feed/podcast/")

if __name__ == "__main__":
    feed = get_feed()
    print(len(feed.entries), feed.entries[0].title, feed.entries[0].published)
