from django.contrib import admin
from josel.apps.sistema.models import Genero, Comite, Designacion, Vocero, Publicacion, Pagina, comiteElectoral, Habitante,condicionHabitante,Nacionalidad,estadoCivil,nivelInstruccion,profesionOficio,Incapacidad,Dincapacidad,Pension


class voceroAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellidos','cedula','comite','designacion','thumbnail')
	list_filter = ('comite',)
	search_fields = ['nombres','apellidos','cedula']
	fields = (('nombres','apellidos'),'cedula','genero','foto','direccion','correo','telefono',('comite','designacion'),'votos','status')





class comiteAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellidos','cedula','designacion','thumbnail')
	list_filter = ('designacion',)
	search_fields = ['nombres','apellidos','cedula']
	fields = ('nombres','apellidos','cedula','genero','foto','direccion','correo','telefono',('comite','designacion'),'votos','status')


class publicacionAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha')
	fields = ('titulo','descripcion','imagen','url_album')

class habitanteAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellidos','cedula','manzana','edad')
	list_filter = ('manzana','profesion_oficio')
	search_fields = ['nombres','apellidos','cedula','edad']
	fields = ('condicion','nombres','apellidos',('nacionalidad','cedula'),'fecha_nac','genero','estado_civil','direccion','num_casa',('telf_cel','telf_hab','telf_ofic'),'correo','manzana',('nivel_instruccion','profesion_oficio'),('trabaja','ingreso_mensual'),('incapacidad','pension','cne'),'discapacidad','embarazo','status' )

admin.site.register(Genero)
admin.site.register(Vocero,voceroAdmin)
admin.site.register(Comite)
admin.site.register(Designacion)
admin.site.register(Publicacion,publicacionAdmin)
admin.site.register(Pagina)
admin.site.register(comiteElectoral,comiteAdmin)
admin.site.register(Habitante,habitanteAdmin)
admin.site.register(condicionHabitante)
admin.site.register(Nacionalidad)
admin.site.register(estadoCivil)
admin.site.register(nivelInstruccion)
admin.site.register(profesionOficio)
admin.site.register(Incapacidad)
admin.site.register(Dincapacidad)
admin.site.register(Pension)
