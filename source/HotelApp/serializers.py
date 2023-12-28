
from .models import *
from rest_framework.serializers import ModelSerializer


class PackSerializer(ModelSerializer):
    class Meta:
        model = Pack
        fields = '__all__'

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class CategoryOptionSerializer(ModelSerializer):
    class Meta:
        model = CategoryOption
        fields = '__all__'


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

