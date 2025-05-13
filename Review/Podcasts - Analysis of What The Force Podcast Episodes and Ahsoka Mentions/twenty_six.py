from twenty_five import get_feed

feed = get_feed()

print(len(feed.entries))
print(len(feed.entries[279]))
