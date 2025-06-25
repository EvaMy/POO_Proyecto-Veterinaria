from django.db import models

# Create your models here.

class UsuarioAdoptante(models.Model):
        nombre= models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        dni= models.CharField(max_length=9, unique=True)
        email=models.EmailField()
        preferencias=models.TextField()

        def __str__(self):
                return self.nombre+ " "+ self.apellido +" "+str(self.dni)
        
class Perro(models.Model):
        nombre=models.CharField(max_length=100)
        raza=models.CharField(max_length=100)
        edad=models.IntegerField()
        tamaño=models.CharField(max_length=50)
        peso=models.FloatField()
        estado_salud=models.CharField(max_length=100)
        vacunado=models.BooleanField()
        estado=models.CharField(max_length=20)
        temperamento=models.CharField(max_length=100)

        def __str__(self):
                return self.nombre+" "+self.raza
