from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ProductoForm, CategoriaForm, UsuarioForm


def obtener_titulo():
    
    return "Bienvenido a Entrenautas"

def obtener_slogan():
    
    return "El primer mercado náutico digital"


def base_view(request: HttpRequest) -> HttpResponse:
    return render(request, "CORE/base.html", {
        "Saludo": obtener_titulo(),
        "obtener_titulo": obtener_titulo(),
        "obtener_slogan": obtener_slogan(),
    })

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "CORE/index.html")

def crear_producto(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria = categoria_form.cleaned_data['nombre']
                producto.categoria = categoria
                producto.save()
                return redirect("index")
    else:
        form = ProductoForm()
    categoria_form = CategoriaForm()
    return render(request, "CORE/cargar_producto.html", {"form": form, "categoria_form": categoria_form})

def crear_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UsuarioForm()
    return render(request, "CORE/crear_usuario.html", {"form": form})

def crear_categoria(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CategoriaForm()
    return render(request, "CORE/crear.html", {"form": form})

def pagina_construccion(request: HttpRequest) -> HttpResponse:
    return render(request, "CORE/pagina_construccion.html")
