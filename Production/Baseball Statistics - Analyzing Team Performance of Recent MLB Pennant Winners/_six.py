from four import get_df

df = get_df()
season_avg = df.groupby('Season')[['BattingAverage','ERA','FieldingPct']].mean().sort_index(ascending=False) # sort desc 2023 to 2019
print(season_avg)
