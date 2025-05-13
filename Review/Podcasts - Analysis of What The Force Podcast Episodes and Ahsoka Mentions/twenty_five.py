from twenty_four import get_text
import feedparser, pandas as pd, datetime, re

def get_feed():
    text = get_text()
    return feedparser.parse(text)

def get_aher_df():
    feed = get_feed()
    return pd.DataFrame([{'title':entry.title, 'pubdate':datetime.datetime(*entry.published_parsed[:6]), 
                        'description':entry.get('description','') + ' ' + entry.get('summary','') + ' ' + entry.get('content','')[0].value if 'content' in entry else entry.get('summary','')}
                        for entry in feed.entries])

def get_Ahsoka_ep():
    aher_df = get_aher_df()
    return aher_df[aher_df.apply(lambda row: bool(re.search(r'ahsoka', row.title+row.description, re.I)), axis=1)]

if __name__ == "__main__":
    Ahsoka_ep = get_Ahsoka_ep()
    print(Ahsoka_ep[['pubdate','title']].head(),len(Ahsoka_ep))
