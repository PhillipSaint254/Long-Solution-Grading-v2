from four import get_avg_floor
from second import get_floor_prices

def get_table_data():
    table_data = []
    floor_prices = get_floor_prices()
    avg_floor = get_avg_floor()
    for c, fp_lam in floor_prices.items():
        sol = fp_lam / 1e9
        pct = (sol - avg_floor) / avg_floor * 100
        table_data.append([c.replace('_', ' ').title(), sol, pct])
    return table_data

if __name__ == "__main__":
    print(get_table_data())
