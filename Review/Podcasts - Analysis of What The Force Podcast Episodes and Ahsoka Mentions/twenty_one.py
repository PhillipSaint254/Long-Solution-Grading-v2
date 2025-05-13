from twenty import get_df

def get_ahsoka_episodes():
    df = get_df()
    return df[df['title'].str.contains('ahsoka', case=False) | df['description'].str.contains('ahsoka', case=False)].copy()

if __name__ == "__main__":
    ahsoka_episodes = get_ahsoka_episodes()
    print(ahsoka_episodes[['pubdate','title']].head(), len(ahsoka_episodes))
