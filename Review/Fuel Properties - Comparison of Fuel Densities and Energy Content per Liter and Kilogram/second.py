from first import GetStats as gst

class GetStats(gst):
    def __init__(self):
        super().__init__()
        self.density_jet = 0.8
        self.energy_per_kg_jet = self.energy_jet / self.density_jet

    def show_energy_per_kg_jet(self):
        print(self.energy_per_kg_jet)

if __name__ == "__main__":
    stats = GetStats()
    stats.show_energy_per_kg_jet()
