from graphene_django_extras import  DjangoSerializerType
from .serializers import *


class PackType(DjangoSerializerType):
    class Meta:
        serializer_class = PackSerializer
        description = " Type definition for a single Pack "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("exact",),
        }



class ActivityType(DjangoSerializerType):
    class Meta:
        serializer_class = ActivitySerializer
        description = " Type definition for a single Activity "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("exact",),
        }


class CategoryOptionType(DjangoSerializerType):
    class Meta:
        serializer_class = CategoryOptionSerializer
        description = " Type definition for a single CategoryOption "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "name": ("exact",),
        }


class OptionType(DjangoSerializerType):
    class Meta:
        serializer_class = OptionSerializer
        description = " Type definition for a single Option "
        filter_fields = {
            "id": ("exact", ),
            "deleted": ("exact", ),
            "categorie__id": ("exact",),
            "name": ("exact", ),
        }
