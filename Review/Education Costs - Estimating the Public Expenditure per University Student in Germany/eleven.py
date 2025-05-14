from ten import GetStats

df_costs = GetStats().get_df_costs()

print(df_costs.to_markdown(index=False))
