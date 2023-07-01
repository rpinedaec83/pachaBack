from django.contrib import admin
from .models import Curso, Alumno, Profesor, Matricula

admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Matricula)
