import pandas as pd
from five import get_sorted_rows

def get_df():
    data = get_sorted_rows()
    return pd.DataFrame(data, columns=['Integration','Users','% of ChatGPT Users'])

if __name__ == "__main__":
    print(get_df())
