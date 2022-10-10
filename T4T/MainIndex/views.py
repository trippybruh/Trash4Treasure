
from sqlite3 import IntegrityError
from django.template import loader
from django.urls import reverse
from django.http import *
from .models import Users, Catalogue
from django.views.decorators.csrf import csrf_exempt

#home
def BaseIndex(request):
    return HttpResponse(loader.get_template('MainIndex.html').render())

def extra(**kwargs):
    kwargs.get()
    return HttpResponse()

#log and sign up
def log_and_sign(request, **kwargs):

    ec = kwargs.get('ec')
    msg = 'No_msg'

    if ec != None:
        if ec == 4:
            msg = "Unexpected Database Error"
        elif ec == 5:
            msg = "Incorrect username/email or password"    
        elif ec == 0:
            msg = "Account successfully created! You are able to log in now!"
        elif ec == 1:
            msg = "Sorry, an account with this username or this email already exists!"
        elif ec == 2:
            msg = "Your passowrd is shorter than 6 chars or didn't match the password confirmation field!"
        elif ec == 3:
            msg = "Unexpected Database Error"    
    else: ec = -1

    context = {
        'ec' : ec,
        'msg' : msg
    }

    return HttpResponse(loader.get_template('DashAccess.html').render(context, request))

@csrf_exempt
def dash_login(request):

    if request.method == 'POST':
        try:
            nickname = request.POST.get('nickname')
            psw = request.POST.get('password')
            Allusers = Users.objects.all()
            for id in Allusers:
                if id.nickname == nickname or id.email == nickname:
                    if id.psw == psw:
                        return HttpResponseRedirect(f'dash={id.pk}')
                    else: 
                        break
            return HttpResponseRedirect('5')  
        except IntegrityError:  
            return HttpResponseRedirect('4')

#da fixare
@csrf_exempt
def registration(request):

    def isValid(nickname, email):

        Allusers = Users.objects.all()
        for id in Allusers:
            if id.nickname == nickname: return False
            if id.email == email: return False
        return True

    if request.method == 'POST':
        try:
            nickname = str(request.POST.get('nickname'))
            psw = str(request.POST.get('psw'))
            pswconf = str(request.POST.get('pswconf'))
            email = str(request.POST.get('email'))
            if psw == pswconf and len(psw) >= 6:
                if isValid(nickname, email):
                    new_reg = Users(nickname = nickname, psw = psw, email = email)
                    new_reg.save()
                    return HttpResponseRedirect('0')
                else: return HttpResponseRedirect('1') 
            else: return HttpResponseRedirect('2')
        except IntegrityError:
            return HttpResponseRedirect('3')

#user dash
def account_organizer(request, id):

    #get personal lists
    user = Users.objects.get(id=id)
    context = {
        'user' : user
    }
    return HttpResponse(loader.get_template('AccountDash.html').render(context, request))

#db control
def dbs_show(request):

    Allusers = Users.objects.all().values()
    context = {
        'Users': Allusers,
    }
    return HttpResponse(loader.get_template('DBcheck.html').render(context, request)) 

def deleteUser(request, id):

    user = Users.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse(dbs_show))   

#catalogue
def QueryCatalogue(request):
    pass


