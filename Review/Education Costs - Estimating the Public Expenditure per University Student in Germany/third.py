from second import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.exchange_usd_to_eur = 0.904 # approximate 2016 average from FRED (since 1 EUR ~ 1.10 USD).

    def get_cost_annual_eur(self):
        return self.cost_annual * self.exchange_usd_to_eur
    
    def get_cost_bachelor_eur(self):
        return self.get_cost_bachelor() * self.exchange_usd_to_eur
    
    def get_cost_master_eur(self):
        return self.get_cost_master() * self.exchange_usd_to_eur
    
if __name__ == "__main__":
    stats = GetStats()
    print(stats.get_cost_annual_eur(), 
          stats.get_cost_bachelor_eur(), 
          stats.get_cost_master_eur())
