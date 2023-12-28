from graphene_django_extras import  DjangoSerializerType
from .serializers import *


class ReservationType(DjangoSerializerType):
    class Meta:
        serializer_class = ReservationSerializer
        description = " Type definition for a single Reservation "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("exact",),
        }

