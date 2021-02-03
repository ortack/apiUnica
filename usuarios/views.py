from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import SolicitudUsuario, Aplicacion, EstadoSolicitud, UsuarioAplicacion
from usuarios.forms import SolicitarUsuarioForm, AplicacionForm
from django.shortcuts import redirect
# Create your views here.


def home(request):
    usuarios = SolicitudUsuario.objects.filter(estado_solicitud=1)
    return render(request, 'home.html', {
        'usuarios' : usuarios
    })

def aplicaciones(request):

    aplicaciones = Aplicacion.objects.all()
    return render(request, 'aplicaciones.html', {
        'aplicaciones' : aplicaciones
    })

def solicitar_usuario(request):
    form = SolicitarUsuarioForm()
    if request.method == "POST":
        form = SolicitarUsuarioForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/usuarios')
    return render(request, "solicitar_usuario.html", {'form': form})

def alta_aplicacion(request):
    form = AplicacionForm()
    if request.method == "POST":
        form = AplicacionForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/aplicaciones')
    return render(request, "alta_aplicacion.html", {'form': form})




