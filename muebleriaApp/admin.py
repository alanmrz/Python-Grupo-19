from django.contrib import admin
from .models import Producto, Carrito

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion') 
    search_fields = ('nombre', 'descripcion') 

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
    list_editable = ('cantidad',)  
    search_fields = ('producto__nombre',) 

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito, CarritoAdmin)
