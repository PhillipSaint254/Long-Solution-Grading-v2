from five import GetStats as GST
import pandas as pd

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.fields = ['Humanities', 'Sciences', 'Engineering']
        self.degree_type = self.degrees

    def get_rows(self):
        rows = []
        for field in self.fields:
            rows.append({"Study Direction": field, "Degree": "Bachelor (3 years)", "Total Cost (USD)": self.get_total_cost_bachelor()})
            rows.append({"Study Direction": field, "Degree": "Master (2 years)", "Total Cost (USD)": self.get_total_cost_master()})
            rows.append({"Study Direction": field, "Degree": "Full 3+2 (Bach+Master)", "Total Cost (USD)": self.get_total_cost_bachelor()+self.get_total_cost_master()})
        return rows
    
    def get_df(self):
        rows = self.get_rows()
        return pd.DataFrame(rows)
    
if __name__ == "__main__":
    print(GetStats().get_df())
