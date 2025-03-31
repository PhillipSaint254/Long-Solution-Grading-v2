from twenty_two import get_df_sorted

df_sorted = get_df_sorted()

print(df_sorted[['Country','Total','Population','Oph_per_100k']].to_string(index=False))
