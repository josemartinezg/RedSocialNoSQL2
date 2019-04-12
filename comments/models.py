from datetime import datetime
from django.db import models
from publicacion.models import Publicacion
from usuario.models import Usuario


class Comments(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.DO_NOTHING)
    id_perfil = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    comentario = models.CharField(max_length=200)
    fecha_publicado = models.DateTimeField(default=datetime.now)

    def str(self):
        return self.name