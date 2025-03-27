from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class WeatherData(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='weather_data'
    )
    location = models.CharField(max_length=200)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    solar_radiation = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.timestamp}"