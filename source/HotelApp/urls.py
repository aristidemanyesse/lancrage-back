from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import settings
from .views import *


app_name = "HotelApp"
urlpatterns = [
    path('packs/', packs, name="packs"),
    path('activities/', activities, name="activities"),
]