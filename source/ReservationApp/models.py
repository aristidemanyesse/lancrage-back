import uuid
from django.db import models

from CoreApp.models import BaseModel

# Create your models here.
class Reservation(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name