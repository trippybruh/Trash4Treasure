from django.utils import timezone
from django.db import models


class Users(models.Model):

    nickname = models.CharField(max_length=50, unique=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(default=timezone.now()) #account creation timestamp

class Catalogue(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    img = models.ImageField(null=True)
    item_tags = models.CharField(max_length=300, default='Unspecified')
    geo_position = models.CharField(max_length=50, default='Unspecified')

    publisher = models.ForeignKey(Users, on_delete=models.CASCADE)
    publisher_nn = models.CharField(null=True, max_length=50)

    ads_published = models.DateTimeField(default=timezone.now())
    ads_removed = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True)
    next_owner = models.CharField(max_length=50, null=True, blank=True)




    


