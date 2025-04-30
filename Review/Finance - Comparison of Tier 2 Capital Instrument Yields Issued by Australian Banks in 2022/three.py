from second import get_df

class GetStats:
    
    def __init__(self):
        df = get_df()
        self.average_yield = df["Yield"].mean()
        self.highest_bank = df.iloc[df["Yield"].idxmax()]["Bank"]
        self.lowest_bank = df.iloc[df["Yield"].idxmin()]["Bank"]

    def __str__(self):
        return f"{str(self.average_yield), self.highest_bank, self.lowest_bank}"

if __name__ == "__main__":
    print(GetStats())
    