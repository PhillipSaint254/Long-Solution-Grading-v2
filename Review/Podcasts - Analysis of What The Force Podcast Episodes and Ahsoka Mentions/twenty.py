from eight import get_df as gdf

def get_df():
    df = gdf()
    df[df.description.str.contains('tano', case=False)][['pubdate','title','description']].iloc[0, :]
    return df
