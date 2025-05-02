from four import get_df_sorted as gdfs

def get_df_sorted():
    df_sorted = gdfs()
    df_sorted['Inflation rate (%)'] = df_sorted['Inflation rate']
    df_sorted = df_sorted[['Month','Inflation rate (%)']]
    return df_sorted

if __name__ == "__main__":
    print(get_df_sorted())
