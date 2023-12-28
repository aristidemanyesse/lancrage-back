
from .models import *
from rest_framework.serializers import ModelSerializer


class EmployeSerializer(ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

