from four import get_df

df = get_df()
print([df.title.str.contains('[Aa]hsoka', regex=True).sum(), df.description.str.contains('[Aa]hsoka', regex=True).sum()])
