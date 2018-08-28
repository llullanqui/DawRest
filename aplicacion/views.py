from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def usuarios(request):
	if request.method == "POST":
		form = DetalleForm(request.POST)
		if form.is_valid():
			form.save()
			usuario = form.cleaned_data['usuario']
			return redirect('servicios',pk=usuario.id)
	usuarios = Usuario.objects.all()
	form = DetalleForm()
	return render(request,'aplicacion/usuarios.html',{"usuarios":usuarios,"form":form})

def servicios(request,pk):
	usuario = Usuario.objects.get(pk=pk)
	servicios = Usuario_Servicio.objects.filter(usuario=pk)
	return render(request,'aplicacion/servicios.html',{"usuario":usuario,"servicios":servicios})

def editar(request,pk):
	if request.method == "POST":
		detalle = Usuario_Servicio.objects.get(pk=pk)
		form = DetalleForm(request.POST,instance=detalle)
		if form.is_valid():
			form.save()
			usuario = form.cleaned_data['usuario']
			return redirect('servicios',pk=usuario.id)
	detalle = Usuario_Servicio.objects.get(pk=pk)
	form = DetalleForm(instance = detalle)
	return render(request,'aplicacion/editar.html',{"detalle":detalle,"form":form})

def eliminar(request,pk):
	detalle = Usuario_Servicio.objects.get(pk=pk)
	usuario = detalle.usuario 
	detalle.delete()
	return redirect ('servicios',pk=usuario.id)