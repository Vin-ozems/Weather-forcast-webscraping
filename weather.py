import requests
import pandas as pd
import csv  

API_KEY = "1d3601caa02fc9c973503176859f0b44"
OWN_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

Kaduna_lat_lon_params = {
    "lat": 10.531850,
    "lon": 7.429470,
    "appid": API_KEY
}

response = requests.get(url=OWN_API_ENDPOINT, params=Kaduna_lat_lon_params)
response.raise_for_status()
data = response.json()

# Convert forecast list to DataFrame
data_new = pd.DataFrame(data["list"])

# Save JSON objects in 'list' directly as CSV rows
with open("weather_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data_new.columns)
    writer.writeheader()

    for _, row in data_new.iterrows():
        writer.writerow(row.to_dict())


    
