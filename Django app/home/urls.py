from django.urls import path
from home.forms import INFORMACION_FORM
from home.views import *
from home import views

urlpatterns = [
    path("", pruebainicial, name="home"),
    path("experimento/", INFORMACION_FORM, name='formulario'),
    path("formulario/", intento2_formulario),
    path("datos/", ver_datos, name="datos"),
    path("salida/", views.salir, name="salir")]