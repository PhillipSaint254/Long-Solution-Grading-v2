from four import get_df as gdf

def get_df():
    df = gdf()
    df["Yield (%)"] = df["Yield"]
    return df.drop(columns="Yield")

if __name__ == "__main__":
    print(get_df())
