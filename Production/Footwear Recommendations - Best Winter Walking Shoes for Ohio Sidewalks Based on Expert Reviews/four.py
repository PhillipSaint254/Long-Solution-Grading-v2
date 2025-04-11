from third import get_df_norm as get_df_norm_1

def get_df_norm():
    df_norm = get_df_norm_1()
    df_norm['composite'] = df_norm.mean(axis=1)
    df_norm.sort_values('composite', ascending=False)
    return df_norm

if __name__ == "__main__":
    df_norm = get_df_norm()
    print(df_norm)
