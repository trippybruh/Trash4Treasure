from django import forms
from .models import Users, Catalogue

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['nickname', 'psw', 'email']

class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = ['title', 'description', 'item_tags', 'geo_position']
