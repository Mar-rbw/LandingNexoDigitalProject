from django.shortcuts import render
from LandingNexoDigitalApp.models import (resumenServicios, serviciosWeb,
                                          serviciosMobiles, serviciosNube,
                                          serviciosSeguridad)

# Create your views here.
def landing_inicio(request):
    context = {
        'servicios': resumenServicios()
    }
    return render(request, "index.html", context)

def landing_servicios(request):
    context = {
        'servicios': resumenServicios()
    }
    return render(request, "servicios.html", context)

def landing_nosotros(request):
    return render(request, "nosotros.html")

def landing_contacto(request):
    return render(request, "contacto.html")

def landing_detalleWeb(request):
    context = {
        'servicios': serviciosWeb()
    }
    return render(request, "detalle-1.html", context)

def landing_detalleMobile(request):
    context = {
        'servicios': serviciosMobiles()
    }
    return render(request, "detalle-2.html", context)

def landing_detalleNube(request):
    context = {
        'servicios': serviciosNube()
    }
    return render(request, "detalle-3.html", context)

def landing_detalleSeguridad(request):
    context = {
        'servicios': serviciosSeguridad()
    }
    return render(request, "detalle-4.html", context)