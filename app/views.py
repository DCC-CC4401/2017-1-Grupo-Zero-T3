from django.forms import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from app.models import *
from app.form import VendedorFijoForm, VendedorAmbulanteForm, AlumnoForm, EditarVendedor, ProductoForm, LoginForm
import time


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def logout_view(request):
    logout(request)
    return render(request, "app/index.html")


def login_view(request):
    # create a form instance and populate it with data from the request:
    form = LoginForm(request.POST, request.FILES)
    # check whether it's valid:
    print(form.is_valid())
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            context = dict()
            user = Usuario.objects.get(user=user)
            tipo = user.tipo
            if (tipo == 2):
                return render(request, "app/index.html")
            if (tipo == 3):
                context["id"] = Vendedor.objects.get(user = user).id
                return HttpResponseRedirect("/app/vendedorprofilepage/"+str(context["id"]), context)
        else:
            form = LoginForm()
            return render(request, "app/login.html", {'form': form})
    else:
        form = LoginForm()
        return render(request, 'app/login.html', {'form': form})


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
    context["foto"] = v.user.foto

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
        va = VendedorAmbulante.objects.get(vendedor=v)
        context["estado"] = "disponible" if va.activo else "no disponible"

    context["fav"] = len(Favorito.objects.filter(vendedor=v))
    context["productos"] = Producto.objects.filter(vendedor=v)

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
            efectivo = form.cleaned_data['efectivo']
            credito = form.cleaned_data['credito']
            debito = form.cleaned_data['debito']
            junaeb = form.cleaned_data['junaeb']
            hora_apertura = form.cleaned_data['hora_apertura']
            hora_clausura = form.cleaned_data['hora_clausura']
            imagen = form.cleaned_data['file']
            user = User(username=nombre, email=email)
            user.set_password(contrasena)
            user.save()
            usuario = Usuario(user=user, foto=imagen, tipo=3)
            usuario.save()
            vendedor = Vendedor(user=usuario, credito=credito, debito=debito, efectivo=efectivo, JUNAEB=junaeb, tipo=1)
            vendedor.save()
            vendedorfijo = VendedorFijo(vendedor=vendedor, hora_apertura=hora_apertura, hora_clausura=hora_clausura,
                                        ubicacion='')
            vendedorfijo.save()
            context = dict()
            context["id"] = vendedor.id
            # redirect to a new URL:
            return render(request, "app/vendedor-profile-page.html", context)

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
            efectivo = form.cleaned_data['efectivo']
            credito = form.cleaned_data['credito']
            debito = form.cleaned_data['debito']
            junaeb = form.cleaned_data['junaeb']
            imagen = form.cleaned_data['file']
            user = User(username=nombre, email=email)
            user.set_password(contrasena)
            user.save()
            usuario = Usuario(user=user, foto=imagen, tipo=3)
            usuario.save()
            vendedor = Vendedor(user=usuario, credito=credito, debito=debito, efectivo=efectivo,
                                JUNAEB=junaeb, activo=True, tipo=2)
            vendedor.save()
            vendedorambulante = VendedorAmbulante(vendedor=vendedor)
            vendedorambulante.save()
            # redirect to a new URL:
            return render(request, "app/index.html")

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
            user = User(username=nombre, email=email)
            user.set_password(contrasena)
            user.save()
            alumno = Usuario(user=user, foto=imagen, tipo=2)
            alumno.save()
            # redirect to a new URL:
            return render(request, "app/index.html")

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


def editarvendedor(request, id):
    if request.method == 'POST':
        form = EditarVendedor(request.POST, request.FILES)

        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            hora_apertura = form.cleaned_data["hora_apertura"]
            hora_clausura = form.cleaned_data["hora_clausura"]
            credito = form.cleaned_data["credito"]
            debito = form.cleaned_data["debito"]
            efectivo = form.cleaned_data["efectivo"]
            junaeb = form.cleaned_data["junaeb"]
            foto = form.cleaned_data["foto"]

            return vendedorprofilepage(request, id)

    context = dict()
    context["id"] = id

    v = Vendedor.objects.get(id=id)
    initial = dict()

    initial["nombre"] = v.user.username

    initial["debito"] = v.debito
    initial["credito"] = v.credito
    initial["efectivo"] = v.efectivo
    initial["junaeb"] = v.JUNAEB

    initial["foto"] = v.user.foto

    context["fijo"] = v.tipo == 1

    if context["fijo"]:
        vf = VendedorFijo.objects.get(id=id)
        initial["hora_apertura"] = vf.hora_apertura
        initial["hora_clausura"] = vf.hora_clausura

    form = EditarVendedor(initial=initial)

    context["form"] = form
    return render(request, "app/editar-vendedor.html", context)


def registrarProducto(request, id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ProductoForm(request.POST, request.FILES)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            descripcion = form.cleaned_data['descripcion']
            vendedor = Vendedor.objects.get(id=id)
            imagen = form.cleaned_data['file']
            producto = Producto(vendedor=vendedor, foto=imagen, nombre=nombre, descripcion=descripcion, precio=precio,
                                stock=stock, categoria=1)
            producto.save()
            # redirect to a new URL:
            return render(request, "app/vendedor-profile-page.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductoForm()

    context = dict()
    context["id"] = id
    context["form"] = form
    return render(request, "app/gestion-productos.html", context)
