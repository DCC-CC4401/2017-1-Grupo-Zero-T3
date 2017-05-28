from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def gestionproductos(request):
    return render(request, "app/gestion-productos.html")


def vendedorprofilepage(request):
    return render(request, "app/vendedor-profile-page.html")
