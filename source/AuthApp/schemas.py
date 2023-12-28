from graphene_django_extras import  DjangoSerializerType
from .serializers import *


class EmployeType(DjangoSerializerType):
    class Meta:
        serializer_class = EmployeSerializer
        description = " Type definition for a single Employe "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "username": ("exact",),
        }

