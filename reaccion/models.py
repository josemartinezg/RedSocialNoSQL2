from datetime import datetime
from django.db import models
from publicacion.models import Publicacion
from usuario.models import Usuario

class Reaccion(models.Model):
    id_perfil = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.DO_NOTHING)
    like = models.BooleanField(default=True)
    fecha_like = models.DateTimeField(default=datetime.now)
    def str(self):
        return self.name