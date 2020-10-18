from django.contrib import admin

from .models import Venta, Cliente, Producto, Area


class VentaAdmin(admin.ModelAdmin):
    list_display = ('Cliente', 'No_nota', 'Producto', 'Descripcion', 'Cantidad', 'Total', 'Abono', 'fecha')
    list_filter = ('Producto__area',)
    search_fields = ('No_nota', 'Descripcion', 'Cliente__nombre', 'Cliente__telefono')
    exclude = ('fecha',)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo', 'area')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Venta, VentaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Area, AreaAdmin)
