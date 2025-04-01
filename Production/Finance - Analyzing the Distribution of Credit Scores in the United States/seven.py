import pandas as pd
import numpy as np
from _six import get_arr_rand

def get_percentages():
    return [10.0] * 10


def get_deviles_data():
    arr_rand = get_arr_rand()

    # Get the decile thresholds and build a summary dataframe

    # percentiles at 10 to 90
    deciles_labels = [f"D{i}" for i in range(1, 10)]
    deciles_vals = np.percentile(arr_rand, np.arange(10, 100, 10))
    return deciles_labels, deciles_vals

if __name__ == "__main__":
    deciles_labels, deciles_vals = get_deviles_data()
    arr_rand = get_arr_rand()

    # To construct ranges for each decile:
    # Decile 1: min to d1
    # Decile 2: d1 to d2
    # ...
    # Decile 9: d8 to d9
    # Decile 10: d9 to max

    lower_bounds = [arr_rand.min()] + list(deciles_vals[:-1])
    upper_bounds = list(deciles_vals) + [arr_rand.max()]

    # percentages: by definition, roughly 10%
    percentages = get_percentages()

    # build DataFrame
    import math

    decile_rows = []
    for i in range(10):
        row = {
            'Decile': i+1,
            'Score range': f"{lower_bounds[i]:.0f}–{upper_bounds[i]:.0f}",
            'Percent of scores': f"{percentages[i]:.1f}%"
        }
        decile_rows.append(row)

    decile_df = pd.DataFrame(decile_rows)
    print(decile_df)
