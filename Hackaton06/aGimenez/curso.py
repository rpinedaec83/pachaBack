from clases import Curso
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

def mostrarCursos():
    header = ['Id Curso', 'Nombre']
    query = "Select * from Curso;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarCurso():
    nombre = input("Ingrese Nombre Curso: ")
    header = ['Id Curso', 'Nombre']
    query = f"Select * from Curso where nombreCurso = '{nombre}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def editarCurso():
    buscarCurso()
    IdCurso = int(input("Ingrese Id de Curso que desea editar: "))
    nombreNuevo = input("Ingrese Nombre: ")
    query = f'''Update Curso
        set 
        nombreCurso = '{nombreNuevo}'
        where IdCurso = '{IdCurso}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearCurso():
    nombre = input("Ingrese Nombre: ")
    curso = Curso(nombre)
    query = f'''insert into Curso(nombreCurso)
        values('{curso.nombre}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarCurso():
    buscarCurso()
    IdCurso = int(input("Ingrese Id de Curso que desea eliminar: "))
    query = f''' delete from Curso
        where IdCurso = '{IdCurso}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")
