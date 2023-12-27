from django.shortcuts import render
from annoying.decorators import render_to
# Create your views here.

@render_to('ReservationApp/lists.html')
def lists(request):
    if request.method == "GET":
        ctx = {
            "officines" : "officines"
        }
        return ctx