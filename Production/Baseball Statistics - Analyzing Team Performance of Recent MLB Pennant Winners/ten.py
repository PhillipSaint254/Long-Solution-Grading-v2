from nine import get_final_table

final_table = get_final_table()
print(final_table.round({'BattingAverage':3,'ERA':2,'FieldingPct':3}).to_markdown())
