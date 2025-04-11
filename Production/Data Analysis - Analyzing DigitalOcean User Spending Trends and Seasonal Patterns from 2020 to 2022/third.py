from second import get_arpu_quarter
from first import get_months

def get_arpu_for_date(date):
    arpu_quarter = get_arpu_quarter()
    year = date.year
    month = date.month
    q = (month-1)//3 + 1
    key = f"{year}Q{q}"
    return arpu_quarter[key]

def get_monthly_arpu():
    months = get_months()
    return [get_arpu_for_date(m) for m in months]

if __name__ == "__main__":
    monthly_arpu = get_monthly_arpu()
    print(monthly_arpu[:12], len(monthly_arpu))
    