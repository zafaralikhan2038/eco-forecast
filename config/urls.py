# from django.contrib import admin
# from django.urls import path, include
# from .views import index

# urlpatterns = [
#     # Index page
#     path('', index, name='index'),
    
#     # Admin site
#     path('admin/', admin.site.urls),
    
#     # Authentication URLs
#     path('auth/', include('apps.accounts.urls')),
    
#     # App URLs
#     path('dashboard/', include('apps.dashboard.urls')),
#     path('weather/', include('apps.weather.urls')),
#     path('forecast/', include('apps.energy_forecast.urls')),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from .views import index

# urlpatterns = [
#     # Index page
#     path('', index, name='index'),
    
#     # Admin site
#     path('admin/', admin.site.urls),
    
#     # Authentication URLs
#     path('auth/', include('apps.accounts.urls')),
    
#     # App URLs
#     path('dashboard/', include('apps.dashboard.urls')),
#     path('weather/', include('apps.weather.urls')),
#     path('forecast/', include('apps.energy_forecast.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    # Index page
    path('', index, name='index'),
    
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('auth/', include(('apps.accounts.urls', 'accounts'), namespace='auth')),
    
    # App URLs
    path('dashboard/', include(('apps.dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('weather/', include(('apps.weather.urls', 'weather'), namespace='weather')),
    path('forecast/', include(('apps.energy_forecast.urls', 'forecast'), namespace='forecast')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
