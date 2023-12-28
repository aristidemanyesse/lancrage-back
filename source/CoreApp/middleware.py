
import datetime
import uuid, pytz
from django.shortcuts import redirect
from django.utils.timezone import make_aware
from CoreApp import tools
from django.utils import translation


class LockoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response     

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.path_info)
        if not request.path_info.startswith('/gestion/organisation/ajax/mycomte/'):
            if '/admin/' not in request.path_info and '/auth/' not in request.path_info and '/graphql/' not in request.path_info:
                if 'locked' in request.session:
                    if request.session['locked'] :
                        return redirect("auth:locked")
                if not request.user.is_authenticated:
                    return redirect("auth:login")



class  AccessCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response    

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.path_info.startswith('/gestion/organisation/ajax/mycomte/'):
            if len(request.path_info.split("/")) >= 2:
                request.module_name = request.path_info.split("/")[1]
                
                if len(request.path_info.split("/")) >= 3:
                    try:
                        test = uuid.UUID(request.path_info.split("/")[3], version=4)
                    except:
                        test = False
                    if len(request.path_info.split("/")) >= 4 and request.path_info.split("/")[3] != "" and not test:
                        request.page_name = request.path_info.split("/")[3]
                    else:
                        request.page_name = request.path_info.split("/")[2] if request.path_info.split("/")[2] != "" else "dashboard_"+request.module_name
