import uuid
from django.db import models
from CoreApp.models import BaseModel

# Create your models here.
class Pack(BaseModel):
    name        = models.CharField(max_length=255)
    price       = models.IntegerField(default = 0)
    nbre_lit    = models.IntegerField(default = 0)
    superficie  = models.IntegerField(default = 0)
    modele_lit  = models.CharField(max_length=255)
    inclus      = models.TextField(default = "")
    image       = models.ImageField(max_length = 255, upload_to = "images/pack/", default='images/pack/default.png', null = True, blank=True)



    def __str__(self):
        return self.name



class Activity(BaseModel):
    name            = models.CharField(max_length=255)
    public_price    = models.IntegerField(default = 0)
    private_price   = models.IntegerField(default = 0)
    description     = models.TextField(default = "")
    prerequis       = models.TextField(default = "")
    image           = models.ImageField(max_length = 255, upload_to = "images/activities/", default='images/activities/default.png', null = True, blank=True)

    def __str__(self):
        return self.name
    
    

class CategoryOption(BaseModel):
    name        = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Option(BaseModel):
    name = models.CharField(max_length=255)
    categorie = models.ForeignKey(CategoryOption, on_delete = models.CASCADE, related_name="categorie_option")


    def __str__(self):
        return self.name