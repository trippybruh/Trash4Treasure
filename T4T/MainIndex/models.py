from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import *


class Users(models.Model):

    #base info
    nickname = models.CharField(max_length=50, unique=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=30)
    django_model_user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #additional info
    created = models.DateTimeField(default=datetime.now()) 
    bio = models.CharField(max_length=500, null=True)
    wishlist = models.TextField(null=True)

    class Meta:
        managed = True    

class Catalogue(models.Model):

    #object informations
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    img = models.ImageField(null=True) #fixare img source
    number_of_items = models.IntegerField(null=True)
    item_tags= models.TextField(null=True)
    
    #location info
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    geo_position = models.CharField(max_length=255)

    #owner
    publisher = models.ForeignKey(Users, on_delete=models.CASCADE)
    publisher_nn = models.CharField(null=True, max_length=50)

   #additional data
    ads_published = models.DateTimeField(default=datetime.now())
    ads_removed = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True)
    next_owner = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = True



    


