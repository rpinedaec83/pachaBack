from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    
    path('alumnos/inscribir/', views.inscribir_alumno, name='inscribir_alumno'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('profesores/contratar/', views.contratar_profesor, name='contratar_profesor'),
    path('cursos/matricular/', views.matricular, name='matricular'),
    path('ver_alumnos_curso/<int:curso_id>/', views.ver_alumnos_curso, name='ver_alumnos_curso'),
]
