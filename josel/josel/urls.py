from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^',include('josel.apps.inicio.urls')),
    url(r'^',include('josel.apps.sistema.urls')),
    url(r'^admin/', admin.site.urls),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
