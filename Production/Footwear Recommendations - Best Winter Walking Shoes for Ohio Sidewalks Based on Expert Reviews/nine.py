from seven import get_df_combined

def get_df_display():
    df_combined = get_df_combined()
    df_display = df_combined.copy()
    df_display['Composite Score'] = df_display['Composite Score'].round(2)
    return df_display

if __name__ == "__main__":
    df_display = get_df_display()
    print(df_display)
# smh