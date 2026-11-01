import requests

URL="https://stephen-king-api.onrender.com/api/books"
req=requests.get(URL)
req
'''Response [200]'''
req.json()

import pandas as pd
pd.json_normalize(data['data'])