import pandas as pd
from second import get_df

def normalize(series, invert=False):
    if invert:
        # invert for price: smaller better
        return 1 - (series - series.min()) / (series.max() - series.min())
    else:
        return (series - series.min()) / (series.max() - series.min())

def get_df_norm():
    df = get_df()
    df_norm = pd.DataFrame()
    df_norm['warmth_norm'] = normalize(df['warmth'])
    df_norm['waterproof_norm'] = normalize(df['waterproof'])
    df_norm['traction_norm'] = normalize(df['traction'])
    df_norm['price_norm'] = normalize(df['price'], invert=True)
    return df_norm

if __name__ == "__main__":
    df_norm = get_df_norm()
    print(df_norm)
