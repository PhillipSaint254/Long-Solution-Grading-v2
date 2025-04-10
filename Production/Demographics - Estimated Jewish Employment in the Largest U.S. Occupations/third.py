from second import get_df as get_df_1

def get_df():
    df = get_df_1()
    df['Estimated Jewish Workers'] = df['Estimated Jewish Workers'].round(0).astype(int)
    df['% of Jewish Population'] = df['% of Jewish Population'].round(2)
    return df

if __name__ == "__main__":
    df = get_df()
    print(df)
