from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseIndex),
    path('signup/', views.new_User),
    path('login/', views.existing_User),
]
