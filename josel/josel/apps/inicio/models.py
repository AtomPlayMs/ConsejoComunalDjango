# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contacto(models.Model):
	nombres = models.CharField('Nombre y apellido',max_length=100,null=False)
	correo = models.CharField('Correo eléctronico',max_length=150)
	texto = models.TextField('Texto')

	def __unicode__(self):
		return self.nombres


class Lugares(models.Model):

	nombre = models.CharField('Nombre del lugar',max_length=300)
	direccion = models.CharField('Dirección',max_length=200)
	descripcion = models.TextField('Descripción')
	imagen = models.FileField(upload_to='Lugares/',null=True,blank=True)
	thumbnail = models.ImageField(upload_to='Lugares/',blank=True,null=True)
	lat = models.CharField('Latitud',max_length=50)
	lng = models.CharField('Longitud',max_length=50)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

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
         THUMBNAIL_SIZE = (300,250)

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

        	super(Lugares, self).save()