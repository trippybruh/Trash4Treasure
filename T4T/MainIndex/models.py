
from django.db import models


class Users(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    created = models.TimeField() #account creation timestamp
    
    def __str__(self):
        return self.nickname

class Catalogue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    img = models.ImageField(null=True)
    nickname = models.ForeignKey(Users, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)
    next_owner = models.CharField(max_length=50, null=True)
    ads_published = models.TimeField(auto_created=True)
    ads_removed = models.TimeField(null=True)

    def __str__(self):
        return self.title



    


