from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseIndex),

    path('signup/', views.log_and_sign),
    path('signup/newuser/', views.registration),
    path('signup/newuser/<int:ec>', views.log_and_sign),
    path('signup/user/', views.dash_login),
    path('signup/user/<int:ec>', views.log_and_sign),

    path('signup/user/dash=<int:id>', views.account_organizer),

    path('dbadmin/', views.dbs_show),
    path('dbadmin/delete/<int:id>', views.deleteUser),

    path('aboutT4T/', views.extra)
]
