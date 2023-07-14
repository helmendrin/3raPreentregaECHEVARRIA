from django.db import models

class Plato(models.Model):
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    # Otros atributos de la clase Plato
    # ...

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    platos = models.ManyToManyField(Plato)

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    platos = models.ManyToManyField(Plato, through='Pedido', related_name='mesas')
    pedido = models.OneToOneField('Pedido', null=True, blank=True, on_delete=models.SET_NULL, related_name='mesa')

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    platos = models.ManyToManyField(Plato)
