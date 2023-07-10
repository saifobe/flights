from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event, Weather, Flight
import requests
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone
import json



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

                api_data = response.json() 

                
                for data in api_data['results']:  
                    event = Event(
                        id = data['id'],
                        title = data['title'],
                        description = data['description'],
                        rank = data['rank'],
                        country = data['country'],
                        location_x = data['location'][0],
                        location_y = data['location'][1],
                    )
                    event.save()
                    
                return Response(api_data)

class WeatherList(APIView):
     def get(self, request):
        queryset = Weather.objects.filter(id=request.GET.get('id'))
        event = Event.objects.get(id=request.GET.get('id'))
        date = queryset.first().created_at if queryset.exists() else None
        if date and date <= timezone.now() - timedelta(hours=6):
            queryset.filter(created_at__lte=timezone.now() - timedelta(hours=6)).delete()
        
        
        if queryset.exists():
            return Response(queryset.values())
        else:
            response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={event.location_y}&lon={event.location_x}&appid=f22892654725839a44ff6db985f0b151",
            )
            

            api_data = response.json()

            humidity = api_data.get("main", {}).get("humidity")
            temperature = api_data.get("main", {}).get("temp")

            if humidity is not None and temperature is not None:
                weather = Weather(
                    id=event,
                    humidity=humidity,
                    temperature=temperature,
                )
                weather.save()
                return Response(
                    Weather.objects.filter(id=request.GET.get("id")).values()
                )
            else:
                return Response({"message": "Failed to retrieve weather data"})
            
            

class FlightList(APIView):

    def get_nearby_airport(self, event):
        lat = event.location_y
        lon = event.location_x
        url = f'https://airlabs.co/api/v9/nearby?lat={lat}&lng={lon}&distance=200&api_key=27325f7b-d13d-473a-b9ae-c3f8e2f21585'
        response = requests.get(url)
        api_data = response.json()
        most_nearby_airport = None
        if response.status_code == 200:

            for airoprt in api_data['response']['airports']:
                if most_nearby_airport is None:
                    most_nearby_airport = airoprt
                elif airoprt['distance'] < most_nearby_airport['distance']:
                    most_nearby_airport = airoprt
                
        return most_nearby_airport



    def get(self, request):

        id = request.GET.get('id')
        airport_code = request.GET.get('airport_code')
        
        queryset = Flight.objects.filter(event=id)
        event = Event.objects.get(id=id)
        nearest_ariport = FlightList.get_nearby_airport(self, event)
        if nearest_ariport is None:
            return Response({
                "status": "error",
                "message": "No nearby airport found"
            })


        date = queryset.first().created_at if queryset.exists() else None
        
        if date and date <= timezone.now() - timedelta(hours=6):
            queryset.filter(created_at__lte=timezone.now() - timedelta(hours=6)).delete()
        
        if queryset.exists():
            return Response(queryset.values())
        
        else:
            event = Event.objects.get(id=id)
            # Retrieve the flights based on the event location and user's airport code from AirLabs API
            url_going = f'https://airlabs.co/api/v9/schedules?dep_icao={airport_code}&arr_icao={nearest_ariport["icao_code"]}&api_key=27325f7b-d13d-473a-b9ae-c3f8e2f21585'
            url_back = f'https://airlabs.co/api/v9/schedules?dep_icao={nearest_ariport["icao_code"]}&arr_icao={airport_code}&api_key=27325f7b-d13d-473a-b9ae-c3f8e2f21585'
            response_going = requests.get(url_going)
            response_back = requests.get(url_back)
            
            if response_going.status_code == 200 and response_back.status_code == 200:
                api_data_going = response_going.json()
                api_data_back = response_back.json()
                
                
                # Parse the flight data and save it to the Flight model

                flights = []
                print(api_data_going["response"])

                for flight_data in api_data_going["response"]:
                    flight = Flight(
                        event=event,
                        airport_code=flight_data['airline_icao'],
                        flight_number=flight_data['flight_number'],
                        departure_time=flight_data['dep_time_utc'],
                        arrival_time=flight_data['arr_time_utc']
                    )
                    flights.append(flight)

                for flight_data in api_data_back["response"]:
                    flight = Flight(
                        event=event,
                        airport_code=flight_data['airline_icao'],
                        flight_number=flight_data['flight_number'],
                        departure_time=flight_data['dep_time_utc'],
                        arrival_time=flight_data['arr_time_utc']
                    )
                    flights.append(flight)
                
                Flight.objects.bulk_create(flights)
                
                return Response(Flight.objects.filter(event=id, airport_code=airport_code).values())
            
            else:
                return Response({"message": "Failed to retrieve flights from AirLabs API"}, status=response_going.status_code)

     
     
     

