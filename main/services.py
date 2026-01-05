import os
import requests
from django_redis import get_redis_connection
from .models import Weather

redis_client = get_redis_connection("default")

def fetch_weather(city: str):
    cache_key = f"weather:{city.lower()}"
    cached = redis_client.get(cache_key)
    if cached:
        return eval(cached)

    api_key = os.getenv("API_KEY")
    url = os.getenv("URL")
    params = {"key": api_key, "q": city}

    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        raise Exception("Weather API error")

    data = response.json()
    weather_data = {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "wind_speed": data["current"]["wind_kph"],
        "humidity": data["current"]["humidity"],
        "created_at": data["location"]["localtime"]
    }

    Weather.objects.create(
        city=weather_data["city"],
        temperature=weather_data["temperature"],
        condition=weather_data["condition"],
        wind_speed=weather_data["wind_speed"],
        humidity=weather_data["humidity"],
    )

    redis_client.set(cache_key, str(weather_data), ex=600)

    return weather_data
