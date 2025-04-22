from three import get_df

df = get_df()
markdown_table = df.to_markdown(index=False)
print(markdown_table[:500])
