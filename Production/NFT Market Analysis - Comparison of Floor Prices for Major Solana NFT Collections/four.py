from third import get_floor_prices_SOL, get_avg_floor

def get_pct_diff():
    floor_prices_SOL = get_floor_prices_SOL()
    avg_floor = get_avg_floor()
    return {c: ((fp - avg_floor)/avg_floor)*100 for c, fp in floor_prices_SOL.items()}

if __name__ == "__main__":
    pct_diff = get_pct_diff()
    print(pct_diff)
    