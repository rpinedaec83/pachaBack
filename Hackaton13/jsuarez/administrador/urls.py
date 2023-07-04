from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    
    path('alumnos/inscribir/', views.inscribir_alumno, name='inscribir_alumno'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('profesores/contratar/', views.contratar_profesor, name='contratar_profesor'),
    path('cursos/matricular/', views.matricular, name='matricular'),
    path('ver_alumnos_curso/<int:curso_id>/', views.ver_alumnos_curso, name='ver_alumnos_curso'),

    path('tomar_asistencia/<int:curso_id>/', views.tomar_asistencia, name='tomar_asistencia'),
    path('ingresar_nota/<int:evaluacion_id>/', views.ingresar_nota, name='ingresar_nota'),
    path('ver_asistencias/<int:curso_id>/', views.ver_asistencias, name='ver_asistencias'),
    path('ver_notas/<int:evaluacion_id>/', views.ver_notas, name='ver_notas'),
]
