from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.usuarios,name='index'),
    path(r'usuario/<pk>', views.servicios,name='servicios'),
    path(r'usuario/edit/<pk>', views.editar,name='editar'),
    path(r'usuario/edit/eliminar/<pk>',views.eliminar,name='eliminar'),
]