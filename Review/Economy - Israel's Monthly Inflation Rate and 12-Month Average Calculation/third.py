from second import get_df as gdf

def get_df():
    df = gdf()
    df['Inflation rate'] = df['Inflation rate'].str.replace('%','').str.strip().astype(float)
    return df

if __name__ == "__main__":
    print(get_df().head())
