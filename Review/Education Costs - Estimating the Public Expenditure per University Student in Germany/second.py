from first import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.cost_annual = 14426.869982256332

    def get_cost_bachelor(self):
        return self.cost_annual * 3
    
    def get_cost_master(self):
        return self.cost_annual * 2
    
if __name__ == "__main__":
    stats = GetStats()
    cost_bachelor = stats.get_cost_bachelor()
    cost_master = stats.get_cost_master()
    print(cost_bachelor, cost_master)
