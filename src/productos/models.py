from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos',blank=True, null=True)

    def __str__(self):
      return f"{self.nombre} - {self.marca}"

class Marca(models.Model):
      nombre = models.CharField(max_length=50)
      
      def __str__(self):
       return f"{self.nombre}"




    
