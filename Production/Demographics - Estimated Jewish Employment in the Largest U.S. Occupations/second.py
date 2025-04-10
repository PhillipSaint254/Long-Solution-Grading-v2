import pandas as pd, numpy as np, math, json, sys, pandas as pd
from first import get_results

# Format results
def get_df():
    results = get_results()
    return pd.DataFrame(results, columns=['Occupation', 'Employment 2023', 'Estimated Jewish Workers', '% of Jewish Population'])

if __name__ == "__main__":
    df = get_df()
    print(df)
