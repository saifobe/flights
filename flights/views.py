from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
import requests
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

class EventList(APIView):
    

    def get(self, request):
        queryset = Event.objects.filter(country=request.GET.get('country'))
        date = queryset.first().created_at if queryset.exists() else None
        if date and date <= timezone.now() - timedelta(hours=6):
            queryset.filter(created_at__lte=timezone.now() - timedelta(hours=6)).delete()

        if queryset.exists():
            return Response({
                "status": "success",
                "data": queryset.values()
            })
        else:
                response = requests.get(
                url="https://api.predicthq.com/v1/events/",
                headers={
                    "Authorization": "Bearer EqpJf87ypBIW6cbbhkXRj_HOyxkNezMRw66NdI86",
                    "Accept": "application/json"
                },
                params={
                    "country": request.GET.get('country'),
                    "sort": "rank",
                    "limit": 10
                }
            )

                api_data = response.json()  # Get the data from the API response

                # Save the data in the database
                for data in api_data['results']:  # Assuming the data is in the 'results' key
                    event = Event(
                        id = data['id'],
                        title = data['title'],
                        description = data['description'],
                        rank = data['rank'],
                        country = data['country'],
                    )
                    event.save()
                    
                return Response(api_data)



