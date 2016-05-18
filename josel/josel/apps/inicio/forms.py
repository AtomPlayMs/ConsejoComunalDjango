from django import forms
from .models import Lugares

class ContacForm(forms.Form):

	Nombres = forms.CharField(widget=forms.TextInput())
	Correo = forms.EmailField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())



class LugaresForm(forms.ModelForm):
	class Meta:
		model 	= Lugares
		exclude = {'fecha',}
	
