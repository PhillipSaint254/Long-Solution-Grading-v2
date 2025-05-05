import pandas as pd, numpy as np
from third import GetStats

def get_data():
    stats = GetStats()
    return {
        'Fuel Type': ['Diesel', 'Petrol (gasoline)', 'Jet A-1 jet fuel', 'Unleaded gasoline'],
        'Density (kg/L)': [stats.density_diesel, stats.density_petrol, 0.81, stats.density_unleaded],
        'Energy content (MJ/L)': [stats.energy_diesel, stats.energy_petrol, stats.energy_jet, stats.energy_unleaded],
    }

def get_df():
    data = get_data()
    df = pd.DataFrame(data)
    df['Energy per mass (MJ/kg)'] = df['Energy content (MJ/L)'] / df['Density (kg/L)']
    return df

if __name__ == "__main__":
    print(get_df())
