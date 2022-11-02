
from datetime import datetime
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.decorators import *

from .models import Users, Catalogue

#home/about pages
def baseIndex(request, **kwargs):
    print(f"\nsession user: {request.user}\n")  
    
    context = {
            'auth' : request.user.is_authenticated,
            'req_user': request.user,
    }
    return HttpResponse(loader.get_template('MainIndex.html').render(context, request))

def extra(request, **kwargs):
    return HttpResponse(loader.get_template('AboutPage.html').render())

#log and sign views/logic
def logsign_page(request, **kwargs):

    def set_msg(ec):
        if ec != None:
            if ec == -1:
                msg = "You just logged out!"
            elif ec == 0:
                msg = "Account successfully created! You are able to log in now!"
            elif ec == 1:
                msg = "Sorry, an account with this username or this email already exists!"
            elif ec == 2:
                msg = "Your passowrd is shorter than 6 chars or didn't match the password confirmation field!"
            elif ec == 3 or ec == 4:
                msg = "Unexpected Error!"
            elif ec == 5:
                msg = "Incorrect username/email or password!"    
        else:
            msg = None

        return msg
    
    if not request.user.is_authenticated:
        ec = kwargs.get('ec')

        context = {
            'ec' : ec,
            'msg' : set_msg(ec)
        }

        return HttpResponse(loader.get_template('DashAccess.html').render(context, request))
    else: return account_organizer(request, nickname=request.user, ec=None)       

def log_action(request):

    if request.method == 'POST':
        try:            
            nickname = request.POST.get('nickname')
            psw = request.POST.get('psw')
            Allusers = Users.objects.all()
            for id in Allusers:
                if id.nickname == nickname or id.email == nickname:
                    if id.psw == psw:
                        user = authenticate(request, username = nickname, password = psw)
                        login(request, user)
                        user.last_login = datetime.now()
                        return account_organizer(request, nickname=id.nickname, ec=None)
                    else: 
                        break
            return logsign_page(request, ec=5)  
        except Exception as e:  
            print(e)
            return logsign_page(request, ec=4)

def sign_action(request):

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
            country = str(request.POST.get('state'))
            email = str(request.POST.get('email'))
            if psw == pswconf and len(psw) >= 6:
                if isValid(nickname, email):
                    new_user = User.objects.create_user(nickname, email, psw, date_joined=datetime.now())   #django user model
                    Users(nickname = nickname, psw = psw, country = country, email = email, django_model_user = new_user).save() #my user model                    
                    return logsign_page(request, ec=0)
                else: return logsign_page(request, ec=1) 
            else: return logsign_page(request, ec=2)
        except Exception as e:
            print(e)
            return logsign_page(request, ec=3)

#logged user personal dashboard
@login_required(login_url='/signup/')
def account_organizer(request, **kwargs):

    ec = kwargs.get('ec')
    msg = None

    if ec != None:
        if ec == 0:
            msg = "Successfully added!"
        elif ec == 1:
            msg = "An error occurred!"    
    else: ec = -1

    context = {
        'auth' : True,
        'req_user': request.user,
        'user' : Users.objects.get(nickname=kwargs.get('nickname')),
        'ec' : ec,
        'msg' : msg
    }

    return HttpResponse(loader.get_template('AccountDash.html').render(context, request))

@login_required(login_url='/signup/')
def addItem(request, id):

    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            city = request.POST.get('city')
            region = request.POST.get('region')
            n_obj = request.POST.get('items_number')
            publisher = Users.objects.get(id=id)

            new_piece = Catalogue(title = title, description = description, publisher = publisher, publisher_nn = publisher.nickname, 
            geo_position = str(publisher.country + ", " + region + ", " + city), country = publisher.country, region = region, city = city, number_of_items = n_obj)

            if request.POST.get('item_tags') != None:
                new_piece.item_tags = request.POST.get('item_tags')

            new_piece.save()
            return account_organizer(request, nickname=publisher.nickname, ec=0)
        
        except Exception as e:
            print(e)
            return account_organizer(request, nickname=publisher.nickname, ec=1)

@login_required(login_url='/signup/')
def logout_action(request):
    logout(request)
    return logsign_page(request, ec=-1)

#db control
def dbs_show(request):

    Allusers = Users.objects.all().values()
    Alldjangousers = User.objects.all().values()
    Allstuff= Catalogue.objects.all().values()

    context = {
        'MyUsers': Allusers,
        'DjangoUsers' : Alldjangousers,
        'Stuff': Allstuff,
    }

    return HttpResponse(loader.get_template('DBcheck.html').render(context, request)) 

def deleteUser(request, id):

    user = Users.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deleteDjangoUser(request, id):

    user = User.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deletePiece(request, id):

    piece = Catalogue.objects.get(id=id)
    piece.delete()
    return HttpResponseRedirect(reverse(dbs_show)) 

#catalogue
def catBaseOverview(request, **kwargs):

    if kwargs.get('search') != None:
        context = {
            'auth' : request.user.is_authenticated,
            'req_user': request.user,
            'search': kwargs.get('search'),
            'search_type': kwargs.get('search_type'),
            'items' : kwargs.get('items')
        }
    else:    
        context = {
            'auth' : request.user.is_authenticated,
            'req_user': request.user,
            'search': 'No search',
            'items' : Catalogue.objects.all().values()
        }

    return HttpResponse(loader.get_template('BaseCatalogue.html').render(context, request))

def sortCatBy(request, **kwargs):
    
    if request.method == 'GET':
        try:
            req_items = Catalogue.objects
            field = kwargs.get('field')
            if kwargs.get('field_value') == None:
                req_items.all().order_by(field)
            else:
                if field == 'geo_position':
                    req_items.filter(geo_position=kwargs.get('field_value')).values()

            context = {
                    'items' : req_items
                }        

            return HttpResponse(loader.get_template('BaseCatalogue.html').render(request, context))

        except Exception as e:
            print(e)          

def catalogueQuerySelection(request):
    
    if request.method == 'GET':
        try:
            query = Catalogue.objects
            user_searched = request.GET.get('search')
            search_type = request.GET.get('search_type')
            if search_type != 'default':
                if search_type == 'by descriptions':
                    query = query.filter(Q(title__contains=user_searched) | Q(description__contains=user_searched)).values()
                elif search_type == 'by location':
                    query = query.filter(Q(geo_position__contains=user_searched)).values()
                elif search_type == 'by publisher':
                    query = query.filter(Q(publisher_nn__contains=user_searched)).values()
            else: query = query.filter(Q(title__contains=user_searched)).values()
            
            return catBaseOverview(request, search=user_searched, search_type=search_type, items=query)

        except Exception as e:
            print(e)    




