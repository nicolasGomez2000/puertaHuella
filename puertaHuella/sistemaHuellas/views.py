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
    persona=None
    if ingreso:
        persona = Alumno.objects.filter(numeroRegistro=ingreso.numRegistro).first()
    if persona:
        bienvenido = "alumno"
    else:
        persona = Docente.objects.filter(numeroRegistro=ingreso.numRegistro).first()
        bienvenido = "docente"

    #alumnos = Alumno.objects.filter(dni=32434)
    #docente =  Docente.objects.filter(dni=1234)
    #docente = list(docente)
    #alumnos = list(alumnos)#para asegurarse de ....
    #alumno = alumnos[0]
    #docente = docente[0]
    #DETERMINAR SI ES ALUMNO O DOCENTE PARA MOSTRAR UNA U OTRA VISTA. HECHO
    #COLOCAR DIRECCION DE LOS RECURSOS COMO CSS U IMAGENES, PARA QUE NO TE APARESCA COMO LINK
    src = '{}{}.{}'.format('\\media\\images\\', persona.numeroRegistro, 'jpg')

    
    return render(request,'bienvenidoPersona.html',{'nombre':persona.nombre,'apellido':persona.apellido, 
                'src':src, 'bienvenido': bienvenido})
