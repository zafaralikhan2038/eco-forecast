import requests
from geopy.geocoders import Nominatim

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherstack.com/current"
        self.geolocator = Nominatim(user_agent="renewable_energy_prediction")
    
    def get_coordinates(self, location):
        try:
            location_data = self.geolocator.geocode(location)
            return location_data.latitude, location_data.longitude
        except Exception as e:
            raise ValueError(f"Could not find coordinates for {location}: {e}")
    
    def fetch_weather_data(self, location):
        try:
            lat, lon = self.get_coordinates(location)
            params = {
                'access_key': self.api_key,
                'query': f"{lat},{lon}",
                'units': 'm'  # Metric units
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise RuntimeError(f"Error fetching weather data: {e}")