from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django import forms


class Usuario(models.Model):
    SEX_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    correo_electronico = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    contrasena = forms.CharField(widget=forms.PasswordInput)
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    descripcion = models.TextField(blank=True)
    pais_nacimiento = CountryField()
    pais_residente = CountryField(blank=True)
    linea_direccion_1 = models.CharField(max_length=120, blank=True)
    linea_direccion_2 = models.CharField(max_length=120, blank=True)
    sector = models.CharField(max_length=120, blank=True)
    ciudad = models.CharField(max_length=120, blank=True)
    telefono = models.CharField(max_length=20)
    es_verificado = models.BooleanField(default=False)
    es_privado = models.BooleanField(default=False)
    foto_perfil = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    coordenadas = models.CharField(max_length=200, blank=True)
    fecha_ingreso = models.DateTimeField(default=datetime.now, blank=True)



def _str_(self):
    return self.nombre_usuario