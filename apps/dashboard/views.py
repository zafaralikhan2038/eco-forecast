from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg, Max, Min, Sum

from apps.weather.models import WeatherData
from apps.energy_forecast.models import EnergyForecast

@login_required
def dashboard_index(request):
    """
    Render the dashboard with recent weather data, energy forecasts, and aggregated insights.
    """
    # Get recent data (last 24 hours)
    twenty_four_hours_ago = timezone.now() - timedelta(hours=24)
    
    recent_weather = WeatherData.objects.filter(
        user=request.user, 
        timestamp__gte=twenty_four_hours_ago
    ).order_by('-timestamp')[:10]
    
    recent_forecasts = EnergyForecast.objects.filter(
        user=request.user, 
        timestamp__gte=twenty_four_hours_ago
    ).order_by('-timestamp')[:10]
    
    # Calculate some additional insights
    context = {
        'recent_weather': recent_weather,
        'recent_forecasts': recent_forecasts,
        'weather_insights': {
            'avg_temperature': recent_weather.aggregate(Avg('temperature'))['temperature__avg'] or 0,
            'max_temperature': recent_weather.aggregate(Max('temperature'))['temperature__max'] or 0,
            'min_temperature': recent_weather.aggregate(Min('temperature'))['temperature__min'] or 0,
        },
        'energy_insights': {
            'total_solar_output': recent_forecasts.aggregate(Sum('predicted_solar_output'))['predicted_solar_output__sum'] or 0,
            'total_wind_output': recent_forecasts.aggregate(Sum('predicted_wind_output'))['predicted_wind_output__sum'] or 0,
        }
    }
    
    return render(request, 'dashboard/index.html', context)


def register_view(request):
    """
    Handle user registration with validation and automatic login.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard:index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})