from twenty import get_final_table, get_freq_table

final_table = get_final_table()
freq_table = get_freq_table()
final_table_markdown = final_table.to_markdown(index=False)
freq_table_markdown = freq_table.reset_index().to_markdown(index=False)
print(final_table_markdown, freq_table_markdown)
