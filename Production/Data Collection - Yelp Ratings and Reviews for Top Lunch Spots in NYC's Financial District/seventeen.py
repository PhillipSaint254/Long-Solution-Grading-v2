from sixteen import get_df_avg_rating

df, _ = get_df_avg_rating()
print(df.round(2).to_markdown())
