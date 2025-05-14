from third import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.exchange = 0.9

    def get_cost_annual_eur(self):
        return self.cost_annual * self.exchange
    
    def get_cost_bachelor_eur(self):
        return self.get_cost_bachelor() * self.exchange
    
    def get_cost_master_eur(self):
        return self.get_cost_master() * self.exchange
    
if __name__ == "__main__":
    stats = GetStats()
    print(stats.get_cost_bachelor_eur(), 
        stats.get_cost_master_eur(), 
        stats.get_cost_annual_eur())
