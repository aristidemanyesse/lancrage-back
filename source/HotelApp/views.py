from django.shortcuts import render
from annoying.decorators import render_to

from HotelApp.models import Pack
# Create your views here.


@render_to('HotelApp/packs.html')
def packs(request):
    if request.method == "GET":
        packs = Pack.objects.filter(deleted = False)
        ctx = {
            "packs" : packs
        }
        return ctx


@render_to('HotelApp/activities.html')
def activities(request):
    if request.method == "GET":
        ctx = {
            "officines" : "officines"
        }
        return ctx