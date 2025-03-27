# Construct the data
data = [
    {'id':'Zw1ucZEqQ78','year':2020,'views':30863,'likes':2072,'comments':446},
    {'id':'xoi9omtAiNQ','year':2020,'views':132053,'likes':7755,'comments':1041},
    {'id':'NXYHwHRa5Ks','year':2021,'views':195510,'likes':6750,'comments':1300},
    {'id':'Xdf41gsESTc','year':2021,'views':15005,'likes':464,'comments':107},
    {'id':'5D86_ptqd8I','year':2022,'views':3232,'likes':358,'comments':55},
    {'id':'NzahTmBpVq8','year':2023,'views':223570,'likes':3940,'comments':641},
    {'id':'oZuVgb04S3U','year':2024,'views':61836,'likes':2887,'comments':939},
    {'id':'N2XzPByJmkc','year':2024,'views':10764,'likes':716,'comments':170},
    {'id':'421RyqJ5__4','year':2024,'views':45228,'likes':1901,'comments':745},
]

import pandas as pd

df = pd.DataFrame(data)

print(df)

df_grouped = df.groupby('year').agg(
    videos=('id','count'),
    avg_views=('views','mean'),
    avg_likes=('likes','mean'),
    avg_comments=('comments','mean')
).reset_index()

print(df_grouped)
