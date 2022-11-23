from django.db import models

# Create your models here.
#Clase que va a ir al views para los datos y a la BD
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacim = models.DateField()
    dni = models.IntegerField()

    