from django.urls import path
from . import views, authViews

urlpatterns = [
    path('', views.baseIndex),

    path('signup/', views.logsign_page),
    path('signup/newuser/', views.sign_action),
    path('signup/user/', views.log_action),
    path('logout/', views.logout_action),

    path('signup/user/dash', views.account_organizer),
    path('signup/user/dash=<int:id>/add', views.addItem),

    path('dbadmin/', views.dbs_show),
    path('dbadmin/deleteUser/<int:id>', views.deleteUser),
    path('dbadmin/deleteDjangoUser/<int:id>', views.deleteDjangoUser),
    path('dbadmin/deletePiece/<int:id>', views.deletePiece),

    path('catalogue/', views.catBaseOverview),
    path('catalogue/search/', views.catalogueQuerySelection),

    path('aboutT4T/', views.extra)
]
