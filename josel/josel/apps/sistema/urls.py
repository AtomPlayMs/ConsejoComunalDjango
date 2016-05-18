from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'pdf/$', views.pdf_view, name='vista_pdf'),
	url(r'habitantes/$', views.habitantes_view, name='vista_habitante'),
	url(r'publicaciones/pagina/(?P<pagina>.*)/$', views.publicacion_view, name='vista_publicacion'),

]
