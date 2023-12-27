
from .models import *
from rest_framework.serializers import ModelSerializer


class ChambreSerializer(ModelSerializer):
    class Meta:
        model = Chambre
        fields = '__all__'

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class PredictionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

