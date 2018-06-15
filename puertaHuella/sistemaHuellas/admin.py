from django.contrib import admin
from .models import Alumno
from .models import Docente
from .models import Curso
from .models import Materia
#from .models import Asistencia
# Register your models here.
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Materia)
#admin.site.register(Asistencia)
