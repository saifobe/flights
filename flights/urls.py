from django.urls import path
from .views import EventList



urlpatterns = [
    path('v1/events/', EventList.as_view(), name='event_detail'),
]