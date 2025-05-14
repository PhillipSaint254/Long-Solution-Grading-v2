from four import get_df

def get_df_staff():
    df = get_df()
    return df.set_index("Year")

if __name__ == "__main__":
    print(get_df_staff())
