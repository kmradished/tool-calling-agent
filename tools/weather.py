import requests
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    получает текущую погоду по названию города
    """
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "ru",
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if "results" not in geo_data or not geo_data["results"]:
        return f"не удалось найти город: {city}"

    place = geo_data["results"][0]

    latitude = place["latitude"]
    longitude = place["longitude"]
    city_name = place["name"]
    country = place["country"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "timezone": "auto",
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_response.raise_for_status()
    weather_data = weather_response.json()

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    weather_code = current["weather_code"]

    return (
        f"погода в городе {city_name}, {country}: "
        f"температура {temperature}°C, "
        f"скорость ветра {wind_speed} км/ч, "
        f"код погоды {weather_code}"
    )