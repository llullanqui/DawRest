from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)

	def __str__(self):
		return '%s %s' % (self.nombre,self.apellido)

class Servicio(models.Model):
	nombre = models.CharField(max_length=255)
	
	def __str__(self):
		return '%s' % (self.nombre)

class Ciudad(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.nombre)

class Usuario_Servicio(models.Model):
	usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE,null=False)
	servicio = models.ForeignKey('Servicio',on_delete=models.CASCADE,null=False)
	ciudad = models.ForeignKey('Ciudad',on_delete=models.CASCADE,null=False)
	observaciones = models.TextField(max_length=500,null=True)

	def __str__(self):
		return '%s - %s' % (self.usuario,self.servicio)
