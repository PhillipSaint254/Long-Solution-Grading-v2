from twelve import get_df_table

df_table = get_df_table()
print(df_table.to_markdown(index=False))
