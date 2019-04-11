from django.db import models
from datetime import datetime
from usuario.models import Usuario
from django.db import models

class Publicacion(models.Model):
    id_perfil = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=200)
    fecha_publicado = models.DateField()
    hora_publicado = models.DateTimeField()


    def str(self):
        return self.name