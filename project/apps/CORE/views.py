from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import CategoriaForm, ProductoForm, UsuarioForm

# Create your views here.


def index(request):
    return render(request, "CORE/index.html", {"Saludo": obtener_titulo(), "Slogan": obtener_slogan()})

def obtener_titulo():
    return "Bienvenido a Entrenautas"

def obtener_slogan():
    return "El primer mercado nautico digital"

def crear_producto(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else: #request.method == "GET":
        form = ProductoForm()
    return render(request, "CORE/crear.html", {"form": form})

def crear_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else: #request.method == "GET":
        form = UsuarioForm()
    return render(request, "CORE/crear.html", {"form": form})

def crear_categoria(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...
    else: #request.method == "GET":
        form = CategoriaForm()
    return render(request, "CORE/crear.html", {"form": form})
