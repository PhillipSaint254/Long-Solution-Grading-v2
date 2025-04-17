import numpy as np
from second import get_floor_prices_SOL

def get_avg_floor():
    floor_prices_SOL = get_floor_prices_SOL()
    return np.mean(list(floor_prices_SOL.values()))

if __name__ == "__main__":
    avg_floor = get_avg_floor()
    print(avg_floor)
    