from four import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.annual_cost_usd = self.get_cost_usd_2016()
        self.years_bachelor = 3
        self.years_master = 2
        self.degrees = ['Bachelor (3 years)', 'Master (2 years)']

    def get_total_cost_bachelor(self):
        return self.annual_cost_usd * self.years_bachelor
    
    def get_total_cost_master(self):
        return self.annual_cost_usd * self.years_master
    
if __name__ == "__main__":
    stats  = GetStats()
    print(stats.annual_cost_usd, 
          stats.get_total_cost_bachelor(), 
          stats.get_total_cost_master())
