from statsmodels.tsa.seasonal import seasonal_decompose
from five import get_monthly_avg
import pandas as pd

# Decompose monthly average time series
def get_seasonal():
    monthly_avg = get_monthly_avg()
    ts = monthly_avg
    ts.index = pd.DatetimeIndex(ts.index)  # ensure index is datetime
    result = seasonal_decompose(ts, model='additive', period=12)  # 12-month seasonality
    return result.seasonal

if __name__ == "__main__":
    seasonal = get_seasonal()
    print(seasonal.head(15), seasonal.tail(5))
