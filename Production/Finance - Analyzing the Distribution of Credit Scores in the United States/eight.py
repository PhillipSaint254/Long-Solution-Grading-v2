from seven import get_deviles_data, get_percentages
from _six import get_arr_rand
import pandas as pd

arr_rand = get_arr_rand()
_, deciles_vals = get_deviles_data()
percentages = get_percentages()

lower_bounds = [arr_rand.min()] + list(deciles_vals)  # now length 10

upper_bounds = list(deciles_vals) + [arr_rand.max()]

decile_rows = []
for i in range(10):
    row = {
        'Decile': i+1,
        'Score range': f"{lower_bounds[i]:.0f}–{upper_bounds[i]:.0f}",
        'Percent of scores': f"{percentages[i]:.1f}%"
    }
    decile_rows.append(row)

decile_df = pd.DataFrame(decile_rows)

print(decile_df)
