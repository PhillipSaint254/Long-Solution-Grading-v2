from second import GetStats as GST

class GetStats(GST):
    def get_staff_1987(self):
        return round(super().get_staff_1987())
    
    def get_staff_1989(self):
        return round(super().get_staff_1989())
    
if __name__ == "__main__":
    stats = GetStats()
    print(
        stats.get_staff_1987(),
        stats.get_staff_1989()
    )
