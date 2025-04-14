from sixteen import get_seasonal_table

def get_seasonal_markdown():
    seasonal_table = get_seasonal_table()
    return seasonal_table[['Month Name', 'Seasonal Effect']].to_markdown(index=False)

if __name__ == "__main__":
    seasonal_markdown = get_seasonal_markdown()
    print(seasonal_markdown[:500])
