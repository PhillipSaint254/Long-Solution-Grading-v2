from eight import get_df

df = get_df()

for idx, row in df.iterrows():
    if "tano" in row.description.lower():
        print(idx, row.pubdate, row.title)
