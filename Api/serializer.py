# LLAMAMOS LA BDD PARA VISUALIZARLA
# Y LLAMAMOS A TODOS MODELOS
from .models import*
from rest_framework import serializers
# TANSFROMAMOS PARA CONECTAR EL 
# BACK CON EL FRONT A UN FORMATO JSON
class ListaProd(serializers.ModelSerializer):
    class Meta:
        # llamamos a la tabla
        model=Productos
        # llamamos a todos los elementos
        fields='__all__'

