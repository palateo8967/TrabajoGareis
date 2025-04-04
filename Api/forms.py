from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['Codigo', 'Nombre', 'Precio', 'Marca', 'Descripcion']
