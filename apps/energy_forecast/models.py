from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class EnergyForecast(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='energy_forecasts'
    )
    location = models.CharField(max_length=200)
    forecast_date = models.DateField()
    predicted_solar_output = models.FloatField()
    predicted_wind_output = models.FloatField()
    confidence_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.forecast_date}"