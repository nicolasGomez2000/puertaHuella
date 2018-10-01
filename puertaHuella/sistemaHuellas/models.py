from django.db import models
from PIL import Image, ImageChops, ImageEnhance, ImageOps

# Create your models here.

class Curso(models.Model):
    nomCurso=models.CharField(max_length=50)

class Persona(models.Model):
    dni=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fechaNac=models.DateField()
    celular=models.CharField(max_length=20,blank=True)
    mail=models.EmailField(max_length=30, blank=True)
    imagen=models.ImageField(upload_to='images', null=True, default=None)

class Alumno(Persona):
    pass

    #class Meta:
      #  ordering: ["apellido", "nombre"]

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Materia(models.Model):
    nomMateria=models.CharField(max_length=50)

#hereda de Persona
class Docente(models.Model):
   dni=models.IntegerField(unique=True)
   nombre=models.CharField(max_length=50)
   apellido=models.CharField(max_length=50)
   direccion=models.CharField(max_length=50)
   fechaNac=models.DateField()
   celular=models.CharField(max_length=20,blank=True)
   mail=models.EmailField(max_length=30, blank=True)
   categoria=models.CharField(max_length=50, blank=True)
   imagen=models.ImageField(upload_to='images', null=True, default=None)
class Ingreso(models.Model):
   numRegistro=models.IntegerField()
   fecha=models.DateTimeField(auto_now=True)
   activo=models.BooleanField(default=True)


    












