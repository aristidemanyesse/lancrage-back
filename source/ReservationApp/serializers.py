
from .models import *
from rest_framework.serializers import ModelSerializer


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

