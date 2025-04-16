from third import get_df

def get_df_counts():
    df = get_df()
    df_counts = df['Specialty Category'].value_counts().reset_index()
    df_counts.columns = ['Specialty Category', 'Total Count']
    return df_counts

if __name__ == "__main__":
    print(get_df_counts())
    