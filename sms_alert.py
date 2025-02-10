from twilio.rest import Client
import requests 

API_KEY = "your_api_key"
location = "city_name"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"

response = requests.get(url)
weather_data = response.json()

crop_thresholds = {
    {"Crop": "Arecanut", "Minimum Rainfall (mm)": 750, "Maximum Rainfall (mm)": 4500},
    {"Crop": "Other Kharif Pulses", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Rice", "Minimum Rainfall (mm)": 544, "Maximum Rainfall (mm)": 2775},
    {"Crop": "Banana", "Minimum Rainfall (mm)": 1700, "Maximum Rainfall (mm)": 2500},
    {"Crop": "Cashewnut", "Minimum Rainfall (mm)": 600, "Maximum Rainfall (mm)": 1200},
    {"Crop": "Coconut", "Minimum Rainfall (mm)": 1000, "Maximum Rainfall (mm)": 3000},
    {"Crop": "Dry Ginger", "Minimum Rainfall (mm)": 1500, "Maximum Rainfall (mm)": 3000},
    {"Crop": "Sugarcane", "Minimum Rainfall (mm)": 1400, "Maximum Rainfall (mm)": 3500},
    {"Crop": "Sweet Potato", "Minimum Rainfall (mm)": 750, "Maximum Rainfall (mm)": 1200},
    {"Crop": "Tapioca", "Minimum Rainfall (mm)": 1000, "Maximum Rainfall (mm)": 1500},
    {"Crop": "Black Pepper", "Minimum Rainfall (mm)": 2000, "Maximum Rainfall (mm)": 3000},
    {"Crop": "Dry Chillies", "Minimum Rainfall (mm)": 600, "Maximum Rainfall (mm)": 1200},
    {"Crop": "Other Oilseeds", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Turmeric", "Minimum Rainfall (mm)": 1000, "Maximum Rainfall (mm)": 2000},
    {"Crop": "Maize", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Moong (Green Gram)", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Urad", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Arhar/Tur", "Minimum Rainfall (mm)": 600, "Maximum Rainfall (mm)": 1000},
    {"Crop": "Bajra", "Minimum Rainfall (mm)": 250, "Maximum Rainfall (mm)": 500},
    {"Crop": "Castor Seed", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Cotton (Lint)", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 1500},
    {"Crop": "Groundnut", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Horse Gram", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Jowar", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Korra", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Masoor", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Ragi", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Sesamum", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Sunflower", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 750},
    {"Crop": "Wheat", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 1500},
    {"Crop": "Samai", "Minimum Rainfall (mm)": 400, "Maximum Rainfall (mm)": 750},
    {"Crop": "Onion", "Minimum Rainfall (mm)": 350, "Maximum Rainfall (mm)": 500},
    {"Crop": "Coriander", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 600},
    {"Crop": "Potato", "Minimum Rainfall (mm)": 500, "Maximum Rainfall (mm)": 600}

}

rainfall = weather_data["list"][0]["rain"] if "rain" in weather_data["list"][0] else 0

if rainfall < crop_thresholds[crop]["min_rainfall"]:
    alert_message = f" Low rainfall detected! Irrigation needed for {crop}."
elif rainfall > crop_thresholds[crop]["max_rainfall"]:
    alert_message = f" Excessive rainfall! Ensure proper drainage for {crop}."
else:
    alert_message = f" Rainfall is within the safe range for {crop}."

account_sid = "twilio_sid"
auth_token = "twilio_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=alert_message,
    from_= +18314005233,
    to=farmer_number
)

print(" SMS Sent Successfully! Message SID:", message.sid)
