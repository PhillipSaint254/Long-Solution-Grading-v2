from eight import GetStats as GST
import pandas as pd, numpy as np

class GetStats(GST):
    def get_df_costs(self):
        return pd.DataFrame({
            "Study Direction": ["Humanities", "Sciences", "Engineering"],
            "Bachelor 3 yr cost (USD)": np.repeat(self.get_total_cost_bachelor(),3),
            "Master 2 yr cost (USD)": np.repeat(self.get_total_cost_master(),3),
            "Bachelor 3 yr cost (EUR)": np.repeat(self.get_total_cost_bachelor()*0.9,3),
            "Master 2 yr cost (EUR)": np.repeat(self.get_total_cost_master()*0.9,3)
        })

if __name__ == "__main__":
    df_costs = GetStats().get_df_costs()
    print(df_costs)
