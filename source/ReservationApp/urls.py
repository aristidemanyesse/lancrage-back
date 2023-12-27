from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import settings
from .views import *


app_name = "ReservationApp"
urlpatterns = [
    path('lists/', lists, name="lists"),
]