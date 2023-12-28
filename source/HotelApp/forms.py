from django.forms import ModelForm
from .models import *

        
class PackForm(ModelForm):
    class Meta:
        model = Pack
        fields = "__all__"
        
        
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        
class CategoryOptionForm(ModelForm):
    class Meta:
        model = CategoryOption
        fields = "__all__"
        
class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = "__all__"
