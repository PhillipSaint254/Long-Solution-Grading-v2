from four import get_df

df = get_df()
avg_values = df[['BattingAverage','ERA','FieldingPct']].mean()
print(avg_values)
