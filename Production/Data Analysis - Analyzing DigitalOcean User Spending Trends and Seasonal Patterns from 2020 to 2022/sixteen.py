from thirteen import get_seasonal_table as get_seasonal_table_1

def get_seasonal_table():
    seasonal_table = get_seasonal_table_1()
    seasonal_table['Seasonal Effect'] = seasonal_table['Seasonal Effect'].round(2)
    return seasonal_table

if __name__ == "__main__":
    seasonal_table = get_seasonal_table()
    print(seasonal_table[['Month Name', 'Seasonal Effect']])
