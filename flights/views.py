from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
import requests

# Create your views here.

class EventList(APIView):
    queryset = Event.objects.all()
    def get(self, request, format=None):
        response = requests.get(
        url="https://api.predicthq.com/v1/events/",
        headers={
        "Authorization": "Bearer $EqpJf87ypBIW6cbbhkXRj_HOyxkNezMRw66NdI86",
        "Accept": "application/json"
        },
        params={
            "id": "5uRg7CqGu7DTtu4Rfk"
        }
        )

        return(response.json())
        


