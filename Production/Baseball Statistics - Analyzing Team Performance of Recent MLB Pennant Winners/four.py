from third import get_records
import pandas as pd

def get_df():
    records = get_records()
    return pd.DataFrame(records)

if __name__ == "__main__":
    print(get_df())
