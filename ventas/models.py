from django.db import models
from django.utils import timezone


class Configuracion(models.Model):
    nombre = models.CharField(max_length=32)
    folio_inicial = models.IntegerField()


class Nota(models.Model):
    no_nota = models.IntegerField()
    cliente = models.ForeignKey('Cliente', null=True, on_delete=models.SET_NULL)
    total = models.FloatField()
    anticipo = models.FloatField()
    fecha = models.DateTimeField(default=timezone.now)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.no_nota)


class Venta(models.Model):
    nota = models.ForeignKey('Nota', null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey('Producto', null=True, on_delete=models.SET_NULL)
    descripcion = models.TextField()
    cantidad = models.FloatField()
    total = models.FloatField()
    impreso = models.BooleanField(default=False)
    diseñado = models.BooleanField(default=False)
    fecha_entrega = models.DateField(null=True, blank=True)

    def __str__(self):
        return '[%s] %s $%s' % (self.cantidad, self.producto.nombre, self.total)


class Cliente(models.Model):
    nombre = models.TextField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return '%s : %s' % (self.nombre, self.telefono)


class Producto(models.Model):
    nombre = models.TextField()
    costo = models.FloatField()
    area = models.ForeignKey('Area', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.area)


class Area(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return '%s' % (self.nombre,)
