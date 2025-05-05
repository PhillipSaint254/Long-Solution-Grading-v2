import pandas as pd, numpy as np

def get_data():
    return {
    'Fuel Type': ['Diesel', 'Petrol (ethanol‑free gasoline)', 'Jet A-1 jet fuel', 'Unleaded gasoline (automotive)'],
    'Density (kg/L)': [0.832, 0.745, 0.8075, 0.745],  # Jet typical average 0.8075
    'Energy content (MJ/L)': [35.86, 32.18, 37.627, 33.526],
}

def get_df():
    data = get_data()
    df = pd.DataFrame(data)
    df['Energy per mass (MJ/kg)'] = df['Energy content (MJ/L)'] / df['Density (kg/L)']
    return df

if __name__ == "__main__":
    print(get_df())
