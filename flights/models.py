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
    created_at = models.DateTimeField(default=datetime.now)
    
    
