from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services import WeatherService
from .models import WeatherData
import os


# Create your views here.

@login_required
def weather_data_view(request):
    api_key = os.getenv('WEATHERSTACK_API_KEY')
    if not api_key:
        return render(request, 'dashboard/weather_data.html', {
            'error': 'WeatherStack API key not configured'
        })

    if request.method == 'POST':
        location = request.POST.get('location')
        try:
            weather_service = WeatherService(api_key)
            weather_data = weather_service.fetch_weather_data(location)
            
            # Save weather data based on WeatherStack API response structure
            weather_entry = WeatherData.objects.create(
                user=request.user,
                location=location,
                temperature=weather_data['current']['temperature'],
                humidity=weather_data['current']['humidity'],
                wind_speed=weather_data['current']['wind_speed'],
                solar_radiation=0  # WeatherStack doesn't provide solar radiation
            )
            
            return render(request, 'dashboard/weather_data.html', {
                'weather_data': weather_entry
            })
        except Exception as e:
            return render(request, 'dashboard/weather_data.html', {
                'error': str(e)
            })
    
    return render(request, 'dashboard/weather_data.html')