from ten import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.annual_cost_usd_rounded = round(self.annual_cost_usd, 0)
        self.annual_cost_eur_rounded = round(self.annual_cost_usd * 0.9, 0)

if __name__ == "__main__":
    stats = GetStats()
    print(stats.annual_cost_usd_rounded, 
          stats.annual_cost_eur_rounded)
