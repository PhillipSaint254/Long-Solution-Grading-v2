from twelve import get_method_years
import numpy as np, pandas as pd, math

def get_time_periods():
    method_years = get_method_years()
    time_periods = {}
    for method, years in method_years.items():
        if years:
            time_periods[method] = f"{min(years)}-{max(years)} B.C."
        else:
            time_periods[method] = "N/A"
    return time_periods

if __name__ == "__main__":
    print(get_time_periods())
