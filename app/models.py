from django.db import models

# Create your models here.

class Suscripcion(models.Model):
    nombre_suscripcion = models.CharField(max_length=20)
    precio_suscripcion = models.IntegerField()
    creacion_avisos = models.CharField(max_length=100)
    cantidad_panfletos = models.IntegerField()
    promocion_google_ads = models.CharField(max_length=100)
    monitoreo_optimizacion = models.CharField(max_length=100)
    creacion_pagina_web = models.CharField(max_length=100, blank=True, null=True)
    asistencia_personalizada = models.CharField(max_length=100, blank=True, null=True)
    diseño_banners = models.CharField(max_length=100, blank=True, null=True)
    administracion_campañas = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_suscripcion