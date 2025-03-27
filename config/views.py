# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     """
#     Render the index page for the wind-solar-prediction app.
#     """
#     features = [
#         {
#             'icon': 'fas fa-cloud',
#             'title': 'Weather Data Integration',
#             'description': 'Advanced collection and processing of weather forecast data'
#         },
#     ]
#     return render(request, 'index.html', {'features': features})

from django.shortcuts import render

def index(request):
    """
    Render the index page for the wind-solar-prediction app.
    """
    features = [
        {
            'icon': 'fas fa-cloud',
            'title': 'Weather Data Integration',
            'description': 'Advanced collection and processing of multi-source weather forecast data, ensuring comprehensive environmental insights.'
        },
        {
            'icon': 'fas fa-chart-line',
            'title': 'Predictive Analytics',
            'description': 'Machine learning algorithms that provide accurate short-term and long-term renewable energy production forecasts.'
        },
        {
            'icon': 'fas fa-solar-panel',
            'title': 'Renewable Asset Optimization',
            'description': 'Intelligent recommendations for solar panel and wind turbine placement based on predictive modeling.'
        },
        {
            'icon': 'fas fa-network-wired',
            'title': 'Grid Integration',
            'description': 'Seamless energy production predictions to optimize grid management and reduce supply fluctuations.'
        },
        {
            'icon': 'fas fa-leaf',
            'title': 'Sustainability Metrics',
            'description': 'Comprehensive CO2 reduction tracking and environmental impact assessment for renewable energy projects.'
        },
        {
            'icon': 'fas fa-globe',
            'title': 'Global Data Insights',
            'description': 'Real-time global renewable energy trends and location-specific performance analytics.'
        }
    ]
    return render(request, 'index.html', {'features': features})