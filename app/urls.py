from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^base/', views.base, name='base'),
    url(r'^vendedorA/', views.vendedorA, name='vendedorA'),
    url(r'^vendedorV/', views.vendedorV, name='vendedorV'),
    url(r'^vendedorVE/', views.vendedorVE, name='vendedorVE'),
    url(r'^$', views.index, name='index'),
]