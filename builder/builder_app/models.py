from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    
    user = models.ForeignKey(User)
    
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=1000)
    
    members = models.ManyToManyField(User, verbose_name="members", related_name="project_members")
    followers = models.ManyToManyField(User, verbose_name="followers", related_name="project_followers")
    

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    bio = models.CharField(max_length=1000)
    
    website = models.CharField(max_length=255)
    blog = models.CharField(max_length=255)


class Comment(models.Model):
    
    text = models.CharField(max_length=512)
    project = models.OneToOneField(Project)
    user = models.OneToOneField(User)


class Message(models.Model):
    
    sender = models.OneToOneField(User, related_name="message_sender")
    receiver = models.OneToOneField(User, related_name="message_receiver")
    text = models.CharField(max_length=1000)
