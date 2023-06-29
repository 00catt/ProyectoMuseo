from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=50)
    celular = models.IntegerField()
    edad = models.SmallIntegerField()
    contrasena = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellidos)
    
class Artista(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=50)
    celular = models.IntegerField()
    arte = models.CharField(max_length=100)
    argumento = models.CharField(max_length=1000)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellidos)
    
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=100)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.precio)
