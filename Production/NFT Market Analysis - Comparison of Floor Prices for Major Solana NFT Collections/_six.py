from five import get_table_data
import pandas as pd

def get_table_df():
    table_data = get_table_data()
    table_df = pd.DataFrame(table_data, columns=['NFT Collection', 'Floor Price (SOL)', 'Difference from Average (%)'])
    table_df['Floor Price (SOL)'] = table_df['Floor Price (SOL)'].round(2)
    table_df['Difference from Average (%)'] = table_df['Difference from Average (%)'].round(1)
    return table_df

if __name__ == "__main__":
    print(get_table_df())
