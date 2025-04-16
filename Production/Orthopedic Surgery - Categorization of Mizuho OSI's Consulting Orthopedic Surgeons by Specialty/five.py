from third import get_df

def get_df_final():
    df = get_df()
    return df.copy()

if __name__ == "__main__":
    df_final = get_df_final()
    print(df_final)
