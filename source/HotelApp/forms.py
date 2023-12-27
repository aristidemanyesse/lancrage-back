from django.forms import ModelForm
from .models import *

        
# Create the form class.
class PackForm(ModelForm):
    class Meta:
        model = Pack
        fields = "__all__"
        
        
# Create the form class.
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
