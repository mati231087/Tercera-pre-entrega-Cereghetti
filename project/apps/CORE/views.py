from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import CategoriaForm, ProductoForm, UsuarioForm





def index(request):
    if request.method == "POST":
        if "crear_usuario" in request.POST:
            return redirect("crear_usuario")
        elif "ver_productos" in request.POST:
            return redirect("pagina_construccion")
    return render(request, "CORE/index.html", {"Saludo": obtener_titulo(), "Slogan": obtener_slogan()})

def obtener_titulo():
    return "Bienvenido a Entrenautas"

def obtener_slogan():
    return "El primer mercado nautico digital"

def crear_producto(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else:
        form = ProductoForm()
    return render(request, "CORE/crear.html", {"form": form})

def crear_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else:
        form = UsuarioForm()
    return render(request, "CORE/crear_usuario.html", {"form": form})

def crear_categoria(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else:
        form = CategoriaForm()
    return render(request, "CORE/crear.html", {"form": form})

def pagina_construccion(request: HttpRequest) -> HttpResponse:
    return render(request, "CORE/pagina_construccion.html")

