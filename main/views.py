from django.shortcuts import render
from django.http import HttpResponseNotFound
from .services import fetch_weather

def get_weather(request):
    city = request.GET.get('q', 'Tashkent')
    try:
        weather_data = fetch_weather(city)
    except Exception as e:
        return render(request, 'weather.html', {"error": str(e)})

    return render(request, 'weather.html', {'weather': weather_data})

def custom_404_view(request, exception=None):
    return HttpResponseNotFound(
        'Resource not found. You must write /login or /weather', status=404
    )
