from django.db import models

#------------------------ Modelo  ------------------------
class INFORMACION(models.Model):
    #Guardar imagen dentro de la base de datos
    imagen        = models.ImageField("Imagen del defecto", upload_to="imagenes", null=True, blank=True) 
    nombre_imagen = models.CharField("Nombre de la imagen", max_length=100, null=True, blank=True)
    upload_to     = models.CharField("Fecha y hora de subida", max_length=70, null=False, blank=False) #Con esto, no deberia hacer nada mas con la fecha (creo)
    callefinal    = models.CharField("Registros de calles", max_length=70, null=True, blank=True)
    resultado     = models.CharField("Resultado del analis", max_length=50, null=True, blank=True)
    class meta:
        verbose_name        = "Informe"
        verbose_name_plural = "Informes"
        ordering = ['upload_to']
        
    def __str__(self):
        return self.upload_to