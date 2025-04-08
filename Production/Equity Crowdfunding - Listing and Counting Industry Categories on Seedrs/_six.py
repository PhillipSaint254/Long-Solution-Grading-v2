import pandas as pd, json, textwrap, math, numpy as np, re, pandas as pd
from fifth import get_unique_categories

unique_categories = get_unique_categories()
print(pd.DataFrame({'Industry Category (Seedrs)': unique_categories}))
