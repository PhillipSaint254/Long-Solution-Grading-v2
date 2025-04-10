from second import get_df

df = get_df()
df["GPU % of Total"] = df["GPU % of Total"] * 100  # Wait we already multiply by 100; oh we mis; Wait we double.
print(df)
