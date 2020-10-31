from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import Venta, Cliente, Producto, Area, Nota


class VentaInline(admin.TabularInline):
    model = Venta
    autocomplete_fields = ('producto',)
    exclude = ('pendiente_impresion', 'entregado')


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    actions = ['marcar_nota_entregada']
    list_display = ('no_nota', 'cliente', 'get_ventas', 'total', 'anticipo', 'fecha', 'entregado')
    search_fields = ('no_nota', 'cliente__nombre', 'Cliente__telefono')
    list_filter = ('entregado',)
    fields = (('no_nota', 'cliente'), ('total', 'anticipo'))
    exclude = ('fecha',)
    autocomplete_fields = ('cliente',)
    inlines = [
        VentaInline,
    ]

    def marcar_nota_entregada(self, request, queryset):
        for nota in queryset:
            nota.entregado = not nota.entregado
            nota.save()

    marcar_nota_entregada.short_description = "Marcar como entrado"

    def get_ventas(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((venta,) for venta in obj.venta_set.all()),
        ) or mark_safe("<span class='errors'>I can't determine this address.</span>")

    get_ventas.short_description = 'ventas'


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    actions = ('marcar_entragado', 'marcar_impreso')
    list_display = ('nota', 'producto', 'descripcion', 'cantidad', 'total', 'impreso', 'diseñado')
    list_filter = ('producto__area', 'impreso', 'diseñado')
    search_fields = ('nota__no_nota', 'descripcion', 'producto__nombre')

    def marcar_impreso(modeladmin, request, queryset):
        for venta in queryset:
            venta.impreso = not venta.impreso
            venta.save()

    marcar_impreso.short_description = "Marcar como impreso"

    def marcar_entragado(modeladmin, request, queryset):
        for venta in queryset:
            venta.diseñado = not venta.diseñado
            venta.save()

    marcar_entragado.short_description = "Marcar como diseñado"


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo', 'area')
    search_fields = ('nombre',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
