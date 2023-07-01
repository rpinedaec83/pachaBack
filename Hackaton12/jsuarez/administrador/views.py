from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, MatriculaForm, ProfesorForm
from django.shortcuts import render
from .models import Curso, Alumno, Matricula, Profesor


def home(request):
    cursos = Curso.objects.all()
    return render(request, 'home.html', {'cursos': cursos})


def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})


def inscribir_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'inscribir_alumno.html', {'form': form})


def contratar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'contratar_profesor.html', {'form': form})


def matricular(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            alumno = form.cleaned_data['alumno']
            profesor = form.cleaned_data['profesor']

            matricula = Matricula(
                alumno=alumno, curso=curso, profesor=profesor)
            matricula.save()

            return redirect('cursos')
    else:
        form = MatriculaForm()
    return render(request, 'matricular.html', {'form': form})


def ver_alumnos_curso(request, curso_id):
    # Obtener el curso a partir del ID
    curso = Curso.objects.get(id=curso_id)

    alumnos_matriculados = Matricula.objects.filter(curso=curso)

    profesores_asignados = Profesor.objects.filter(
        matricula__curso=curso).distinct()

    context = {
        'curso': curso,
        'alumnos_matriculados': alumnos_matriculados,
        'profesores_asignados': profesores_asignados
    }

    return render(request, 'ver_alumnos_curso.html', context)
