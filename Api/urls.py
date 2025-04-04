from django.urls import path, include
from . import views

urlpatterns = [
    # Corremos el servidor y las ('') indican
    # que es la url principal
    # ,(Home) llama a la funcion para retonrnar la pagina 
    # 
    path('', views.home, name = 'home'),
    path('agregar/', views.agregarProducto, name = 'agregarProducto'),
    path('productos/', views.listaProductos, name = 'listaProductos'),
]