import pandas as pd

# Let's construct the URL for the HMDA data subset CSV.
# We'll use 2022, states=CA, actions_taken=1

url = 'https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=CA&years=2022&actions_taken=1'

# Let's fetch a portion? The API streams the entire CSV. We need to load all? It might be big.
# We will try to read directly with pandas, which supports streaming.
# But we need to be careful about memory/time limits.

# Let's check how large a file with these filters is by downloading the first few rows.

import requests
