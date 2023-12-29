
from django.urls import path
from . import views 
from . import ajax 

app_name = "auth"
urlpatterns = [
    path('', views.login),
    path('login/', views.login, name="login"),
    path('locked/', views.locked, name="locked"),
    path('disconnect/', views.disconnect, name="disconnect"),
    # path('forgetpassword/', views.forgetpassword, name="forgetpassword"),
    path('reset/', views.reset, name="reset"),
    path('expiration/', views.expiration, name="expiration"),


    path('ajax/connexion/', ajax.connexion),
    path('ajax/first_user/', ajax.first_user),
    path('ajax/unlocked/', ajax.unlocked),
    # path('ajax/forgetpassword/', ajax.forgetpassword),
    # path('ajax/reset/', ajax.reset),

]
