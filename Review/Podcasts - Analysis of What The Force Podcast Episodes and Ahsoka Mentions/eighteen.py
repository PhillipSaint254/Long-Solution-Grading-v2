from eight import get_df

def get_average_all_years():
    df = get_df()
    return df.groupby(df.pubdate.dt.year).size().mean()

if __name__ == "__main__":
    print(get_average_all_years())
