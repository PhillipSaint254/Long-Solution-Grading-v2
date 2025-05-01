import pandas as pd, numpy as np
from third import get_event_data


def get_df():
    event_data = get_event_data()
    return pd.DataFrame(event_data)

if __name__ == "__main__":
    print(get_df())
