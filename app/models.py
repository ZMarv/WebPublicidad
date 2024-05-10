from django.db import models

# Create your models here.

class Suscripcion(models.Model):
    id_suscripcion = models.IntegerField(primary_key=True)
    nombre_suscripcion = models.CharField(max_length=20)
    precio_suscripcion = models.IntegerField()
    descripcion_suscripcion = models.CharField(max_length=100)

    def __str__(self):
        txt = "ID {0}  -  Nombre {1}  -  Precio {2}"
        return txt.format(self.id_suscripcion, self.nombre_suscripcion, self.precio_suscripcion)