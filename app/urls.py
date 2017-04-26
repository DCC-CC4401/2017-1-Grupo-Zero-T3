from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^base/', views.base, name='base'),
    url(r'^vendedorA/', views.vendedorA, name='vendedorA'),
    url(r'^vendedorV/', views.vendedorV, name='vendedorV'),
    url(r'^producto/', views.producto, name='producto'),
    url(r'^productoV/', views.productoV, name='productoV'),
    url(r'^$', views.index, name='index'),
]