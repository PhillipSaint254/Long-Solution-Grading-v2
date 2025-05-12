from four import get_df

df = get_df()
print(list(set([w for t in df.title for w in t.split() if w.lower().startswith('aho') or w.lower().startswith('ahs') or w.lower().startswith('ahsoka')])))
