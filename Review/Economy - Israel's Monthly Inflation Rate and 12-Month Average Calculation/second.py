from first import get_tables

def get_df():
    tables = get_tables()
    return tables[0].copy()

if __name__ == "__main__": 
    df = get_df()
    print(df.head())
