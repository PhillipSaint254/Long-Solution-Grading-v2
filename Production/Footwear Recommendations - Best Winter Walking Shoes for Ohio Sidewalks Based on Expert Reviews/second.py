import numpy as np, pandas as pd, math, json, statistics
from first import get_shoes

def get_df():
    shoes = get_shoes()
    # convert to DataFrame
    return pd.DataFrame(shoes).T

if __name__ == "__main__":
    df = get_df()
    print(df)
