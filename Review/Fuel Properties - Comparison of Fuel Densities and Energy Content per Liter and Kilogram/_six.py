from five import get_df as gdf

def get_df():
    df = gdf()
    df['Density (kg/L)']=df['Density (kg/L)'].round(3)
    df['Energy content (MJ/L)']=df['Energy content (MJ/L)'].round(2)
    df['Energy per mass (MJ/kg)'] = df['Energy per mass (MJ/kg)'].round(2)
    return df

if __name__ == "__main__":
    print(get_df())
