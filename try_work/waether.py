import requests

API_KEY = "0ae4f4f993a253baf072ea68bf532392"  # use one of the keys you see in your dashboard
CITY = "Abenase"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code != 200:
    print("Error:", data.get("message", "Something went wrong"))
else:
    location = data["name"]
    country = data["sys"]["country"]
    temp_c = data["main"]["temp"]
    condition = data["weather"][0]["description"]

    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
