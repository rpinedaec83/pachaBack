from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, LoginForm, MatriculaForm, ProfesorForm
from django.shortcuts import render
from .models import Asistencia, Curso, Alumno, Evaluacion, Matricula, Nota, Profesor, Rol
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def perfil_administrador(request):
    rol = Rol.objects.get(usuario=request.user)

    return render(request, 'perfil_administrador.html')

def perfil_profesor(request):
    rol = Rol.objects.get(usuario=request.user)

    return render(request, 'perfil_profesor.html')

def perfil_alumno(request):
    rol = Rol.objects.get(usuario=request.user)

    return render(request, 'perfil_alumno.html')

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


@login_required
def tomar_asistencia(request, curso_id):
    if request.method == 'POST':
        curso = Curso.objects.get(pk=curso_id)
        alumnos = Alumno.objects.all()
        for alumno in alumnos:
            asistencia = request.POST.get(f'asistencia_{alumno.id}')
            Asistencia.objects.create(alumno=alumno, curso=curso, estado=asistencia)
        return redirect('ver_asistencias', curso_id=curso_id)
    else:
        curso = Curso.objects.get(pk=curso_id)
        alumnos = Alumno.objects.all()
        return render(request, 'tomar_asistencia.html', {'curso': curso, 'alumnos': alumnos})

@login_required
def ingresar_nota(request, evaluacion_id):
    if request.method == 'POST':
        evaluacion = Evaluacion.objects.get(pk=evaluacion_id)
        alumnos = Alumno.objects.all()
        for alumno in alumnos:
            nota = request.POST.get(f'nota_{alumno.id}')
            Nota.objects.create(alumno=alumno, evaluacion=evaluacion, valor=nota)
        return redirect('ver_notas', evaluacion_id=evaluacion_id)
    else:
        evaluacion = Evaluacion.objects.get(pk=evaluacion_id)
        alumnos = Alumno.objects.all()
        return render(request, 'ingresar_nota.html', {'evaluacion': evaluacion, 'alumnos': alumnos})


@login_required
def ver_asistencias(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    asistencias = Asistencia.objects.filter(curso=curso)
    return render(request, 'ver_asistencias.html', {'curso': curso, 'asistencias': asistencias})

@login_required
def ver_notas(request, evaluacion_id):
    evaluacion = Evaluacion.objects.get(pk=evaluacion_id)
    notas = Nota.objects.filter(evaluacion=evaluacion)
    return render(request, 'ver_notas.html', {'evaluacion': evaluacion, 'notas': notas})