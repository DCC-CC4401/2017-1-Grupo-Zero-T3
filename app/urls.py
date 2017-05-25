from django.conf.urls import url
from . import views

#Agrego SignUp
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^$', views.index, name='index'),
]