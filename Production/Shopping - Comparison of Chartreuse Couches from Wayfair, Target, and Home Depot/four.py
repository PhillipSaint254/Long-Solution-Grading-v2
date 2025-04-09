import pandas as pd, numpy as np, json, sys, math, statistics
import pandas as pd 
from second import get_sorted_couches

def get_df():
    sorted_couches = get_sorted_couches()
    return pd.DataFrame(sorted_couches)

if __name__ == "__main__":
    df = get_df()
    print(df)
