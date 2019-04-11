from django.db import models
from usuario.models import Usuario

class Seguidor(models.Model):
    id_perfil = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING,related_name='%(class)s_requests_created')
    id_perfil_seguido = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    aceptado = models.BooleanField(default=False)

    def str(self):
        return self.name