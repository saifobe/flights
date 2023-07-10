from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


# Create your models here.

class Event(models.Model):
    id = models.CharField(max_length = 100, primary_key = True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rank = models.IntegerField(max_length=100)
    country = models.CharField(max_length=100)
    location_x = models.FloatField(max_length=255)
    location_y = models.FloatField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    
    

class Weather(models.Model):
    id = models.ForeignKey(Event, on_delete=models.CASCADE, primary_key=True)
    humidity = models.IntegerField(max_length=100)
    temperature = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

class Flight(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    airport_code = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now)


    
    
