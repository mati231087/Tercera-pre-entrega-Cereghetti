from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "CORE/index.html", {"Saludo": obtener_titulo(), "Slogan": obtener_slogan()})

def obtener_titulo():
    return "Bienvenido a Entrenautas"

def obtener_slogan():
    return "El primer mercado nautico digital"

