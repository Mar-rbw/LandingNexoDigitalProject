from django.shortcuts import render

# Create your views here.
def landing_inicio(request):
    return render(request, "inicio.html")

def landing_servicios(request):
    return render(request, "servicios.html")

def landing_nosotros(request):
    return render(request, "nosotros.html")

def landing_contacto(request):
    return render(request, "contacto.html")