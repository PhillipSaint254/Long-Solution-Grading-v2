import pandas as pd, numpy as np, re, sys, textwrap, math
from first import get_tables

tables = get_tables()
regular_season = tables[1]

# check duplicates of 'NAME'
print(regular_season['NAME'].value_counts().head())
