from third import get_df

def get_df_rounded():
    df = get_df()
    df_rounded = df.copy()
    df_rounded['Estimated Jewish Workers'] = (df_rounded['Estimated Jewish Workers'] / 1000).round(0) * 1000 # round to nearest thousand
    df_rounded['Estimated Jewish Workers'] = df_rounded['Estimated Jewish Workers'].astype(int)
    df_rounded['% of Jewish Population'] = df_rounded['% of Jewish Population'].round(2)
    return df_rounded

if __name__ == "__main__":
    df_rounded = get_df_rounded()
    print(df_rounded)
