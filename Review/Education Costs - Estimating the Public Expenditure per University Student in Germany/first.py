
class GetStats:
    def __init__(self):
        self.gdp_2016 = 42961.0356905775
        self.ratio = 33.58129/100

    def get_cost_usd_2016(self):
        return self.gdp_2016 * self.ratio
    
if __name__ == "__main__":
    cost_usd_2016 = GetStats().get_cost_usd_2016()
    print(cost_usd_2016)
