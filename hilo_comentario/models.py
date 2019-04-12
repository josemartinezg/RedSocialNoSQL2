from datetime import datetime
from django.db import models
from comments.models import Comments
from usuario.models import Usuario

class Hilos_Comentario(models.Model):
    id_comentario = models.ForeignKey(Comments, on_delete=models.DO_NOTHING)
    id_perfil = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    comentario = models.CharField(max_length=200)
    fecha_publicado = models.DateTimeField(default=datetime.now)

    def str(self):
        return self.name