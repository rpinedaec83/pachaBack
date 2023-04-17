from utils import Menu
from alumno import *
from profesor import *
from curso import *
from salon import *

def menuAlumno():
    ansMenuAlumno = ""
    opMenuAlumno = {"Crear Alumno" : "1", "Mostrar Lista de Alumnos" : "2", "Buscar Alumno" : "3", "Editar Alumno" : "4", "Eliminar Alumno" : "5", "Asignar Salon" : "6", "Asignar Nota" : "7", "Volver Menu Principal" : "0"}
    menuAlumno = Menu("Alumno", opMenuAlumno)
    while ansMenuAlumno != 0:
        ansMenuAlumno = menuAlumno.show()
        if(ansMenuAlumno == "1"):
            crearAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "2"):
            mostrarAlumnos()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "3"):
            buscarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "4"):
            editarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "5"):
            eliminarAlumno()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuAlumno == "6"):
            ansMenuSalonAlumno = ""
            opMenuSalonAlumno = {"Asignar Salon a un Alumno" : "1", "Mostrar Salones Asignados a un Alumno" : "2", "Editar Salon de un Alumno" : "3", "Eliminar Salon de un Alumno" : "4", "Volver Menu Anterior" : "0"}
            menuSalonAlumno = Menu("Salon Alumno", opMenuSalonAlumno)
            while ansMenuSalonAlumno != 0:
                ansMenuSalonAlumno = menuSalonAlumno.show()
                if(ansMenuSalonAlumno == "1"):
                    crearSalonAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "2"):
                    mostrarSalonAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "3"):
                    editarSalonAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "4"):
                    eliminarSalonAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonAlumno == "0"):
                    break                   
        if(ansMenuAlumno == "7"):
            ansMenuNotaAlumno = ""
            opMenuNotaAlumno = {"Asignar Nota a un Alumno" : "1", "Mostrar Notas Bimestrales de un Alumno" : "2", "Editar Notas de un Alumno" : "3", "Eliminar Notas de un Alumno" : "4", "Volver Menu Anterior" : "0"}
            menuNotaAlumno = Menu("Nota Alumno", opMenuNotaAlumno)
            while ansMenuNotaAlumno != 0:
                ansMenuNotaAlumno = menuNotaAlumno.show()
                if(ansMenuNotaAlumno == "1"):
                    crearNotaAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "2"):
                    buscarNotaAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "3"):
                    editarNotaAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "4"):
                    eliminarNotaAlumno()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaAlumno == "0"):
                    break
        if(ansMenuAlumno == "0"):
            break                  

def menuProfesor():
    ansMenuProfesor = ""
    opMenuProfesor = {"Crear Profesor" : "1", "Mostrar Lista de Profesores" : "2", "Buscar Profesor" : "3", "Editar Profesor" : "4", "Eliminar Profesor" : "5", "Asignar Salon" : "6", "Asignar Nota" : "7", "Volver Menu Principal" : "0"}
    menuProfesor = Menu("Profesor", opMenuProfesor)
    while ansMenuProfesor != 0:
        ansMenuProfesor = menuProfesor.show()
        if(ansMenuProfesor == "1"):
            crearProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "2"):
            mostrarProfesores()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "3"):
            buscarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "4"):
            editarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "5"):
            eliminarProfesor()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuProfesor == "6"):
            ansMenuSalonProfesor = ""
            opMenuSalonProfesor = {"Asignar Salon a un Profesor" : "1", "Mostrar Salones Asignados a un Profesor" : "2", "Editar Salon de un Profesor" : "3", "Eliminar Salon de un Profesor" : "4", "Volver Menu Anterior" : "0"}
            menuSalonProfesor = Menu("Salon Profesor", opMenuSalonProfesor)
            while ansMenuSalonProfesor != 0:
                ansMenuSalonProfesor = menuSalonProfesor.show()
                if(ansMenuSalonProfesor == "1"):
                    crearSalonProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "2"):
                    mostrarSalonProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "3"):
                    editarSalonProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "4"):
                    eliminarSalonProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuSalonProfesor == "0"):
                    break                   
        if(ansMenuProfesor == "7"):
            ansMenuNotaProfesor = ""
            opMenuNotaProfesor = {"Asignar Nota a un Profesor" : "1", "Mostrar Notas Bimestrales de un Profesor" : "2", "Editar Notas de un Profesor" : "3", "Eliminar Notas de un Profesor" : "4", "Volver Menu Anterior" : "0"}
            menuNotaProfesor = Menu("Nota Profesor", opMenuNotaProfesor)
            while ansMenuNotaProfesor != 0:
                ansMenuNotaProfesor = menuNotaProfesor.show()
                if(ansMenuNotaProfesor == "1"):
                    crearNotaProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaProfesor == "2"):
                    buscarNotaProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaProfesor == "3"):
                    editarNotaProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaProfesor == "4"):
                    eliminarNotaProfesor()
                    input("Toque un Boton para continuar")
                    continue
                if(ansMenuNotaProfesor == "0"):
                    break
        if(ansMenuProfesor == "0"):
            break                  

def menuSalon():
    ansMenuSalon = ""
    opMenuSalon = {"Crear Salon" : "1", "Mostrar Lista de Salones" : "2", "Editar Salon" : "3", "Eliminar Salon" : "4", "Volver Menu Principal" : "0"}
    menuSalon = Menu("Salon", opMenuSalon)
    while ansMenuSalon != 0:
        ansMenuSalon = menuSalon.show()
        if(ansMenuSalon == "1"):
            crearSalon()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuSalon == "2"):
            mostrarSalones()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuSalon == "3"):
            editarSalon()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuSalon == "4"):
            eliminarSalon()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuSalon == "0"):
            break 

def menuCurso():
    ansMenuCurso = ""
    opMenuCurso = {"Crear Curso" : "1", "Mostrar Lista de Cursos" : "2", "Editar Curso" : "3", "Eliminar Curso" : "4", "Volver Menu Principal" : "0"}
    menuCurso = Menu("Curso", opMenuCurso)
    while ansMenuCurso != 0:
        ansMenuCurso = menuCurso.show()
        if(ansMenuCurso == "1"):
            crearCurso()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuCurso == "2"):
            mostrarCursos()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuCurso == "3"):
            editarCurso()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuCurso == "4"):
            eliminarCurso()
            input("Toque un Boton para continuar")
            continue
        if(ansMenuCurso == "0"):
            break 

try:
    opMenuPrincipal = {"Alumnos" : "1", "Profesores" : "2", "Salones" : "3", "Cursos" : "4", "Salir" : "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            menuAlumno()
            continue
        if(ansMenuPrincipal == "2"):
            menuProfesor()
            continue
        if(ansMenuPrincipal == "3"):
            menuSalon()
            continue
        if(ansMenuPrincipal == "4"):
            menuCurso()
            continue
except Exception as error:
    print(str(error))

