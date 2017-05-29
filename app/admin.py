from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(VendedorFijo)
admin.site.register(VendedorAmbulante)
admin.site.register(Producto)
admin.site.register(Favorito)
