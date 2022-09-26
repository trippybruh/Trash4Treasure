from django.db import models

class Users(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    created = models.TimeField(auto_created=True) #account creation timestamp
    dofb = models.DateTimeField() #date of birth


