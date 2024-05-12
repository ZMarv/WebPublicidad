from django.db import models

# Create your models here.

class Suscripcion(models.Model):
    nombre_suscripcion = models.CharField(max_length=20)
    precio_suscripcion = models.IntegerField()
    descripcion_suscripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_suscripcion