from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request, template_name='appAdminColegio/index.html'):
    cursos = Curso.objects.all()
    dato_cursos = {"cursos": cursos}
    return render(request, template_name, dato_cursos)