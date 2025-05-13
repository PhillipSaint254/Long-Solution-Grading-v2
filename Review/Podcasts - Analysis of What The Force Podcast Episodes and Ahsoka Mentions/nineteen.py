from twenty import get_df

def get_episodes_df():
    df = get_df()
    episodes_df = df[['pubdate','title']].copy()
    episodes_df['release_date'] = episodes_df.pubdate.dt.date.astype(str)
    return episodes_df[['release_date','title']]

if __name__ == "__main__":
    episodes_df = get_episodes_df()
    print(episodes_df.head())
