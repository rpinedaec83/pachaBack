from utils import Menu
from alumnos import Alumnos
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

try:
    opMenuPrincipal = {"Mostrar salones": "1", "Editar salon": "2","Crear salon": "3","Borrar salon":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','anoEscolar','seccion', 'idAlumno', 'idProfesor']
            query = "Select * from salon;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            idSalon = int(input("Que salon deseas editar: "))
            query = f"Select * from salon where id = {idSalon};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','anoEscolar','seccion', 'idAlumno', 'idProfesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            anoEscolar = int(input("Dime el año escolar: "))
            seccion = input("Dime la seccion: ")
            idAlumno = int(input("Dime el id del alumno: "))
            idProfesor = int(input("Dime el id del profesor: "))
            query = f'''Update salon 
                set ano_escolar = {anoEscolar},
                seccion = '{seccion}',
                id_alumno = {idAlumno},
                id_profesor = {idProfesor}
                where id = {idSalon};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            anoEscolar = int(input("Dime el año escolar: "))
            seccion = input("Dime la seccion: ")
            idAlumno = int(input("Dime el id del alumno: "))
            idProfesor = int(input("Dime el id del profesor: "))
            query= f'''insert into salon(ano_escolar,seccion,id_alumno,id_profesor)
                     values({anoEscolar},'{seccion}', {idAlumno}, {idProfesor});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            idSalon = int(input("Que salon deseas borrar: "))
            query = f"Select * from salon where id = {idSalon};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','anoEscolar','seccion', 'idAlumno', 'idProfesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from salon
                where id = {idSalon};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))