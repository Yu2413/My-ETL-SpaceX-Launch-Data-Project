import requests
import pandas as pd

API_URL = "https://api.spacexdata.com/v4/launches"
data2 = requests.get(API_URL).json()

df = pd.json_normalize(data2) # flatten nested JSON

print(df.columns[:10]) # show sample columns

df_success = df[df["success"] == True] # filter successful launches

print(df_success.head())
print(f"Successful launches: {len(df_success)}.")

df_failures = df[df["success"] == False] # filter unsuccessful launches

print(df_failures.head())
print(f"Unsuccessful launches: {len(df_failures)}.")










