import pandas as pd, re, datetime
from first import get_feed

def get_entries():
    # Convert entries to DataFrame
    entries = []
    feed = get_feed()
    for entry in feed.entries:
        title = entry.title
        pubdate = entry.published  # str
        # convert to datetime
        dt = datetime.datetime.strptime(pubdate, '%a, %d %b %Y %H:%M:%S %z')
        # description or summary
        desc = entry.get('summary', '')  # may contain html
        entries.append({'title': title, 'pubdate': dt, 'description': desc})
    return entries
    
def get_df():
    return pd.DataFrame(get_entries())

if __name__ == "__main__":
    df = get_df()
    print(df.head(), df.tail(), len(df))
