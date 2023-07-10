from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "CORE/index.html", {"Saludo": "Bienvenido a Entrenautas"})


def index(request):
    return render(request, "CORE/index.html", {"Slogan": "El primer mercado nautico digital"})