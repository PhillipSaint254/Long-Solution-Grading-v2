from sixteen import get_seasonal_table

seasonal_table = get_seasonal_table()
print(seasonal_table[['Month Name','Seasonal Effect']].to_markdown(index=False))
