from third import get_df

def get_ahsoka_df():
    df = get_df()
    return df[df['title'].str.contains('Ahsoka', case=False) | df['description'].str.contains('Ahsoka', case=False)]

if __name__ == "__main__":
    ahsoka_df = get_ahsoka_df()
    print(ahsoka_df[['pubdate','title']].head(), len(ahsoka_df))
