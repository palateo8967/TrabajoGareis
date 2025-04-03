from django.db import models

# Create your models here.

# CREAMOS LA TABLA PARA LOS PRODUCTOS
class Productos(models.Model):
    Codigo=models.IntegerField(primary_key=True)
    Nombre=models.TextField(max_length=20)
    Precio=models.FloatField(max_length=10)
    Marca=models.TextField(max_length=20)
    Descripcion=models.TextField(max_length=100)
    # RETORNA LA LLAVE PRIMARIA 
    # PARA DETECTARLA MAS RAPIDO   
    def __int__(self):
        self.Codigo
    
