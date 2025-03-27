from django.urls import path
from . import views

urlpatterns = [
  path('', views.energy_forecast_view, name='energy_forecast'),
]