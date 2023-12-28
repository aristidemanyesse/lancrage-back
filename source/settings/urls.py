"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


def home(request):
    if request.user.is_authenticated:
        return redirect("gestion/")
    return redirect("auth/login/")



urlpatterns = [
    path('', home),
    path('auth/', include("AuthApp.urls")),
    path('core/', include('CoreApp.urls')),
    path('gestion/', include("HotelApp.urls")),
    path('reservations/', include("ReservationApp.urls")),
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'AuthApp.views.handler404'
handler400 = 'AuthApp.views.handler400'
handler500 = 'AuthApp.views.handler500'
