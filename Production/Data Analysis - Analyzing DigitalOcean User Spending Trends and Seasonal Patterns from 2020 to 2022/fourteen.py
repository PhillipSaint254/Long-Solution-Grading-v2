from thirteen import get_seasonal_table

seasonal_table = get_seasonal_table()
print(seasonal_table.sort_values('Seasonal Effect').head())
