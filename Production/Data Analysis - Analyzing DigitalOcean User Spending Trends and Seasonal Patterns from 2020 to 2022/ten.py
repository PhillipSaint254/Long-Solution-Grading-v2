from nine import get_seasonal_pattern
import pandas as pd

def get_pattern():
    seasonal_pattern = get_seasonal_pattern()
    seasonal_pattern.index = seasonal_pattern.index.month  # convert to months 1..12
    return pd.Series(seasonal_pattern.values, index=range(1,13))

if __name__ == "__main__":
    pattern = get_pattern()
    print(pattern)
