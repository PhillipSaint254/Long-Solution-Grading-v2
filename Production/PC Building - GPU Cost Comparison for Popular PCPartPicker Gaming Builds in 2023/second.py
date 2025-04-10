import pandas as pd
from first import get_builds

def get_data():
    builds = get_builds()
    return [{"Build": name, "Total Build Cost ($)": data["total_price"], "GPU Cost ($)": data["gpu_price"], "GPU % of Total": data["gpu_percentage"]} for name, data in builds.items()]

def get_df():
    data = get_data()
    df = pd.DataFrame(data)
    df = df.sort_values(by="Total Build Cost ($)", ascending=False)
    return df

if __name__ == "__main__":
    df = get_df()
    print(df)
