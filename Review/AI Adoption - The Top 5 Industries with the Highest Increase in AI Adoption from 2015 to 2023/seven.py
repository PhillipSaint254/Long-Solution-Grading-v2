import pandas as pd

# Data from above
def get_data():
    return [
        ('Retail', 4, 79),
        ('Manufacturing', 12, 70),
        ('IT & Telecom', 12, 63),
        ('Financial Services', 55, 99),
        ('Health Care', 12, 38),
    ]

def get_df():
    data = get_data()
    df = pd.DataFrame(data, columns=['Industry', '2015/2017 Adoption (%)', '2023 Adoption (%)'])
    df['Increase (percentage points)'] = df['2023 Adoption (%)'] - df['2015/2017 Adoption (%)']
    df = df.sort_values(by='Increase (percentage points)', ascending=False)
    return df

if __name__ == "__main__":
    print(get_df())
