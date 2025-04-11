import numpy as np
from third import get_monthly_arpu, get_months

def get_data():
    np.random.seed(0)  # for reproducibility
    num_users = 100

    months = get_months()
    monthly_arpu = get_monthly_arpu()

    data = []
    for date, avg in zip(months, monthly_arpu):
        # standard deviation 20% of ARPU
        std = 0.2 * avg
        # sample 100 values from normal distribution
        spend = np.random.normal(loc=avg, scale=std, size=num_users)
        # clip to positive
        spend = np.clip(spend, 0, None)
        for s in spend:
            data.append({'date': date, 'spend': s})
    return data

if __name__ == "__main__":
    data = get_data()
    print(len(data))
