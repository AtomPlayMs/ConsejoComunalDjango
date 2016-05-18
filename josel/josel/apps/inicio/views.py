# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from josel.apps.sistema.models import Publicacion, Pagina, Vocero, comiteElectoral
from django.http import HttpResponse
from .forms import ContacForm, LugaresForm
from .models import Contacto, Lugares
from django.http import HttpResponseRedirect
from django.utils.text import Truncator
from django.core.paginator import Paginator,EmptyPage,InvalidPage



def index_view(request):
	"""queryset = Publicacion.objects.order_by('-id')
				for obj in queryset:
					obj.text = Truncator(obj.descripcion).chars(12, truncate = '')
					print obj.text"""
	public = Publicacion.objects.order_by('id')
	paginator = Paginator(public,1)
	
	publicaciones = paginator.page(paginator.num_pages)

	template = loader.get_template('inicio/index.html')
	ctx = {'publicacion':publicaciones}
	return HttpResponse(template.render(ctx,request))



def contacto_view(request):
	info_enviado = False
	nombres = ""
	correo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContacForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			nombres = formulario.cleaned_data['Nombres']
			correo = formulario.cleaned_data['Correo']
			texto = formulario.cleaned_data['Texto']
			c = Contacto()
			c.nombres = nombres
			c.correo = correo
			c.texto = texto
			c.save()
			template = loader.get_template('inicio/gracias_contacto.html')
			return HttpResponse(template.render(request))
		
		
		else:
				info_enviado = "Información con datos incorrectos"
				formulario = ContacForm()
		template = loader.get_template('inicio/contacto.html')
		ctx = {'form':formulario,'nombres':nombres,'correo':correo,'texto':texto,'info_enviado':info_enviado}
		return HttpResponse(template.render(ctx,request))

	else:
		
		formulario = ContacForm()
		template = loader.get_template('inicio/contacto.html')
		ctx = {'form':formulario,'nombres':nombres,'correo':correo,'texto':texto,'info_enviado':info_enviado}
		return HttpResponse(template.render(ctx,request))


def voceros_view(request):
	voceros = Vocero.objects.order_by('comite')
	template = loader.get_template('inicio/voceros.html')
	ctx = {'voceros':voceros}
	return HttpResponse(template.render(ctx,request))


def comite_view(request):
	comite = comiteElectoral.objects.order_by('designacion')
	template = loader.get_template('inicio/comite_electoral.html')
	ctx = {'comite':comite}
	return HttpResponse(template.render(ctx, request))


def agregarLugar_view(request):

	info = "Iniciado"
	if request.method == "POST":
		form = LugaresForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/')
	else:
		form = LugaresForm()
		template = loader.get_template('inicio/agregar_lugar.html')
		ctx = {'form':form,'informacion':info}
		return HttpResponse(template.render(ctx,request))

def lugares_view(request):
	lugares = Lugares.objects.all()
	template = loader.get_template('inicio/lugares.html')
	ctx = {'lugares':lugares}
	return HttpResponse(template.render(ctx,request))