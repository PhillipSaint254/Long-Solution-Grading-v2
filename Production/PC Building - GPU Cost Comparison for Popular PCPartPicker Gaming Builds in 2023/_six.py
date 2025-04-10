from five import get_df

df = get_df()
print(df.round({"GPU % of Total":2}))
