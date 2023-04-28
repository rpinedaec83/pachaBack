from conexion import conexion
from tabulate import tabulate
import utils
class Curso:

    def __init__(self,idCurso,nombre,idProfesor,idAlumno):
        self.idCurso = idCurso
        self.nombre = nombre
        self.idProfesor = idProfesor
        self.idAlumno = idAlumno
        


    __cn = conexion()  
    __lstCurso = []

    def cargarCurso():        
        query = "select * from Curso;"
        res = Curso.__cn.ConsultarQuery(query=query)
        for crs in res:
            curso = Curso(crs[0], crs[1], crs[2], crs[3])
            Curso.__lstCurso.append(curso)

    def listarCurso():
        header = ['ID','Nombre','ID Profesor','ID Alumno']
        query = "SELECT * FROM Curso;"
        res = Curso.__cn.ConsultarQuery(query=query)
        print(utils.color.BLUE + tabulate(res, headers=header, tablefmt='fancy_grid')+ utils.color.END)
        input(utils.color.GREEN+"Presione 'Enter' para continuar..."+utils.color.END)

    def crearCurso():
        try:
            nombre = input("Nombre de Curso: ")
            idProfesor = int(input("ID Profesor: "))
            idAlumno = int(input("ID Alumno: "))
            query= f'''insert into curso(nombre,idProfesor,idAlumno)
                    values('{nombre}',{idProfesor},{idAlumno});'''
            if(Curso.__cn.EjecutarQuery(query=query)):
                Curso.listarCurso()
                print("Datos creados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)

    def editarCurso():
        try:
            idCurso = int(input("Ingrese el ID del Curso a editar: "))
            query = f"Select * from Curso where idCurso = {idCurso};"
            res = Curso.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','ID Profesor','ID Alumno']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            nombre = input("Nombre de Curso: ")
            idProfesor = int(input("ID Profesor: "))
            idAlumno = int(input("ID Alumno: "))
            queryUpdate = f'''Update Curso 
                    set nombre = '{nombre}',
                    idProfesor = '{idProfesor}',
                    idAlumno = {idAlumno} where idCurso = {idCurso};'''
            if(Curso.__cn.EjecutarQuery(query=queryUpdate)):
                Curso.listarCurso()
                print("Datos actualizados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)
        
    def eliminarCurso():
        try:
            idCurso = int(input("¿Que Curso deseas borrar?: "))
            query = f"Select * from Curso where idCurso = {idCurso};"
            res = Curso.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','ID Profesor','ID Alumno']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            query = f''' delete from Curso
                where idCurso = {idCurso};'''
            if(Curso.__cn.EjecutarQuery(query=query)):
                print("Datos borrados correctamente")
                Curso.listarCurso()
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)