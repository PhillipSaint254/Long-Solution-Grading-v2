from first import get_floor_prices

# convert lamports to SOL (1e9 lamports per SOL)
def get_floor_prices_SOL():
    floor_prices = get_floor_prices()
    return {c: lam/1e9 if lam is not None else None for c, lam in floor_prices.items()}

if __name__ == "__main__":
    floor_prices_SOL = get_floor_prices_SOL()
    print(floor_prices_SOL)
