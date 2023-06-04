from django.db import models
import uuid
from datetime import date
# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Ciclo(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Curso(models.Model):
    name=models.CharField(max_length=150,null=False,default='')
    description=models.CharField(max_length=500,null=True)
    ciclo=models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    availability=models.PositiveIntegerField(null=False,default=25)

class Aula(models.Model):
    name= models.CharField(max_length=150,null=False,default='')
    max_students=models.PositiveIntegerField(null=False,default=10)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)

class UserSchool(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=150,null=False,default='')
    dni = models.CharField(max_length=10,null=False,default='72455505')
    email=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=500,null=True)
    img_path=models.CharField(max_length=500,null=True)
    availability=models.PositiveIntegerField(null=False,default=5)
    password=models.CharField(max_length=10,null=False,default='1111111')
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
class Alumnos(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=150,null=False,default='')
    dni = models.CharField(max_length=10,null=False,default='72455505')
    email=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=500,null=True)
    img_path=models.CharField(max_length=500,null=True)
    availability=models.PositiveIntegerField(null=False,default=5)
    password=models.CharField(max_length=10,null=False,default='1111111')
    def __str__(self):
        return self.name

class Matricula(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    alumno=models.ForeignKey(Alumnos, on_delete=models.DO_NOTHING)
    profesor=models.ForeignKey(UserSchool, on_delete=models.DO_NOTHING)
    aula=models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    ciclo=models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    curso=models.ForeignKey(Curso, on_delete=models.DO_NOTHING,null=True)
    def __str__(self):
        return str(self.id)

class Asistencia(models.Model):
    alumno=models.ForeignKey(Alumnos, on_delete=models.DO_NOTHING)
    profesor=models.ForeignKey(UserSchool, on_delete=models.DO_NOTHING)
    fecha = models.DateField(default=date.today)
    attendance=models.BooleanField(default=False)
    def __str__(self):
        return str(self.attendance)
