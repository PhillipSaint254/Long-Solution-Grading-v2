from third import get_df

def get_df_final():
    df = get_df()
    df_final = df.copy()
    # Format numbers with commas
    df_final['Employment (2023 BLS)'] = df_final['Employment 2023'].map(lambda x: f"{x:,}")
    df_final['Estimated Jewish Workers'] = df_final['Estimated Jewish Workers'].map(lambda x: f"{x:,}")
    df_final['% of Jewish Population'] = df_final['% of Jewish Population'].map(lambda x: f"{x:.2f}%")
    df_display = df_final[['Occupation', 'Employment (2023 BLS)', 'Estimated Jewish Workers', '% of Jewish Population']]
    return df_display

if __name__ == "__main__":
    df_final = get_df_final()
    print(df_final)
