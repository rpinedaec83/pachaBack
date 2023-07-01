from django.db import models


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

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno.nombre} matriculado en {self.curso.nombre}"