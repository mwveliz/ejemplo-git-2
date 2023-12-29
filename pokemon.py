import requests
#import pandas as pd
url = "https://pokeapi.co/api/v2/pokemon?limit=12"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.text
#df = pd.DataFrame(data['results'])
#print(df)


