from eight import get_df

df = get_df()

# Search for 'ahsoka' or 'tano' etc.
keywords = ['ahsoka','tano']
for kw in keywords:
    print(kw, "in titles:", df.title.str.contains(kw, case=False).sum(), "in description:", df.description.str.contains(kw, case=False).sum())
