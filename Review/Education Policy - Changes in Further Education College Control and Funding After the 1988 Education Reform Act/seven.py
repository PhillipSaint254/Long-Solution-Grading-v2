from _six import get_df

def get_table():
    df = get_df()
    table = df.copy()
    table["Funding (£m)"] = table["Funding (£m)"].map(lambda x: f"£{x:,.1f}m")
    table["Estimated staff numbers"] = table["Estimated staff numbers"].map(lambda x: f"{x:,}")
    return table

if __name__ == "__main__":
    print(get_table().to_markdown(index=False))
