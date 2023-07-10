from django.urls import path
from .views import EventList, WeatherList, FlightList



urlpatterns = [
    path('events/', EventList.as_view(), name='event_detail'),
    path('weather/', WeatherList.as_view(), name='weather_detail'),
    path('flights/', FlightList.as_view(), name='flight_detail'),
]