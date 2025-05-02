from eight import get_df_final

df_final = get_df_final()
table_markdown = df_final.to_markdown(index=False)
print(table_markdown)
