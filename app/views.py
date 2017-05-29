from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.models import *
from .form import VendedorFijoForm, VendedorAmbulanteForm, AlumnoForm
import time


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signupFijo.html")


def TipoUsuario(request):
    return render(request, "app/TipoUsuario.html")


def gestionproductos(request, id):
    context = dict()
    context["id"] = id
    return render(request, "app/gestion-productos.html", context)


def vendedorprofilepage(request, id):
    context = dict()
    context["id"] = id

    v = Vendedor.objects.get(id=id)
    context["vendor"] = v.user.username
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
    context["tipo"] = (v.tipo == 1)
    context["foto"] = v.foto

    if context["tipo"]:
        vf = VendedorFijo.objects.get(vendedor=v)
        ha = vf.hora_apertura
        context["apertura"] = str(int(ha / 100)) + ":" + str(ha % 100).zfill(2)
        hc = vf.hora_clausura
        context["clausura"] = str(int(hc / 100)) + ":" + str(hc % 100).zfill(2)

        hora_local = time.localtime().tm_hour * 100 + time.localtime().tm_min
        if ha < hora_local < hc:
            context["estado"] = "disponible"
        else:
            context["estado"] = "no disponible"

    else:
        context["estado"] = "disponible" if v.activo else "no disponible"

    context["fav"] = len(Favorito.objects.filter(vendedor=v))
    context["productos"] = Producto.objects.filter(vendedor=v)
    categorias = dict()
    for p in context["productos"]:
        categorias[p.id] = p.get_categoria_display()
    context["categorias"] = categorias

    print(context)

    return render(request, "app/vendedor-profile-page.html", context)


def registrarFijo(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = VendedorFijoForm(request.POST, request.FILES)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form = clean(form)
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['password']
            hora_apertura=form.cleaned_data['hora_apertura']
            hora_clausura=form.cleaned_data['hora_clausura']
            imagen = form.cleaned_data['file']
            user = User(username=nombre, password=contrasena, email=email)
            user.save()
            vendedor=Vendedor(user=user, foto=imagen, credito=True, debito=True, efectivo=True, JUNAEB=True, activo=True, tipo=1)
            vendedor.save()
            vendedorfijo=VendedorFijo(vendedor=vendedor, hora_apertura=hora_apertura, hora_clausura=hora_clausura, ubicacion='')
            vendedorfijo.save()
            # redirect to a new URL:
            return render(request, "app/login.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VendedorFijoForm()

    return render(request, 'app/signupFijo.html', {'form': form})


def registrarAmbulante(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = VendedorAmbulanteForm(request.POST, request.FILES)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form = clean(form)
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['password']
            imagen = form.cleaned_data['file']
            user = User(username=nombre, password=contrasena, email=email)
            user.save()
            vendedor=Vendedor(user=user, foto=imagen, credito=True, debito=True, efectivo=True, JUNAEB=True, activo=True, tipo=2)
            vendedor.save()
            vendedorambulante=VendedorAmbulante(vendedor=vendedor)
            vendedorambulante.save()
            # redirect to a new URL:
            return render(request, "app/login.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VendedorAmbulanteForm()

    return render(request, 'app/signupAmbulante.html', {'form': form})


def registrarAlumno(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = AlumnoForm(request.POST, request.FILES)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            form = clean(form)
            # process the data in form.cleaned_data as required
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['password']
            imagen = form.cleaned_data['file']
            user = User(username=nombre, password=contrasena, email=email)
            user.save()
            alumno=Alumno(user=user, foto=imagen)
            alumno.save()
            # redirect to a new URL:
            return render(request, "app/login.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlumnoForm()

    return render(request, 'app/signupAlumno.html', {'form': form})

def clean(self):
    password1 = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')

    if password1 and password1 != password2:
        raise forms.ValidationError("Passwords don't match")

    return self