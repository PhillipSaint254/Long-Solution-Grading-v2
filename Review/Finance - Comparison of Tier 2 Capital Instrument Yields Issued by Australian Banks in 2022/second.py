import pandas as pd
from first import get_data

def get_df():
    # create DataFrame again
    data = get_data()
    return pd.DataFrame(data,columns=["Bank","Issue Date","Yield"])

if __name__ == "__main__":
    print(get_df())
