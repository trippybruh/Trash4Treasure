from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseIndex),

    path('signup/', views.log_and_sign),
    path('signup/newuser/', views.registration),
    path('signup/newuser/<int:ec>', views.log_and_sign),
    path('signup/user/', views.dash_login),
    path('signup/user/<int:ec>', views.log_and_sign),

    path('signup/user/dash=<int:id>', views.account_org_buffed),
    path('signup/user/dash=<int:id>/<int:ec>', views.account_organizer),
    path('signup/user/dash=<int:id>/add', views.addPiece),

    path('dbadmin/', views.dbs_show),
    path('dbadmin/deleteUser/<int:id>', views.deleteUser),
    path('dbadmin/deletePiece/<int:id>', views.deletePiece),

    path('catalogueOverview/', views.catOverview),

    path('aboutT4T/', views.extra)
]
