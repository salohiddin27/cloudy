import os

import requests
from django.http import HttpResponseNotFound
from django.shortcuts import render
from dotenv import load_dotenv
from .models import Weather

load_dotenv()

def get_weather(request):
    api_key = os.getenv("API_KEY")
    city = request.GET.get('q', 'Tashkent')

    url = os.getenv("URL")
    params = {"key": api_key,
              "q": city,
              }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return render(request, 'weather.html', {"error": "Weather API error"})

    data = response.json()

    city_name = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    wind_speed = data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]
    created_at = data["location"]["localtime"]

    Weather.objects.create(
        city=city_name,
        temperature=temp_c,
        condition=condition,
        wind_speed=wind_speed,
        humidity=humidity,

    )
    weather_data = {
        "city": city_name,
        "temperature": temp_c,
        "condition": condition,
        "wind_speed": wind_speed,
        "humidity": humidity,
        "created_at": created_at,
    }

    return render(request, 'weather.html', {'weather': weather_data})


def custom_404_view(request, exception=None):
    return HttpResponseNotFound('Sorry, the request resource was not found,you must write (login or weather) ', status=404)

