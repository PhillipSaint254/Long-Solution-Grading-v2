from four import get_df

df = get_df()
print([df[df.title.str.contains('Ahsoka', case=False)].shape, df[df.description.str.contains('Ahsoka', case=False)].shape])
