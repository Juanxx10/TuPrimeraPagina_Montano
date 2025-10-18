from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Moto(models.Model):
    NUEVA_USADA_CHOICES = [
        ('Nueva', 'Nueva'),
        ('Usada', 'Usada')]
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    cilindrada = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    año = models.IntegerField()
    estado = models.CharField(max_length=5, choices=NUEVA_USADA_CHOICES, default='Nueva')
    kilometros = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.cilindrada}cc ({self.estado})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
