from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from puertaHuella import settings 
from .models import Alumno, Ingreso
from .models import Docente
# Create your vie.ws here.

def visor(request):
    #alumno = Alumno.objects.filter(dni=32434).first()
    ingreso = Ingreso.objects.filter(activo=True).first()
    if ingreso:
        alumno = Alumno.objects.filter(id=ingreso.numRegistro).first()

    #alumnos = Alumno.objects.filter(dni=32434)
    #docente =  Docente.objects.filter(dni=1234)
    #docente = list(docente)
    #alumnos = list(alumnos)#para asegurarse de ....
    #alumno = alumnos[0]
    #docente = docente[0]
    src = '{}{}.{}'.format('\\media\\images\\', alumno.id, 'jpg')
    return render(request,'holamundo.html',{'nombre':alumno.nombre, 'src':src})

