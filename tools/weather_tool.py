import requests
import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {
            "error": "WEATHER_API_KEY not set"
        }

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    # Handle API error responses safely
    if "main" not in data:
        return {
            "error": data.get("message", "Unable to fetch weather data"),
            "raw_response": data
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
