import pandas as pd
from second import get_data

def get_df():
    data = get_data()
    return pd.DataFrame(data)

if __name__ == "__main__":
    print(get_df())
