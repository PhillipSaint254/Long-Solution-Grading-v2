import numpy as np, pandas as pd
from second import get_tables

tables = get_tables()
regular_season = tables[1]

# Weighted average using GP as weight for key stats
stats_cols = ['PPG','RPG','APG','SPG','BPG','MPG']
weights = regular_season['GP']

# We'll group by NAME; for each group compute weighted average across teams using GP as weights.
def weighted_avg(group, col):
    return np.average(group[col], weights=group['GP'])

def get_agg_dict():
    return {col: (lambda x, col=col: np.average(x, weights=regular_season.loc[x.index, 'GP'])) for col in stats_cols}

# Actually we can't define this this way; we just groupby then apply.
def get_player_agg():
    return regular_season.groupby('NAME').apply(lambda g: pd.Series({col: weighted_avg(g, col) for col in stats_cols + []}, name=g.name))

if __name__ == "__main__":
    print(get_player_agg().head())
