from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Imagen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cada usuario tiene 1 sola imagen
    imagen = models.ImageField(upload_to='media', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

