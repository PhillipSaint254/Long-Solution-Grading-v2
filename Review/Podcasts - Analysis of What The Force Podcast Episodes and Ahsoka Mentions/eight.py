from four import get_df as gdf

def get_df():
    df = gdf()
    df['year'] = df.pubdate.dt.year
    return df
    
if __name__ == "__main__":
    df = get_df()
    print(df)
    print(df.groupby('year').size())
