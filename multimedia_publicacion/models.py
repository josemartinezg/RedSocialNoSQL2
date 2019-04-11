from django.db import models

from publicacion.models import Publicacion


class Multimedia(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.DO_NOTHING)
    contenido = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def str(self):
        return self.name