from django.urls import path
from .views import EventList, WeatherList



urlpatterns = [
    path('v1/events/', EventList.as_view(), name='event_detail'),
    path('v1/weather/', WeatherList.as_view(), name='weather_detail'),
]