from seven import get_avg_all
from second import get_avg_days

class GetStats:
    def __init__(self):
        avg_all = get_avg_all()
        self.avg_years = avg_all / 365
        self.avg_months = avg_all / 30

    def __str__(self):
        return f"{self.avg_years, self.avg_months}"
    
if __name__ == "__main__":
    stats = GetStats()
    avg_days = get_avg_days()
    avg_months = stats.avg_months
    avg_years = stats.avg_years
    print(avg_days, avg_years, avg_months)
