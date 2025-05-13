from eight import get_df

def get_episodes_per_year():
    df = get_df()
    return df.groupby(df.pubdate.dt.year).size()

if __name__ == "__main__":
    print(get_episodes_per_year())
