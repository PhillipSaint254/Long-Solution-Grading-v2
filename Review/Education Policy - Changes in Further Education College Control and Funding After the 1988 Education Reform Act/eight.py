from third import GetStats as GST

class GetStats(GST):
    def __init__(self):
        super().__init__()
        self.funding_diff = 1030.0 - 716.5
        self.staff_change = 26574 - 60227

if __name__ == "__main__":
    stats = GetStats()
    print(
        stats.funding_diff,
        stats.staff_change,
    )
