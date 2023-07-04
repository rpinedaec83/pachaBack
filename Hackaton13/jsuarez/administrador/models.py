from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    identificador = models.CharField(max_length=15)
    edad = models.IntegerField(default=0)
    celular = models.CharField(max_length=9)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno.nombre} matriculado en {self.curso.nombre}"
    

class Evaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)

class Asistencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)

class Nota(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)