from utils import Menu
from alumnos import Alumnos
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

try:
    opMenuPrincipal = {"Mostrar cursos": "1", "Editar curso": "2","Crear curso": "3","Borrar curso":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','nombreCurso','idAlumno', 'idProfesor', 'nota1', 'nota2', 'nota3', 'nota3']
            query = "Select * from cursos;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            idCurso = int(input("Que curso deseas editar: "))
            query = f"Select * from cursos where id = {idCurso};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','nombreCurso','idAlumno', 'idProfesor', 'nota1', 'nota2', 'nota3', 'nota3']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombreCurso = input("Dime nombre del curso: ")
            idAlumno = int(input("Dime el id del alumno: "))
            idProfesor = int(input("Dime el id del profesor: "))
            nota1 = input('Dime la nota del primer bimestre: "')
            nota2 = input('Dime la nota del primer bimestre: "')
            nota3 = input('Dime la nota del primer bimestre: "')
            nota4 = input('Dime la nota del primer bimestre: "')
            query = f'''Update cursos 
                set name = '{nombreCurso}',
                id_alumno = {idAlumno},
                id_profesor = {idProfesor},
                nota_bimestre_1 = '{nota1}',
                nota_bimestre_2 = '{nota2}',
                nota_bimestre_3 = '{nota3}',
                nota_bimestre_4 = '{nota4}'
                where id = {idCurso};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            nombreCurso = input("Dime nombre del curso: ")
            idAlumno = int(input("Dime el id del alumno: "))
            idProfesor = int(input("Dime el id del profesor: "))
            nota1 = input('Dime la nota del primer bimestre: "')
            nota2 = input('Dime la nota del primer bimestre: "')
            nota3 = input('Dime la nota del primer bimestre: "')
            nota4 = input('Dime la nota del primer bimestre: "')
            query= f'''insert into cursos(name,id_alumno,id_profesor,nota_bimestre_1,nota_bimestre_2,nota_bimestre_3,nota_bimestre_4)
                     values('{nombreCurso}',{idAlumno}, {idProfesor} ,'{nota1}', '{nota2}', '{nota3}', '{nota4}');'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            idCurso = int(input("Que cursos deseas borrar: "))
            query = f"Select * from cursos where id = {idCurso};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','nombreCurso','idAlumno', 'idProfesor', 'nota1', 'nota2', 'nota3', 'nota3']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from cursos
                where id = {idCurso};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))