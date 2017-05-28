from django.http import HttpResponse
from django.shortcuts import render
from app.models import *


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def gestionproductos(request, id):
    context = dict()
    context["id"] = id
    return render(request, "app/gestion-productos.html", context)


def vendedorprofilepage(request, id):
    context = dict()
    context["id"] = id

    v = Vendedor.objects.get(id=id)
    context["username"] = v.user.username
    context["estado"] = "disponible" if v.activo else "no disponible"

    pagos = []
    if v.efectivo:
        pagos.append("efectivo")
    if v.credito:
        pagos.append("credito")
    if v.debito:
        pagos.append("debito")
    if v.JUNAEB:
        pagos.append("JUNAEB")
    context["pagos"] = pagos

    if v.tipo == 1:
        vf = VendedorFijo.objects.get(vendedor=v)
        h = vf.hora_apertura
        context["apertura"] = str(int(h/100)) + ":" + str(h%100)
        h = vf.hora_clausura
        context["clausura"] = str(int(h/100)) + ":" + str(h%100)

    context["fav"] = len(Favorito.objects.filter(vendedor=v))
    context["productos"] = Producto.objects.filter(vendedor=v)
    categorias = dict()
    for p in context["productos"]:
        categorias[p.id] = p.get_categoria_display()
    context["categorias"] = categorias

    print(context)

    return render(request, "app/vendedor-profile-page.html", context)
