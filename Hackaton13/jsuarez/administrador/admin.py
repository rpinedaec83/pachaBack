from django.contrib import admin
from .models import Administrador, Asistencia, Curso, Alumno, Evaluacion, Nota, Profesor, Matricula, Rol

admin.site.register(Rol)
admin.site.register(Administrador)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Matricula)

admin.site.register(Evaluacion)
admin.site.register(Asistencia)
admin.site.register(Nota)