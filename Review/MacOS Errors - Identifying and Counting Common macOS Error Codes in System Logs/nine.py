from eight import get_df

df = get_df()
dfMarkdown = df.to_markdown(index=False)
print(dfMarkdown)
