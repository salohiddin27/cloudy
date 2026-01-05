from django.db import models
class Weather(models.Model):
    city = models.CharField(max_length=222)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    humidity = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} {self.temperature}"