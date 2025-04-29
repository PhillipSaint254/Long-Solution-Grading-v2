import pandas as pd, requests

def get_url():
    return "https://www.nbastuffer.com/2023-2024-nba-player-stats/"

def get_tables():
    url = get_url()
    return pd.read_html(url)

if __name__ == "__main__":
    tables = get_tables()
    print(len(tables), [t.shape for t in tables][:5])
