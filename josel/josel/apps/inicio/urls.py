from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index_view, name='vista_index'),
	url(r'contactanos/$', views.contacto_view, name='vista_contacto'),
	url(r'voceros/$', views.voceros_view, name='vista_voceros'),
	url(r'comite-electoral/$', views.comite_view, name='vista_comite'),
	url(r'agregar/lugar/$', views.agregarLugar_view, name='vista_agregar_lugar'),
	url(r'lugares/$', views.lugares_view, name='vista_lugares'),
	

]
