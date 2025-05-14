from nine import GetStats as GST

class GetStats(GST):
    def get_df_costs(self):
        df_costs = super().get_df_costs()
        return df_costs.round({
            "Bachelor 3 yr cost (USD)": 0,
            "Master 2 yr cost (USD)": 0,
            "Bachelor 3 yr cost (EUR)": 0,
            "Master 2 yr cost (EUR)": 0
        })

if __name__ == "__main__":
    print(GetStats().get_df_costs())
