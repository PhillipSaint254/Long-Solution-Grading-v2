from five import get_df

df = get_df()
highest_bank = df.loc[df["Yield (%)"].idxmax(), "Bank"]
lowest_bank = df.loc[df["Yield (%)"].idxmin(), "Bank"]
highest_bank, lowest_bank