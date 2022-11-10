import random
from .basemodels import *
from . import views


def add_random_item(request):

    titles = ['divano anni 30', 'frigo stondato stile americano', 'poltrona della nonna morta', 'tostapane che tosta peni', 'tavolo sgozzapolli poco usato', 'televisore anni 50 che da la scossa']
    regions = ['Lombardia', 'Piemonte', 'Veneto', 'Toscana', 'Emilia-Romagna', 'Lazio', 'Campania', 'Puglia', 'Sicilia', 'Sardegna']

    title = random.choice(titles)
    description = "this auto add function doesnt provide any random description, also because ad's title it's been tweaked to be self explaining and there is no need for me to keep going writing this text string but Im doing it anyway to get a better sense of how a long description would look like!"
    city = "Alberobello"
    region = random.choice(regions)
    n_obj = random.randint(1, 10)
    Django_publisher = User.objects.get(username=request.user)
    My_publisher = Users.objects.get(nickname=request.user)

    new_piece = Catalogue(title = title, description = description, publisher = Django_publisher, publisher_nn = Django_publisher.username, 
    geo_position = str(My_publisher.country + ", " + region + ", " + city), country = My_publisher.country, region = region, city = city, number_of_items = n_obj)
    new_piece.save()

    return views.account_organizer(request, ec=0)

def register_random_user(request): #riusabile per generare istanze utente random per le chat di utenti non registrati

    nicknames = ['gilberto', 'marcovaldo', 'pippobamba', 'bigdickjoe', 'nikthequick', 'samirhashmaster']
    emails = ['@gmail.com', '@hotmail.it', '@yahoo.com']

    nickname = random.choice(nicknames) + str(random.randint(0, 1000)) #1 pos su 6000 che generi un nome uguale ad uno esistente
    psw = '123456'
    country = 'Italy'
    email = nickname + random.choice(emails)

    new_django_user = User.objects.create_user(nickname, email, psw, date_joined=datetime.now()) #django user model
    new_watchlist = UsersWatchlist.objects.create(owner = new_django_user, owner_nn = nickname) 
    new_watchlist.setupList()
    Users.objects.create(nickname = nickname, psw = psw, country = country, email = email, django_model_user = new_django_user, watchlist=new_watchlist) #my user model

    return views.log_action(request, randomRegistration=True, nickname=nickname)
        
    
