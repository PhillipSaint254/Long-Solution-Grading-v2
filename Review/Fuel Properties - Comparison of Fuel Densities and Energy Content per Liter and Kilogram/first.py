class GetStats:
    def __init__(self):
        self.density_diesel = 0.832 # kg/L
        self.energy_diesel = 35.86 # MJ/L
        self.density_petrol = 0.745 # kg/L
        self.energy_petrol = 32.18 # MJ/L
        self.density_unleaded = 0.745 # same as petrol (assuming)
        self.energy_unleaded = 33.526 # from BTS 33,526 kJ/L = 33.526 MJ/L
        self.density_jet = 0.81 # typical mid from 775-840 ~0.8075 -> 0.81
        self.energy_jet = 37.627 # MJ/L from BTS
        self.energy_per_kg_diesel = self.energy_diesel / self.density_diesel
        self.energy_per_kg_petrol = self.energy_petrol / self.density_petrol
        self.energy_per_kg_unleaded = self.energy_unleaded / self.density_unleaded
        self.energy_per_kg_jet = self.energy_jet / self.density_jet
    
    def __str__(self):
        return f"{self.density_diesel, self.energy_per_kg_diesel, self.density_petrol, self.energy_per_kg_petrol, self.density_unleaded, self.energy_per_kg_unleaded, self.density_jet, self.energy_per_kg_jet}"
    
if __name__ == "__main__":
    print(GetStats())
