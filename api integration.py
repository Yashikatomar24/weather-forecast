import requests                                                                                                                                                                                              import requests
import datetime

API_KEY = "YOUR_API_KEY"
CITY = "city_name"
URL = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={CITY}&cnt=16&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    
    city_name = data["city"]["name"]
    country = data["city"]["country"]
    print(f" Weather Forecast for {city_name}, {country}\n")

    for day in data["list"]:
        date = datetime.datetime.fromtimestamp(day["dt"]).strftime('%Y-%m-%d')
        temp_day = day["temp"]["day"]
        temp_min = day["temp"]["min"]
        temp_max = day["temp"]["max"]
        weather_desc = day["weather"][0]["description"].capitalize()
        
        print(f" {date}: {weather_desc}")
        print(f"   Temp: {temp_day} Celcius (Min: {temp_min} Celsius, Max: {temp_max} Celcius)\n")

else:
    print(" Error: Unable to fetch data. Check API key or request parameters.")