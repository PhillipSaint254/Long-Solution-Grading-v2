from setup_data import get_countries_data

import pandas as pd, numpy as np, math, textwrap, json, os, re, sys, pandas as pd
import numpy as np

# Convert dictionary to DataFrame
def get_df():
    countries_data = get_countries_data()
    df = pd.DataFrame(countries_data).T
    df_sorted = df.sort_values('months_to_afford')
    return df_sorted

if __name__ == "__main__":
    print(get_df())