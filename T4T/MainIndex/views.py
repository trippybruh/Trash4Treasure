

from datetime import datetime
from sqlite3 import IntegrityError
from django.template import loader
from django.urls import reverse
from django.http import *
from .models import Users, Catalogue
from django.views.decorators.csrf import csrf_exempt

#home
def BaseIndex(request):
    return HttpResponse(loader.get_template('MainIndex.html').render())

#log and sign up
def new_User(request):
    return HttpResponse(loader.get_template('AccountCreation.html').render())

#da fixare
@csrf_exempt
def registrion(request):
    if request.method == 'POST':
        try:
            now = datetime.now()
            nickname = request.POST.get('nickname')
            psw = request.POST.get('psw')
            pswconf = request.POST.get('pswconf')
            email = request.POST.get('email')
            if psw == pswconf and len(psw) >= 6:
                new_reg = Users(nickname = nickname, psw = psw, email = email, created = now)
                new_reg.save()
            else: pass #display error message to user    
        except IntegrityError:
            print("Some shit didn't got added to database!\n")
        finally:
            return HttpResponseRedirect(reverse(BaseIndex))

def existing_User(request):
    return HttpResponse(loader.get_template('Login.html').render())

#user dash
def account_dash(request):
    pass

#db control
def dbs_show(request):
    Allusers = Users.objects.all().values()
    template = loader.get_template('DBcheck.html')
    context = {
        'Users': Allusers,
    }
    return HttpResponse(template.render(context, request)) 

def delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse(dbs_show))   

def QueryCatalogue(request):
    pass


