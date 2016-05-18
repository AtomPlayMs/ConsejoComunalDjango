# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import datetime
import datetime
from django.core.validators import MaxValueValidator
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os
class Genero(models.Model):
	gen = models.CharField('Genero',max_length=9)

	def __unicode__(self):
		return self.gen

class Comite(models.Model):
	comite = models.CharField('Comite',max_length=300)

	def __unicode__(self):
		return self.comite

class Designacion(models.Model):
	desig = models.CharField('Designacion',max_length=50)

	def __unicode__(self):
		return self.desig

class Vocero(models.Model):

	

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width="50px" height="60px">'%(self.foto,self.foto)
	thumbnail.allow_tags = True

	nombres = models.CharField('Nombres',max_length=200)
	apellidos = models.CharField('Apellidos',max_length=200)
	cedula = models.PositiveIntegerField('Cedula',validators=[MaxValueValidator(99999999)])
	genero = models.ForeignKey(Genero,null=True,on_delete=models.CASCADE)
	foto = models.FileField(upload_to='fotosVoceros',null=True,blank=True)
	direccion = models.CharField('Direccion',max_length=300)
	correo = models.CharField('Correo',max_length=200,null=True,blank=True)
	telefono = models.CharField('Telefono',max_length=11,null=True,blank=True)
	comite = models.ForeignKey(Comite,null=True,on_delete=models.CASCADE)
	designacion = models.ForeignKey(Designacion,null=True,on_delete=models.CASCADE)
	votos = models.IntegerField('Votos obtenidos')
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto


class Publicacion(models.Model):

	

	titulo = models.CharField('Título',max_length=60)
	descripcion = models.TextField('Descrición')
	imagen = models.FileField('Imagén',upload_to='Publicaciones')
	thumbnail = models.ImageField(upload_to='Publicaciones',blank=True,null=True)
	url_album = models.CharField('Link de album en facebook',max_length=800)
	fecha = models.DateField('Fecha',auto_now_add=True)
	
	
	def __unicode__(self):
		return self.titulo


	def create_thumbnail(self):
         # original code for this method came from
         # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

         # If there is no image associated with this.
         # do not create thumbnail
         if not self.imagen:
             return

         from PIL import Image
         from cStringIO import StringIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (200,150)

         DJANGO_TYPE = self.imagen.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         imagen = Image.open(StringIO(self.imagen.read()))

         # Convert to RGB if necessary
         # Thanks to Limodou on DjangoSnippets.org
         # http://www.djangosnippets.org/snippets/20/
         #
         # I commented this part since it messes up my png files
         #
         #if image.mode not in ('L', 'RGB'):
         #    image = image.convert('RGB')

         # We use our PIL Image object to create the thumbnail, which already
         # has a thumbnail() convenience method that contrains proportions.
         # Additionally, we use Image.ANTIALIAS to make the image look better.
         # Without antialiasing the image pattern artifacts may result.
         imagen.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         imagen.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.imagen.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

     	def save(self):
         	# create a thumbnail
         	self.create_thumbnail()

        	super(Publicacion, self).save()



























class Pagina(models.Model):

	nombre = models.CharField('Nombre de la página',max_length=25)
	

	def __unicode__(self):
		return self.nombre

class comiteElectoral(models.Model):

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width="50px" height="60px">'%(self.foto,self.foto)
	thumbnail.allow_tags = True
	
	nombres = models.CharField('Nombres',max_length=200)
	apellidos = models.CharField('Apellidos',max_length=200)
	cedula = models.PositiveIntegerField('Cedula',validators=[MaxValueValidator(99999999)])
	genero = models.ForeignKey(Genero,null=True,on_delete=models.CASCADE)
	foto = models.FileField(upload_to='fotosComites',null=True,blank=True)
	direccion = models.CharField('Direccion',max_length=300)
	correo = models.CharField('Correo',max_length=200,null=True,blank=True)
	telefono = models.CharField('Telefono',max_length=11,null=True,blank=True)
	designacion = models.ForeignKey(Designacion,null=True,on_delete=models.CASCADE)
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

class condicionHabitante(models.Model):
	condicion = models.CharField('Condición',max_length=25)

	def __unicode__(self):
		return self.condicion

class Nacionalidad(models.Model):
	nacionalidad = models.CharField('Nacionalidad',max_length=25)

	def __unicode__(self):
		return self.nacionalidad

class estadoCivil(models.Model):
	estado_civil = models.CharField('Estado civil',max_length=50)

	def __unicode__(self):
		return self.estado_civil

class nivelInstruccion(models.Model):
	nivel_instruccion = models.CharField('Nivel de instrucción',max_length=300)

	def __unicode__(self):
		return self.nivel_instruccion

class profesionOficio(models.Model):
	profesion_oficio = models.CharField('Profesión / Oficio',max_length=300)

	def __unicode__(self):
		return self.profesion_oficio

class Incapacidad(models.Model):
	incapacidad = models.CharField('Incapacidad',max_length=300)

	def __unicode__(self):
		return self.incapacidad

class Dincapacidad(models.Model):
	discapacidad = models.CharField('Dincapacidad',max_length=300)

	def __unicode__(self):
		return self.discapacidad

class Pension(models.Model):
	pension = models.CharField('Pension',max_length=300)

	def __unicode__(self):
		return self.pension

class Habitante(models.Model):

	def edad(self):
		fech = datetime.date.today() - self.fecha_nac
		edadr = str(fech/365).split(' ')[0]
		return edadr
	edad.allow_tags = True

	condicion = models.ForeignKey(condicionHabitante,null=True,on_delete=models.CASCADE)
	nombres = models.CharField('Nombres',max_length=200)
	apellidos = models.CharField('Apellidos',max_length=200)
	nacionalidad = models.ForeignKey(Nacionalidad,null=True,on_delete=models.CASCADE)
	cedula = models.PositiveIntegerField('Cédula',validators=[MaxValueValidator(99999999)])
	fecha_nac = models.DateField('Fecha de nacimiento')
	genero = models.ForeignKey(Genero,null=True,on_delete=models.CASCADE)
	estado_civil = models.ForeignKey(estadoCivil,null=True,on_delete=models.CASCADE)
	direccion = models.CharField('Dirección',max_length=300)
	num_casa = models.CharField('N° de casa',max_length=15,blank=True)
	telf_cel = models.IntegerField('Telf celular',null=True,blank=True)
	telf_hab = models.IntegerField('Telf de habitación',null=True,blank=True)
	telf_ofic = models.IntegerField('Telf de oficina',null=True,blank=True)
	correo = models.CharField('Correo eléctronico',max_length=200,null=True,blank=True)
	manzana = models.IntegerField('Mánzana')
	nivel_instruccion = models.ForeignKey(nivelInstruccion,null=True,blank=True,on_delete=models.CASCADE)
	profesion_oficio = models.ForeignKey(profesionOficio,null=True,blank=True,on_delete=models.CASCADE)
	trabaja = models.CharField('Trabaja?',null=True,blank=True,max_length=2)
	ingreso_mensual = models.DecimalField('Ingreso mensual',null=True,blank=True,max_digits=11,decimal_places=2)
	incapacidad = models.ForeignKey(Incapacidad,null=True,blank=True,on_delete=models.CASCADE)
	pension = models.ForeignKey(Pension,null=True,blank=True,on_delete=models.CASCADE)
	cne = models.CharField('Inscrito en CNE?',blank=True,max_length=2)
	discapacidad = models.ForeignKey(Dincapacidad,null=True,blank=True,on_delete=models.CASCADE)
	embarazo = models.CharField('Embarazo precoz?',blank=True,max_length=2)
	status = models.BooleanField(default=True)



