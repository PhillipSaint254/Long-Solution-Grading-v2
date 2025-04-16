from second import get_names_specialties
import pandas as pd

def get_data():
    data = []
    names_specialties = get_names_specialties()
    for name, spec in names_specialties.items():
        if 'Spine' in spec:
            cat = 'Spine Surgery'
        elif 'Sports' in spec:
            cat = 'Sports Medicine'
        else:
            cat = 'Joint Replacement'
        data.append({'Consulting Surgeon': name, 'Specialty Category': cat})
    return data

def get_df():
    data = get_data()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_df()
    print(df)
