from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    
    user = models.OneToOneField(User)
    
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=1000)
    