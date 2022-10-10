from datetime import *
from django.db import models
from django.utils.timezone import now


class Users(models.Model):
    #porcodio non fa più
    nickname = models.CharField(max_length=50, unique=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(null=True, blank=True, default=now()) #account creation timestamp
    
    def __str__(self):
        return self.nickname

class Catalogue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    img = models.ImageField(null=True)
    nickname = models.ForeignKey(Users, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)
    next_owner = models.CharField(max_length=50, null=True)
    ads_published = models.DateTimeField(auto_created=True)
    ads_removed = models.DateTimeField(null=True)

    def __str__(self):
        return self.title



    


