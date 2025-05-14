import pandas as pd, numpy as np


def get_data():
    return {
        "Year": [1987, 1989],
        "Number_of_FE_Colleges_under_LEA_control": [360, 400],  # approx
        "Funding_allocated_by_LEAs_or_associated_mechanism_£m": [716.5, 1030],
        "Estimated_staffing_levels": [60227, 26574]
    }

def get_df():
    data = get_data()
    return pd.DataFrame(data)

if __name__ == "__main__":
    print(get_df())
