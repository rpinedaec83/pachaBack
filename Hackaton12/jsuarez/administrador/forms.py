from django import forms
from .models import Alumno, Profesor, Curso


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'identificador', 'edad', 'celular')


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'especialidad', 'salario')


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'estado')


class MatriculaForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all())
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all())
