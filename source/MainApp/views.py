from django.shortcuts import render
from annoying.decorators import render_to
# Create your views here.


def dashboard(request):
    return 

@render_to('MainApp/dashboard.html')
def dashboard(request):
    if request.method == "GET":
        ctx = {
            "officines" : "officines"
        }
        return ctx