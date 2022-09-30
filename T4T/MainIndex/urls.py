from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseIndex),
    path('signup/', views.new_User),
    path('signup/newuser/', views.registrion),
    path('login/', views.existing_User),
    path('dbadmin/', views.dbs_show),
    path('dbadmin/delete/<int:id>', views.delete)
]
