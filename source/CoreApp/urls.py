
from django.urls import path
from . import ajax
from django.views.decorators.csrf import csrf_exempt

app_name = "core"
urlpatterns = [
    path('ajax/save/', ajax.save, name="save"),
    path('ajax/mise_a_jour/', ajax.mise_a_jour, name="mise_a_jour"),
    path('ajax/supprimer/', ajax.supprimer, name="supprimer"),
    path('ajax/change_active/', ajax.change_active, name="change_active"),
    path('ajax/filter_date/', ajax.filter_date, name="filter_date"),
    path('ajax/session/', csrf_exempt(ajax.session), name="session"),
    path('ajax/delete_session/', csrf_exempt(ajax.delete_session), name="delete_session"),
    path('ajax/change_language/', ajax.change_language, name="change_language"),

]
