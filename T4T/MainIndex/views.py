
from django.template import loader
from django.http import *
from .models import Users

def BaseIndex(request):
    return HttpResponse(loader.get_template('MainIndex.html').render())

def new_User(request):
    return HttpResponse(loader.get_template('AccountCreation.html').render())

def existing_User(request):
    return HttpResponse(loader.get_template('Login.html').render())

def GetAllUsers(request):
    users = Users.objects.all()    

def QueryCatalogue(request):
    pass
