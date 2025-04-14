from ten import get_pattern

def get_seasonal_table():
    pattern = get_pattern()
    seasonal_table = pattern.reset_index()
    seasonal_table.columns = ['Month', 'Seasonal Effect']
    return seasonal_table

if __name__ == "__main__":
    seasonal_table = get_seasonal_table()
    print(seasonal_table)
    