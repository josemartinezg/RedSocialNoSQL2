from django.db import models
from datetime import datetime
from django import forms
from django_countries.fields import CountryField


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    correo_electronico = models.EmailField(max_length=200)
    fecha_nacimiento = models.DateField()
    contrasena = forms.CharField(max_length=32,widget=forms.PasswordInput)
    sexo = models.CharField(max_length=2)
    descripcion = models.TextField(blank=True)
    pais_nacimiento = CountryField()
    telefono = models.CharField(max_length=20)
    es_verificado = models.BooleanField(default='false')
    es_privado = models.BooleanField(default='false')
    foto_perfil = models.ImageField(upload_to='photos/%Y/%m/%d/')
    coordenadas = models.CharField(max_length=200)
    hire_datte = models.DateTimeField(default=datetime.now, blank=True)


def _str_(self):
    return self.name