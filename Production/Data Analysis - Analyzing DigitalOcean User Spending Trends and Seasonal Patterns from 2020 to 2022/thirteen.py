from twelve import get_seasonal_table as get_seasonal_table_1
# Map month numbers to names for readability
import calendar

def get_seasonal_table():
    seasonal_table = get_seasonal_table_1()
    seasonal_table['Month Name'] = seasonal_table['Month'].apply(lambda x: calendar.month_name[x])
    return seasonal_table

if __name__ == "__main__":
    seasonal_table = get_seasonal_table()
    print(seasonal_table)
    print(seasonal_table.sort_values('Seasonal Effect', ascending=False).head())
