import uuid
from django.db import models
from CoreApp.models import BaseModel

# Create your models here.
class Pack(BaseModel):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name        = models.CharField(max_length=255)
    price       = models.IntegerField(default = 0)
    nbre_lit    = models.IntegerField(default = 0)
    superficie  = models.IntegerField(default = 0)
    modele_lit  = models.CharField(max_length=255)
    inclus      = models.TextField(max_length=255)
    image      = models.ImageField(max_length = 255, upload_to = "images/pack/", default='images/pack/default.png', null = True, blank=True)



    def __str__(self):
        return self.name



class Activity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    

class Option(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name