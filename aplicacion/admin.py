from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(Ciudad)
admin.site.register(Usuario_Servicio)