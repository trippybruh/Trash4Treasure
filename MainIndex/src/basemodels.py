from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import *
from django.contrib.auth.models import *
from . import views

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
symbols = ["!", '|', '"', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^', 'à', 'è', 'ì', 'ò', 'ù', ',', '.', '_', ':', ';', '<', '>', '+', '§', '#', '@', '*', '°', 'ç']

class Catalogue(models.Model):

    #object informations
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='userItems/', default='userItems/default-placeholder.png', null=True) #fixare img source
    number_of_items = models.IntegerField(null=True)
    item_tags= models.TextField(null=True)
    
    #location info
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    geo_position = models.CharField(max_length = 250, null=True)

    #owner
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publisher_nn = models.CharField(null=True, max_length=50)

   #additional data
    popularity = models.BigIntegerField(default=0)
    ads_published = models.DateTimeField(default=datetime.now())
    ads_removed = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True)
    next_owner = models.CharField(max_length=50, null=True, blank=True)

    def updateObj(self, **kwargs):

        #edit info
        if kwargs.get('title') != None:
            self.title = kwargs.get('title')
        if kwargs.get('description') != None:
            self.description = kwargs.get('description')
        if kwargs.get('img') != None:
            self.img = kwargs.get('img')
        if kwargs.get('number_of_items') != None:
            self.number_of_items = kwargs.get('number_of_items')
        if kwargs.get('item_tags') != None:
            self.item_tags = kwargs.get('item_tags')
        
        #edit location
        if kwargs.get('city') != None:
            self.city = kwargs.get('city')
            self.save()
            self.geo_position = str(self.country + ", " + self.region + ", " + self.city)
        if kwargs.get('region') != None:
            self.region = kwargs.get('region')
            self.save()
            self.geo_position = str(self.country + ", " + self.region + ", " + self.city)
        
        self.save()

    @property
    def get_img(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        
    class Meta:
        managed = True

class UsersWatchlist(models.Model):

    #owner
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_nn = models.CharField(max_length=50, unique=True)

    #content
    watchlist_items = models.IntegerField(default=0)
    item1 = models.ForeignKey(Catalogue, on_delete=models.SET(None), null=True)
    item2 = models.ForeignKey(Catalogue, on_delete=models.SET(None), null=True)
    item3 = models.ForeignKey(Catalogue, on_delete=models.SET(None), null=True)
    item4 = models.ForeignKey(Catalogue, on_delete=models.SET(None), null=True)
    item5 = models.ForeignKey(Catalogue, on_delete=models.SET(None), null=True)

    all_items = []

    def getUsefullList(self):
        return self.all_items

    def setupList(self):

        self.item1 = None
        self.item2 = None
        self.item3 = None
        self.item4 = None
        self.item5 = None
        self.save()
    
    def updateAdding(self, new_item):
        try:
            if isinstance(new_item, Catalogue):
                
                if not isinstance(self.item1, Catalogue):
                    self.item1 = new_item
                elif not isinstance(self.item2, Catalogue):
                    self.item2 = new_item
                elif not isinstance(self.item3, Catalogue):
                    self.item3 = new_item
                elif not isinstance(self.item4, Catalogue):
                    self.item4 = new_item
                elif not isinstance(self.item5, Catalogue):
                    self.item5 = new_item
                else: return "full"       

                self.all_items.append(new_item)
                self.watchlist_items += 1
                new_item.popularity += 1

                new_item.save()
                self.save()
                return True

            else: return False

        except Exception as e:
            print(e)
            return False

    def updateRemoving(self, item):
        try:
            if isinstance(item, Catalogue):

                if item == self.item1:
                    self.item1 = None
                elif item == self.item2:
                    self.item2 = None
                elif item == self.item3:
                    self.item3 = None
                elif item == self.item4:
                    self.item4 = None
                elif item == self.item5:
                    self.item5 = None
                else: return 'item not found'

                self.all_items.remove(item)
                self.watchlist_items -= 1
                item.popularity -= 1

                item.save()
                self.save()
                return True

            else: return False

        except Exception as e:
            print(e)
            return False

class Users(models.Model):

    #base info
    nickname = models.CharField(max_length=50, unique=True)
    psw = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=30)
    django_model_user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #additional info
    created = models.DateTimeField(default=datetime.now()) 
    bio = models.CharField(max_length=500, null=True)

    #watchlist and added items
    watchlist = models.ForeignKey(UsersWatchlist, on_delete=models.DO_NOTHING, null=True)
    last_added = Catalogue.objects.filter(publisher_nn=nickname).last()
    added_today = 0
    MAX_ADDING = 5 #max items to be added per day

    def getPswSafety(self): #from 0 to 100 
    
        score = len(self.psw) #min score is 7 
        for x in numbers:
            try:
                if self.psw.index(x) < 51:
                    score += 1
            except ValueError:
                continue
        
        for x in alphabet:
            try:
                if self.psw.index(x) < 51:
                    score += 1
            except ValueError:
                continue

        for x in alphabet:
            try:
                if self.psw.index(x.upper()) < 51:
                    score += 1
            except ValueError:
                continue

        for x in symbols:
            try:
                if self.psw.index(x) < 51:
                    score += 2
            except ValueError:
                continue

        print(score)
        if score < 10:
            return "very weak"
        elif 10 <= score < 18:
            return "weak"
        elif 18 <= score <= 30:
            return "normal"
        elif 30 < score <= 50:
            return "strong"
        elif score > 50:
            return "very strong"

    def getUserItems(self):
        return Catalogue.objects.filter(publisher_nn=self.nickname)

    def getUserWatchlist(self):
        return self.watchlist.getUsefullList()

    def updateUser(self, **kwargs):

        if kwargs.get('new_psw') != None and len(kwargs.get('new_psw')) >= 6:
            self.psw = kwargs.get('new_psw')
        if kwargs.get('email') != None:
            self.email = kwargs.get('email')
        if kwargs.get('bio') != None:
            self.bio = kwargs.get('bio')

        self.save()

    def make_login(self, request):
        login(request, authenticate(request, username = self.nickname, password = self.psw))
        if (self.django_model_user.last_login + timedelta(hours=24)) <= datetime.now():
            self.added_today = 0
        self.django_model_user.last_login = datetime.now()
        self.django_model_user.save()
        self.save()

    class Meta:
        managed = True

    
 