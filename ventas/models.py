from django.db import models
from django.utils import timezone


class Venta(models.Model):
    Cliente = models.ForeignKey('Cliente', null=True, on_delete=models.SET_NULL)
    No_nota = models.IntegerField()
    Producto = models.ForeignKey('Producto', null=True, on_delete=models.SET_NULL)
    Descripcion = models.TextField()
    Cantidad = models.FloatField()
    Total = models.FloatField()
    Abono = models.FloatField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % (self.No_nota,)


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
        return '%s - %s' % (self.nombre,self.area)


class Area(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return '%s' % (self.nombre,)