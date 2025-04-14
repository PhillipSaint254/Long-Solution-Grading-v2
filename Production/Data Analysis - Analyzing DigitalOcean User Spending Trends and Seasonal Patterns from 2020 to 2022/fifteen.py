from eleven import get_yearly_avg_table as get_yearly_avg_table_1

def get_yearly_avg_table():
    yearly_avg_table = get_yearly_avg_table_1()
    yearly_avg_table['Average Monthly Spend (USD)'] = yearly_avg_table['Average Monthly Spend (USD)'].round(2)
    return yearly_avg_table


if __name__ == "__main__":
    yearly_avg_table = get_yearly_avg_table()
    print(yearly_avg_table)
