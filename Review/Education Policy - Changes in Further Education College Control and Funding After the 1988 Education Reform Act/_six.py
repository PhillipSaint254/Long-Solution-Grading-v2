import pandas as pd

def get_df():
    return pd.DataFrame({
        "Year": ["1987 (pre‑ERA)", "1989 (post‑ERA)"],
        "Colleges under LEA control": [360, 400],
        "Funding (£m)": [716.5, 1030],
        "Estimated staff numbers": [60227, 26574]
    })

if __name__ == "__main__":
    print(get_df())
