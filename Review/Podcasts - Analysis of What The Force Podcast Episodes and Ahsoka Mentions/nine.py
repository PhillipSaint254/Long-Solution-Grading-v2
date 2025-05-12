from eight import get_df

def get_df_2023():
    df = get_df()
    return df[df.year==2023][['pubdate','title']]

if __name__ == "__main__":
    print(get_df_2023().head(20))
