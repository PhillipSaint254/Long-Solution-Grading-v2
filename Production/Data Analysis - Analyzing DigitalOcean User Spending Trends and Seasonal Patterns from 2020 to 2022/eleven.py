from _six import get_yearly_avg_monthly

def get_yearly_avg_table():
    yearly_avg_monthly = get_yearly_avg_monthly()
    yearly_avg_table = yearly_avg_monthly.reset_index()
    yearly_avg_table.columns = ['Year', 'Average Monthly Spend (USD)']
    return yearly_avg_table

if __name__ == "__main__":
    yearly_avg_table = get_yearly_avg_table()
    print(yearly_avg_table)
    