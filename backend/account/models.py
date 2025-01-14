from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator

# Create your models here.

class Usuario(User):
    #dispositivos = models.ManyToManyField(Dispositivo, related_name='usuarios', blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    phone_regex = RegexValidator(regex=r'^\d{8}$', message="El número de teléfono debe tener exactamente 8 dígitos.")
    phone = models.CharField(validators=[phone_regex], max_length=8, blank=True, unique=True)


    def __str__(self):
        return self.get_full_name()