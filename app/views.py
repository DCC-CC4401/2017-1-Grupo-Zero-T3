from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    page = "<h1 align='center'> hola mundo! </h1>"
    return HttpResponse(page)


def base(request):
    return render(request, "base.html")


def vendedorA(request):
    return render(request, "FichaVendedor(alumno).html")


def vendedorV(request):
    return render(request, "FichaVendedor(vendedor).html")


def vendedorVE(request):
    return render(request, "FichaVendedor(vendedorEditar).html")
