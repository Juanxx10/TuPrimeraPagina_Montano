from django.contrib import admin

admin.site.site_header = "Administrador de Tienda de Motos"
admin.site.site_title = "Panel de Administración - Motos de Alta Gama"
admin.site.index_title = "Bienvenido al panel de gestión"

from .models import Marca, Moto, Cliente

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen')
    search_fields = ('nombre',)
    list_filter = ('pais_origen',)

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca_nombre', 'modelo', 'cilindrada', 'año', 'kilometros', 'estado', 'precio_formateado')
    search_fields = ('modelo', 'marca__nombre')
    list_filter = ('marca', 'año', 'estado')
    ordering = ('marca__nombre', 'modelo')

    def marca_nombre(self, obj):
        return obj.marca.nombre
    marca_nombre.short_description = 'Marca'
    marca_nombre.admin_order_field = 'marca__nombre'

    def precio_formateado(self, obj):
        return "{:,.0f} USD".format(obj.precio).replace(",", ".")
    precio_formateado.short_description = 'Precio'

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
