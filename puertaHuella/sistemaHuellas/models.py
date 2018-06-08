from django.db import models

# Create your models here.
class Alumno(models.Model):
    dni=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fechaNac=models.DateField()
    celular=models.CharField(max_length=20,blank=True)
    mail=models.EmailField(max_length=30, blank=True)

    #class Meta:
      #  ordering: ["apellido", "nombre"]

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
class Curso(models.Model):
    nomCurso=models.CharField(max_length=50)


class Materia(models.Model):
    nomMateria=models.CharField(max_length=50)

class Docente(models.Model):
    dni=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fechaNac=models.DateField()
    celular=models.CharField(max_length=20,blank=True)
    mail=models.EmailField(max_length=30, blank=True)
    categoria=models.CharField(max_length=50, blank=True)












