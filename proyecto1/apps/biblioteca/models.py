from django.db import models

#class Author(models.Model):
#        name = models.CharField(max_length=200)
#        surname = models.CharField(max_length=200)
#        nacionality = models.CharField(max_length=200)
        
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tematica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    año_edicion = models.IntegerField()
    tematica = models.ForeignKey(Tematica, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo



    
# Create your models here.
