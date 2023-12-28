from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, logout
from annoying.decorators import render_to

import datetime
from django.shortcuts import redirect
from django.utils.timezone import make_aware
# Create your views here.

@render_to('auth/pages/login.html')
def login(request):
    if request.method == "GET":
        logout(request)
        return {}
        

def locked(request):
    if request.method == "GET":
        request.session['locked'] = True
        if "last_url" not in request.session:
            request.session['last_url'] = request.META["HTTP_REFERER"]
        return render(request, "auth/pages/locked.html")



def reset(request):
    return render(request, "auth/pages/reset.html")



def expiration(request):
    if request.mycompte.expiration >= make_aware(datetime.datetime.now()):
        return redirect("auth:login")
    return render(request, "auth/pages/expiration.html")


def disconnect(request):
    logout(request)
    return redirect("auth:login")




###################################################################################################

def handler404(request, exception):
    return render(request, 'acces/pages/404.html')


def handler400(request, exception):
    return render(request, 'acces/pages/400.html')


def handler500(request):
    return render(request, 'acces/pages/500.html')