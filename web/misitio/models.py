from django.db import models


# Create your models here.
class Cliente(models.Model):

    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100, null=False)

    '''
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=True)
    alta = models.DateTimeField('Fecha Alta', blank=False, null=True)
    direccion = models.CharField(max_length=150, blank=False, null=True)
    movil = models.CharField(max_length=14, blank=False, null=True)
    '''


class Vinilo(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    artista = models.CharField(max_length=100, null=False)
    ventas = models.IntegerField(null=False)
    precio = models.FloatField(null=False)
    imagen = models.ImageField(null=False)
