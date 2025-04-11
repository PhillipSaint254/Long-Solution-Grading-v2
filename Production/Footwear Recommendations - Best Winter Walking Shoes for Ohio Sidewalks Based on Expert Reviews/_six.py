import pandas as pd
from five import get_df 
from third import normalize

def get_df_norm():
    df = get_df()
    df_norm = pd.DataFrame()
    df_norm['warmth_norm'] = normalize(df['warmth'])
    df_norm['waterproof_norm'] = normalize(df['waterproof'])
    df_norm['traction_norm'] = normalize(df['traction'])
    df_norm['price_norm'] = normalize(df['price'], invert=True)
    df_norm['composite'] = df_norm.mean(axis=1)
    return df_norm

if __name__ == "__main__":
    df_norm = get_df_norm()
    print(df_norm.sort_values('composite', ascending=False))
