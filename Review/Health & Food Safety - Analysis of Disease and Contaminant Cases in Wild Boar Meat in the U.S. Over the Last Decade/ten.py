from seven import get_df as gdf

def get_df():
    df = gdf()
    df["location"] = ["Colorado recall (FSIS)", "Colorado recall (FSIS)", "California outbreak", "Florida case"]
    return df

if __name__ == "__main__":
    print(get_df())
    