from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^gestionproductos/(?P<id>[0-9]+)$', views.gestionproductos, name='gestionproductos'),
    url(r'^vendedorprofilepage/(?P<id>[0-9]+)$', views.vendedorprofilepage, name='vendedorprofilepage'),
    url(r'^$', views.index, name='index'),
]