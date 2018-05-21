from django.db import models

# Create your models here.
class Alumno(models.Model):
    dni=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    celular=models.CharField(max_length=20,blank=True)
    mail=models.EmailField(max_length=30, blank=True)













