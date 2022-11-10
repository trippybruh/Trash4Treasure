from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseIndex),

    path('signup/', views.logsign_page),
    path('signup/newuser/', views.sign_action),
    path('signup/newrandomuser/', views.sign_action),  #to be removed eventually
    path('signup/user/', views.log_action),
    path('logout/', views.logout_action),

    path('signup/user/dash', views.account_organizer),
    path('signup/user/dash/add', views.addItem),
    path('signup/user/dash/addrandom', views.addItem), #to be removed eventually

    path('dbadmin/', views.dbs_show),
    path('dbadmin/deleteUser/<int:id>', views.deleteUser),
    path('dbadmin/deleteDjangoUser/<int:id>', views.deleteDjangoUser),
    path('dbadmin/deletePiece/<int:id>', views.deletePiece),
    path('dbadmin/deleteWatchlist/<int:id>', views.deleteWatchlist),

    path('catalogue/', views.catBaseOverview),
    path('catalogue/search/', views.catalogueQuerySelection),
    path('catalogue/addwatchlist/', views.addToWatchlist),
    path('catalogue/removewatchlist/', views.removeFromWatchlist),

    path('aboutT4T/', views.extra)
]
