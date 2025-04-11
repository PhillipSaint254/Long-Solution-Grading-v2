from _six import get_df_norm
from five import get_df 

def get_df_combined():
    df = get_df()
    df_norm = get_df_norm()
    df_combined = df.copy()
    df_combined['Composite Score'] = df_norm['composite']
    df_combined.round(2)
    return df_combined

if __name__ == "__main__":
    df_combined = get_df_combined()
    print(df_combined)
