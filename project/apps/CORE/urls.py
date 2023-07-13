
from django.urls import path

from . import views
from .views import crear_categoria, crear_producto, crear_usuario, pagina_construccion

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-categoria/", crear_categoria, name="crear_categoria"),
    path("cargar_producto/", crear_producto, name="cargar_producto"),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
    path("pagina-construccion/", pagina_construccion, name="pagina_construccion"),
    path("base/", views.base_view, name="base"),  
]
