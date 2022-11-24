
from datetime import datetime
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.sessions.backends.db import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib.auth.decorators import *

from .basemodels import *
from .simulationShortcuts import add_random_item, register_random_user

#home/about pages
def baseIndex(request):
    print(f"\nsession user: {request.user}\n")  
    context = {
            'auth' : request.user.is_authenticated,
            'req_user': request.user,
    }
    return HttpResponse(loader.get_template('MainIndex.html').render(context, request))

def about(request):
    return HttpResponse(loader.get_template('AboutPage.html').render())

def faqs(request):
    return HttpResponse(loader.get_template('FaqsPage.html').render())

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

        context = {
            'ec' : kwargs.get('ec'),
            'msg' : set_msg(kwargs.get('ec')),
            'psw_safety':kwargs.get('psw_safety')
        }

        return HttpResponse(loader.get_template('DashAccess.html').render(context, request))
    else: return account_overviewer(request, ec=None)       

def log_action(request, **kwargs):

    if request.method == 'POST':
        try:            
            nickname = request.POST.get('nickname')
            psw = request.POST.get('psw')
            Allusers = Users.objects.all()
            for id in Allusers:
                if id.nickname == nickname or id.email == nickname:
                    if id.psw == psw:
                        id.make_login(request)
                        return account_overviewer(request, ec=None)
                    else: 
                        break
            return logsign_page(request, ec=5)  
        except Exception as e:  
            print(e)
            return logsign_page(request, ec=4)
    
    elif kwargs.get('randomRegistration'):
        user = authenticate(request, username = kwargs.get('nickname'), password = '123456')
        login(request, user)
        user.last_login = datetime.now()
        user.save()
        return account_overviewer(request, ec=None)

def sign_action(request):

    def isValid(nickname, email):

        for id in Users.objects.all():
            if id.nickname == nickname: return False
            if id.email == email: return False
        return True

    if request.method == 'POST':
        try:
            nickname = request.POST.get('nickname')
            psw = request.POST.get('psw')
            pswconf = request.POST.get('pswconf')
            country = request.POST.get('state')
            email = request.POST.get('email')
            if psw == pswconf and len(psw) >= 6:
                if isValid(nickname, email):
                    new_django_user = User.objects.create_user(nickname, email, psw, date_joined=datetime.now()) #django user model
                    new_watchlist = UsersWatchlist.objects.create(owner = new_django_user, owner_nn = nickname)
                    new_watchlist.setupList()
                    new_user = Users.objects.create(nickname = nickname, psw = psw, country = country, email = email,
                    django_model_user = new_django_user, watchlist=new_watchlist)  #my user model 

                    return logsign_page(request, ec=0, psw_safety = new_user.getPswSafety())
                else: return logsign_page(request, ec=1) 
            else: return logsign_page(request, ec=2)

        except Exception as e:
            print(e)
            return logsign_page(request, ec=3)
    
    else: return register_random_user(request)

@login_required(login_url='/signup/')
def logout_action(request):
    logout(request)
    return logsign_page(request, ec=-1)

#logged user personal dashboard
@login_required(login_url='/signup/')
def account_overviewer(request, **kwargs):

    ec = kwargs.get('ec')
    msg = None

    if ec != None:
        if ec == 0:
            msg = "Successfully added!"
        elif ec == 1:
            msg = "An error occurred!" 
        elif ec == 2:
            msg = "Sorry, you can add a maximum of 5 items per day to the catalogue!"   
    else: ec = -1

    context = {
        'auth' : True,
        'req_user': request.user,
        'user' : Users.objects.get(nickname=request.user),
        'ec' : ec,
        'msg' : msg
    }

    return HttpResponse(loader.get_template('AccountDash.html').render(context, request))

@login_required(login_url='/signup/')
def account_items_manager(request):

    if request.method == 'POST':
        action = request.POST.get('user_action')
        if action == 'edit':
            editItem(request)
        elif action == 'delete':
            deletethis = Catalogue.objects.get(pk=request.POST.get('item_id'))
            deletethis.delete()
    
    user = Users.objects.get(nickname=request.user)
    context = {
        'auth': True,
        'req_user' : request.user,
        'req_from' : 'dashboard',
        'items' : user.getUserItems(),
        'watchlist_items' : user.getUserWatchlist()
    }

    return HttpResponse(loader.get_template('AccountItems.html').render(context, request))

@login_required(login_url='/signup/')
def addItem(request):

    if request.method == 'POST':
        try:
            Django_publisher = User.objects.get(username=request.user)
            My_publisher = Users.objects.get(nickname=request.user)

            if My_publisher.added_today < My_publisher.MAX_ADDING:

                My_publisher.added_today += 1
                title = request.POST.get('title')
                description = request.POST.get('description')
                city = request.POST.get('city')
                region = request.POST.get('region')
                n_obj = request.POST.get('items_number')
                img = request.POST.get('image1')

                new_piece = Catalogue(title = title, description = description, img = img, publisher = Django_publisher, publisher_nn = Django_publisher.username, 
                geo_position = str(My_publisher.country + ", " + region + ", " + city), country = My_publisher.country, region = region, city = city, number_of_items = n_obj)

                if request.POST.get('item_tags') != None:
                    new_piece.item_tags = request.POST.get('item_tags')

                My_publisher.save()
                new_piece.save()

                return account_overviewer(request, ec=0)
            
            else: return account_overviewer(request, ec=2)
        
        except Exception as e:
            print(e)
            return account_overviewer(request, ec=1)
    
    else: return add_random_item(request)

@login_required(login_url='/signup/')
def editItem(request):
    if request.method == 'POST':
        pass #many shit

@login_required(login_url='/signup/')
def editAccount(request):

    def validEmail(new):
        for id in Users.objects.all():
            if id.email == new: return False
        return True

@login_required(login_url='/signup/')
def addToWatchlist(request):
    
    if request.method == 'POST':
        try:            
            user = Users.objects.get(nickname=request.POST.get('user_nn'))
            item = Catalogue.objects.get(id=request.POST.get('itemID'))
            if user.django_model_user is not item.publisher:
                updated = user.watchlist.updateAdding(item)
                if updated != "full" and updated:
                    user.save()
            else: updated = "is owner"      

            return catBaseOverview(request, msg=updated)

        except Exception as e:
            print(e)
            return catBaseOverview(request, watchlist_updated="Unexpected Error")

@login_required(login_url='/signup/')
def removeFromWatchlist(request):

    if request.method == 'POST':
        try:
            req_from = request.POST.get('req_from')
            user = Users.objects.get(nickname=request.POST.get('user_nn'))
            updated = user.watchlist.updateRemoving(Catalogue.objects.get(id=request.POST.get('itemID')))

            if updated != 'No such item' and updated:
                user.save()  
            
        except Exception as e:
            print(e)
        
        finally:
            if req_from == 'catalogue':
                return catBaseOverview(request, watchlist_updated=updated)
            elif req_from == 'dashboard':
                return account_items_manager(request)

#db control
def dbs_show(request):

    Allusers = Users.objects.all().values()
    Alldjangousers = User.objects.all().values()
    Allwatchlists = UsersWatchlist.objects.all().values()
    Allstuff= Catalogue.objects.all().values()

    context = {
        'MyUsers': Allusers,
        'DjangoUsers' : Alldjangousers,
        'watchlists' : Allwatchlists,
        'Stuff': Allstuff,
    }

    return HttpResponse(loader.get_template('DBcheck.html').render(context, request)) 

def deleteUser(request, id):

    Users.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deleteDjangoUser(request, id):

    User.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deletePiece(request, id):

    Catalogue.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse(dbs_show)) 

def deleteWatchlist(request, id):

    UsersWatchlist.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deleteAllItems(request):

    for id in Catalogue.objects.all():
        id.delete()
    return HttpResponseRedirect(reverse(dbs_show))

def deleteAllData(request):

    for id in User.objects.all():
        id.delete()
    return HttpResponseRedirect(reverse(dbs_show))

#catalogue
def catBaseOverview(request, **kwargs):

    def set_msg(msg):
        if msg:
            return "Saved!"
        elif not msg:
            return "Unexpected Error!"
        elif msg == 'item not found':
            return "Looks like this item was already removed from your watchlist!"    
        elif msg == 'full':
            return "Your watchlist is full, remove something to add a new item!"
        elif msg == 'is owner':
            return "You already own this item! You can only add to your watchlist other user's items!"
        else: return None

    if kwargs.get('search') != None and request.user.is_authenticated:
        context = {
            'auth' : True,
            'req_user': request.user,
            'req_from': 'catalogue',
            'watchlist_items': Users.objects.get(nickname=request.user).getUserWatchlist(),
            'search': kwargs.get('search'),
            'search_type': kwargs.get('search_type'),
            'sort_type':kwargs.get('sort_type'),
            'items' : kwargs.get('items'),
            'Nitems': kwargs.get('items').count()
        }

    elif kwargs.get('search') != None and not request.user.is_authenticated:
        context = {
            'auth' : False,
            'search': kwargs.get('search'),
            'search_type': kwargs.get('search_type'),
            'sort_type':kwargs.get('sort_type'),
            'items' : kwargs.get('items'),
            'Nitems': kwargs.get('items').count()
        }

    elif kwargs.get('search') == None and request.user.is_authenticated:    
        context = {
            'auth' : True,
            'req_user': request.user,
            'req_from': 'catalogue',
            'msg' : set_msg(kwargs.get('msg')),
            'watchlist_items': Users.objects.get(nickname=request.user).getUserWatchlist(),
            'search': None,
            'items' : Catalogue.objects.all(),
            'Nitems': Catalogue.objects.all().count()
        }
    
    elif kwargs.get('search') == None and not request.user.is_authenticated:
        context = {
            'auth' : False,
            'search': None,
            'items' : Catalogue.objects.all(),
            'Nitems': Catalogue.objects.all().count()
        }

    return HttpResponse(loader.get_template('BaseCatalogue.html').render(context, request))  

def catalogueQuerySelection(request):

    def sortQueryBy(sort_type, query):
    
        if sort_type != 'newest':
            if sort_type == 'oldest':
                query = query.order_by('-ads_published')
            elif sort_type == 'score':
                pass    
            elif sort_type == 'near by':
                pass

        return query
    
    if request.method == 'GET':
        try:
            query = Catalogue.objects
            user_searched = request.GET.get('search')
            search_type = request.GET.get('search_type')
            sort_type = request.GET.get('sort_type')

            if search_type != 'by title':
                if search_type == 'by descriptions':
                    query = query.filter(Q(title__icontains=user_searched) | Q(description__icontains=user_searched))
                elif search_type == 'by location':
                    query = query.filter(Q(geo_position__icontains=user_searched))
                elif search_type == 'by publisher':
                    query = query.filter(Q(publisher_nn__icontains=user_searched))
            else: query = query.filter(Q(title__icontains=user_searched))

            if sort_type == 'oldest':
                query = query.order_by('-ads_published')
    
            return catBaseOverview(request, items=query, search=user_searched, search_type=search_type, sort_type=sort_type)

        except Exception as e:
            print(e)    
