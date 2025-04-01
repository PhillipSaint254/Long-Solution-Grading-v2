import pandas as pd

url = 'https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=CA&years=2022&actions_taken=1'

# read just first few rows to inspect columns
df_head = pd.read_csv(url, nrows=5)
print(df_head.head())
