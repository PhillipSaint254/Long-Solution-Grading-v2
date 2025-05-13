from eight import get_df

idx = 15
df = get_df()
desc = df.loc[idx, 'description'].lower()
start = desc.index('tano')-40 if 'tano' in desc else 0
print(desc[start:start+200])
