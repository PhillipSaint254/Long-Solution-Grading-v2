from eight import get_df

df = get_df()

print(df[df.description.str.contains('tano', case=False)][['pubdate','title','description']].iloc[0, :])
