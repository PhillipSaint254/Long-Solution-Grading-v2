from _six import GetStats as GST

class GetStats(GST):
    def get_df(self):
        df = super().get_df()
        df["Total Cost (USD)"] = df["Total Cost (USD)"].round(0)
        return df
    
if __name__ == "__main__":
    print(GetStats().get_df())