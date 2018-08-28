from django import forms
from .models import *


class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'
		
class DetalleForm(forms.ModelForm):
	class Meta:
		model = Usuario_Servicio
		fields = '__all__'