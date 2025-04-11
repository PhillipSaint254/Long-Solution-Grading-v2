import pandas as pd
from first import get_shoes

def get_df():
    shoes = get_shoes()
    shoes['Columbia Bugaboot III']['price'] = 130
    return pd.DataFrame(shoes).T

if __name__ == "__main__":
    df = get_df()
    print(df)
