# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import A4, cm
from django.template import RequestContext, loader
from .models import Habitante, Vocero, Publicacion
from datetime import datetime
import datetime
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def pdf_view(request):
	html_content = "<h1>***Mensaje***</h1>"
	
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	buffer = BytesIO()
	# Create the PDF object, using the BytesIO object as its "file."
	p = canvas.Canvas(buffer,pagesize=A4)
	
	#Header
	#p.setLinewidth(25)
	p.setFont('Helvetica',22)
	p.drawString(30,750,'Atom')
	
	p.setFont('Helvetica',12)
	p.drawString(30,735,'Reporte')

	p.setFont('Helvetica-Bold',12)
	p.drawString(480,750,"23/04/2016")

	p.line(460,747,560,747)
	# Close the PDF object cleanly.
	p.showPage()
	p.save()


	# Get the value of the BytesIO buffer and write it to the response.
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response


def habitantes_view(request):
	
	habitante = Habitante.objects.all()
	
	queryset = Habitante.objects.all()
	for obj in queryset:
		fech = datetime.date.today() - obj.fecha_nac
		obj.fecha_nac = str(fech/365).split(' ')[0]
		print obj.fecha_nac

	template = loader.get_template('sistema/habitantes.html')
	
	ctx = {'habitante':habitante,'fecha':queryset}
	return HttpResponse(template.render(ctx, request))

def publicacion_view(request,pagina):
	"""queryset = Publicacion.objects.order_by('-id')
				for obj in queryset:
					obj.text = Truncator(obj.descripcion).chars(12, truncate = '')
					print obj.text"""
	list_public = Publicacion.objects.order_by('-id')
	paginator = Paginator(list_public,8)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		publicaciones = paginator.page(page)
	except (EmptyPage,InvalidPage):
		publicaciones = paginator.page(paginator.num_pages)

	template = loader.get_template('sistema/publicaciones.html')
	ctx = {'public':publicaciones}
	return HttpResponse(template.render(ctx,request))