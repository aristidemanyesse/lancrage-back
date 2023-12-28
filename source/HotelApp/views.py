from django.shortcuts import render
from annoying.decorators import render_to

from HotelApp.models import CategoryOption, Option, Pack, Activity
# Create your views here.


@render_to('HotelApp/dashboard.html')
def dashboard(request):
    if request.method == "GET":
        ctx = {
            "packs" : packs
        }
        return ctx


@render_to('HotelApp/packs.html')
def packs(request):
    if request.method == "GET":
        packs = Pack.objects.filter(deleted = False)
        for pack in packs:
            pack.lesinclus = pack.inclus.split(';')
            
        ctx = {
            "packs" : packs
        }
        return ctx


@render_to('HotelApp/activities.html')
def activities(request):
    activites = Activity.objects.filter(deleted = False)
    for item in activites:
        item.lesprerequis = item.prerequis.split(';')
        
    if request.method == "GET":
        ctx = {
            "activites" : activites
        }
        return ctx


@render_to('HotelApp/options.html')
def options(request):
    categories = CategoryOption.objects.filter(deleted = False)
    options = Option.objects.filter(deleted = False)
    if request.method == "GET":
        ctx = {
            "categories" : categories,
            "options" : options,
        }
        return ctx