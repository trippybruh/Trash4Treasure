from datetime import datetime
from django.db import models
from django.contrib.auth.models import *

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
symbols = ["!", '|', '"', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^', 'à', 'è', 'ì', 'ò', 'ù', ',', '.', '_', ':', ';', '<', '>', '+', '§', '#', '@', '*', '°', 'ç']

class Catalogue(models.Model):

    #object informations
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.ImageField(null=True) #fixare img source
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

    class Meta:
        managed = True

class UsersWatchlist(models.Model):

    #owner
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_nn = models.CharField(max_length=50, unique=True)

    #content
    watchlist_items = models.IntegerField(default=0)
    item1 = models.ForeignKey(Catalogue, on_delete=models.DO_NOTHING, null=True)
    item2 = models.ForeignKey(Catalogue, on_delete=models.DO_NOTHING, null=True)
    item3 = models.ForeignKey(Catalogue, on_delete=models.DO_NOTHING, null=True)
    item4 = models.ForeignKey(Catalogue, on_delete=models.DO_NOTHING, null=True)
    item5 = models.ForeignKey(Catalogue, on_delete=models.DO_NOTHING, null=True)

    all_items = []

    def getUsefullList(self):
        return self.all_items

    def setupList(self):

        self.item1 = None
        self.item2 = None
        self.item3 = None
        self.item4 = None
        self.item5 = None
        self.watchlist_items = 0
        self.all_items = [None, None, None, None, None]
        self.save()
    
    def updateList(self, new_item):
        try:
            free = -1
            for x in range(len(self.all_items)):
                if self.all_items[x] == None:
                    free = x
                    break

            if free == 0:
                self.item1 = new_item
            elif free == 1:
                self.item2 = new_item
            elif free == 2:
                self.item3 = new_item
            elif free == 3:
                self.item4 = new_item
            elif free == 4:
                self.item5 = new_item

            self.all_items.insert(free+1, new_item)
            self.watchlist_items += 1
            new_item.popularity += 1

            new_item.save()
            self.save()
            return True

        except ValueError:
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

    #watchlist
    watchlist = models.ForeignKey(UsersWatchlist, on_delete=models.DO_NOTHING, null=True)

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

    class Meta:
        managed = True

    
 