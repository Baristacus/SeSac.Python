import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Seoul", "appid": API_KEY, "units": "metric", "lang": "kr"}

response = requests.get(url, params=params)
response.raise_for_status()

wether_Date = response.json()
city_name = wether_Date["name"]
temperature = wether_Date["main"]["temp"]
description = wether_Date["weather"][0]["description"]


print(f"도시: {city_name}")
print(f"온도: {temperature}")
print(f"날씨: {description}")
