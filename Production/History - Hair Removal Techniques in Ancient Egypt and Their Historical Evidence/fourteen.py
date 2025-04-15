import pandas as pd, numpy as np, math
from thirteen import get_time_periods
from twelve import get_method_counts_source

def get_df():
    data = []
    time_periods = get_time_periods()
    method_counts_source = get_method_counts_source()
    for method, count in method_counts_source.items():
        period = time_periods[method]
        data.append([method, count, period])
    df = pd.DataFrame(data, columns=["Hair Removal Method", "Number of References", "Time Period (B.C.)"])
    return df

if __name__ == "__main__":
    print(get_df())
