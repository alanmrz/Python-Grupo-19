
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.template, name='template'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('agregar_a_carrito/<int:producto_id>/<int:cantidad>/', views.agregar_a_carrito, name='agregar_a_carrito'),
    path('editar_carrito/<int:carrito_id>/', views.editar_carrito, name='editar_carrito'),
    path('eliminar_del_carrito/<int:carrito_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
]
