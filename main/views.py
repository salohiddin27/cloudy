import requests
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Weather


def get_weather(request):
    api_key = "40f58efdfdcf4500ac2112814251010"
    city = request.GET.get('q', 'Tashkent')

    url = "http://api.weatherapi.com/v1/current.json"
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

    # db ga saqlash
    Weather.objects.create(
        city=city_name,
        temperature=temp_c,
        condition=condition,
        wind_speed=wind_speed,
        humidity=humidity,
        created_at=created_at,

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
    return HttpResponseNotFound('Sorry, the request resource was not found,\nyou must write (login or weather) ', status=404)
