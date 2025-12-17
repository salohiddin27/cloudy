from rest_framework import serializers

from .models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        models = Weather
        fields = "__all__"
