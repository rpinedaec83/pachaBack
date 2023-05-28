from utils import Menu
from alumnos import Alumnos
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()
listAlumnos = []

# def cargaInicial():
#     query = "Select * from Alumnos;"
#     res = conexion.consultarBDD(query=query)
#     for alumn in res:
#         alumno = Alumnos(alumn[0], alumn[1], alumn[2], alumn[3])
#         listAlumnos.append(alumno)
# cargaInicial()
try:
    opMenuPrincipal = {"Mostrar Alumnos": "1", "Editar Alumno": "2","Crear Alumno": "3","Borrar Alumno":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','Nombre','email','edad']
            query = "Select * from alumnos;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            idAlumno = int(input("Que alumnos deseas editar: "))
            query = f"Select * from alumnos where id = {idAlumno};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','email','edad']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            NombreAlumno = input("Dime el nombre del alumno: ")
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            query = f'''Update alumnos 
                set nombre = '{NombreAlumno}',
                email = '{email}',
                edad = {edad}
                where id = {idAlumno};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            NombreAlumno = input("Dime el nombre del alumno: ")
            email = input("Dime tu email: ")
            edad = int(input("Dime tu edad: "))
            query= f'''insert into alumnos(nombre,email,edad)
                     values('{NombreAlumno}','{email}',{edad});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            idAlumno = int(input("Que alumno deseas borrar: "))
            query = f"Select * from alumnos where id = {idAlumno};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','email','edad']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from alumnos
                where id = {idAlumno};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))