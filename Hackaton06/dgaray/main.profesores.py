from utils import Menu
from alumnos import Alumnos
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

try:
    opMenuPrincipal = {"Mostrar Profesores": "1", "Editar Profesor": "2","Crear Profesor": "3","Borrar Profesor":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','Nombre','email']
            query = "Select * from profesores;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            idProfesor = int(input("Que profesores deseas editar: "))
            query = f"Select * from profesores where id = {idProfesor};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','email']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombreProfesor = input("Dime el nombre del profesor: ")
            email = input("Dime tu email: ")
            query = f'''Update profesores 
                set nombre = '{nombreProfesor}',
                email = '{email}'
                where id = {idProfesor};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            nombreProfesor = input("Dime el nombre del profesor: ")
            email = input("Dime tu email: ")
            query= f'''insert into profesores(nombre,email)
                     values('{nombreProfesor}','{email}');'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            idProfesor = int(input("Que profesor deseas borrar: "))
            query = f"Select * from profesores where id = {idProfesor};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','email']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from profesores
                where id = {idProfesor};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))