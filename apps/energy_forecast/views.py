from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import EnergyForecastService
from .models import EnergyForecast
from apps.weather.models import WeatherData
from datetime import date

@login_required
def energy_forecast_view(request):
    if request.method == 'POST':
        # Get latest weather data for the user
        latest_weather = WeatherData.objects.filter(user=request.user).latest('timestamp')

        try:
            forecast_service = EnergyForecastService()
            
            # Prepare weather features
            weather_features = [[
                latest_weather.temperature,
                latest_weather.humidity,
                latest_weather.wind_speed,
                latest_weather.solar_radiation
            ]]
            
            # Predict energy output
            solar_output, wind_output = forecast_service.predict_energy_output(weather_features)
            
            # Save forecast
            forecast = EnergyForecast.objects.create(
                user=request.user,
                location=latest_weather.location,
                forecast_date=date.today(),
                predicted_solar_output=solar_output,
                predicted_wind_output=wind_output,
                confidence_score=0.85  # Fixed for simplicity
            )
            
            return render(request, 'dashboard/energy_forecast.html', {
                'forecast': forecast
            })

        except Exception as e:
            return render(request, 'dashboard/energy_forecast.html', {
                'error': str(e)
            })

    return render(request, 'dashboard/energy_forecast.html')
