from seven import GetStats as GST

class GetStats(GST):
    def get_eur(self):
        df = self.get_df()
        df_eur = df.copy()
        df_eur["Total Cost (EUR)"] = (df_eur["Total Cost (USD)"] * 0.9).round(0)
        return df_eur
    
if __name__ == "__main__":
    print(GetStats().get_eur())
