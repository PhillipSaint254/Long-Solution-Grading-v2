from eight import get_df

def get_desc_tano_episode():
    df = get_df()
    return df[df.description.str.contains('tano', case=False)].iloc[0]

if __name__ == "__main__":
    print(get_desc_tano_episode().title)
    