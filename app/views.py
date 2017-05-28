from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.models import *
from .form import VendedorFijoForm


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

def registrar(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = VendedorFijoForm(request.POST)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():

            # process the data in form.cleaned_data as required
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['password']
            hora_apertura=form.cleaned_data['hora_apertura']
            hora_clausura=form.cleaned_data['hora_clausura']
            user = User(username=nombre, password=contrasena, email=email)
            user.save()
            vendedor=Vendedor(user=user, foto=0, credito=True, debito=True, efectivo=True, JUNAEB=True, activo=True, tipo=1)
            vendedor.save()
            vendedorfijo=VendedorFijo(vendedor=vendedor, hora_apertura=hora_apertura, hora_clausura=hora_clausura, ubicacion='')
            vendedorfijo.save()
            # redirect to a new URL:
            return HttpResponseRedirect('app/login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VendedorFijoForm()

    return render(request, 'app/signup.html', {'form': form})
