from django.db import models
from django.utils import timezone


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

class Autor(models.Model):
    nombre = models.CharField(max_length=100)