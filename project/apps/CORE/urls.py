from django.urls import path

from . import views
from .views import crear_categoria, crear_producto, crear_usuario

urlpatterns = [
    path("", views.index),
    path("crear-categoria/", crear_categoria, name="crear_categoria"),
    path("crear-producto/", crear_producto, name="crear_producto"),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
]
