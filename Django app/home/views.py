from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect 
from home.forms import INFORMACION_FORM
from home.models import *
from django.db.models import Q


#--------------------------------------------------------------------
#Renderizado simple
def pruebainicial(request):
    return render(request, "paginas/index2.html")
#--------------------------------------------------------------------
#Poder observar formulario, con metodo POST, ademas de agregar archivo
def intento2_formulario(request):
    forms = INFORMACION_FORM(request.POST, request.FILES)
    if forms.is_valid():
        forms.save()
        forms = INFORMACION_FORM()

    context = {"forms": forms}
    forms   = INFORMACION_FORM()

    return render(request, "paginas/intento2.html", context)

#--------------------------------------------------------------------
#Acceso solo con login 
@login_required
def ver_datos(request):
    queryset = request.GET.get("buscar")
    informaciones = INFORMACION.objects.filter()
    if queryset:
        informaciones = INFORMACION.objects.filter(Q(callefinal__icontains = queryset))
    return render(request, "paginas/datos.html", {"informaciones": informaciones})

def salir(request):
    logout(request)
    return redirect("/")
#--------------------------------------------------------------------