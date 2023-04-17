from conexion import conexion
from utils import Menu
from Colegio import *
from tabulate import TableFormat, tabulate

conexion = conexion()

try:
    opMenuPrincipal = {"Mostrar Datos": "1", "Editar Datos": "2","Crear Datos": "3","Borrar Datos":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            menuSecundario = ""
            opMenuSec = {"Alumnos": "1", "Profesor": "2","Salon": "3","Periodo":"4","Notas": "5","Cursos": "6","Cursos Asignados al docente": "7", "Salir": "0"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()

            if(ansMenuSec == "1"):
                header = ['codAlum','nombre','identificador','edad','correo']
                query = "Select * from Alumno;"
            if(ansMenuSec == "2"):
                header = ['codProf','nombre','identificador','edad','correo']
                query = "Select * from Profesor;"
            if(ansMenuSec == "3"):
                header = ['codSalon','codPeriodo','codigoCurProf']
                query = "Select * from Salon;"
            if(ansMenuSec == "4"):
                header = ['codPeriodo','nombre','Anio','Mes']
                query = "Select * from Periodo;"
            if(ansMenuSec == "5"):
                header = ['codAlum','Nota1','Nota2','Nota3','Nota4','Nota5','Nota6']
                query = "Select * from Periodo;"
            if(ansMenuSec == "6"):
                header = ['codCurso','Nombre']
                query = "Select * from Curso;"
            if(ansMenuSec == "7"):
                header = ['codigo','dni Profesor','Nombre Profesor','Nombre Curso']
                query = "SELECT cp.codigo, pro.identificador, pro.nombre, cur.nombre FROM cursoProfes AS cp INNER JOIN Profesor as pro ON cp.codprof=pro.codprof INNER JOIN Curso as cur ON cp.codCurso=cur.codCurso;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea continuar??: ")

        if(ansMenuPrincipal == "2"):
            menuSecundario = ""
            opMenuSec = {"Alumnos": "1", "Profesor": "2","Periodo":"3","Cursos": "4","Profesor_curso": "5","Salir": "0"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()


            if(ansMenuSec == "1"):
                Id = int(input("Ingrese el Código: "))
                query = f"Select * from Alumno where codAlum = {Id};"
                header = ['codAlum','nombre','identificador','edad','correo']

                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                input("Desea continuar??: ")
                nombre = input("Ingrese su nombre: ")
                dni = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")

                query = f'''Update Alumno set nombre = '{nombre}', identificador = '{dni}', edad = {edad}, correo = '{correo}' where codAlum = {Id};'''

            if(ansMenuSec == "2"):
                Id = int(input("Ingrese el Código: "))
                query = f"Select * from Profesor where codProf = {Id};"
                header = ['codProf','nombre','identificador','edad','correo']

                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                input("Desea continuar??: ")
                nombre = input("Ingrese su nombre: ")
                dni = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")

                query = f'''Update Profesor set nombre = '{nombre}', identificador = '{dni}', edad = {edad}, correo = '{correo}' where codProf = {Id};'''

            if(ansMenuSec == "3"):
                Id = int(input("Ingrese el Código: "))
                query = f"Select * from Periodo where codPeriodo = {Id};"
                header = ['codPeriodo','nombre','Anio','Mes']
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                input("Desea continuar??: ")
                nombre = input("Ingrese su nombre: ")
                anio = int(input("Ingrese Año: "))
                mes = int(input("Ingrese Mes: "))

                query = f'''Update Periodo set nombre = '{nombre}', Anio = {anio}, Mes = {mes} where codPeriodo = {Id};'''

            if(ansMenuSec == "4"):
                Id = int(input("Ingrese el Código: "))
                query = f"Select * from Curso where codCurso = {Id};"
                header = ['codCurso','nombre','Anio','Mes']
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                input("Desea continuar??: ")
                nombre = input("Ingrese su nombre: ")

                query = f'''Update Curso set nombre = '{nombre}' where codCurso = {Id};'''

            if(ansMenuSec == "5"):
                query = "Select * from Curso;"
                header = ['codCurso','Nombre']
                query2 = "Select codProf, nombre from Profesor;"
                header2 = ['codProf','nombre']
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                res2 = conexion.consultarBDD(query=query2)
                print(tabulate(res2, headers=header2, tablefmt='fancy_grid'))

                query = f"Select * from cursoProfes;"
                header = ['codigo','CodigoCurso','CodigoProfesor']
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                input("Desea continuar??: ")
                Id = int(input("Ingrese el Código: "))
                codCurso = input("Ingrese Código del Curso: ")
                codDocente = input("Ingrese Código su Codigo Docente: ")

                query = f'''Update cursoProfes set codCurso = '{codCurso}', codProf = '{codDocente}' where codigo = {Id};'''

            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")

        if(ansMenuPrincipal=="3"):
            menuSecundario = ""
            opMenuSec = {"Alumnos": "1", "Profesor": "2","Curso": "3","Asignar Curso a un Profesor": "4","Salir": "0"}
            menuSec = Menu("Secundario", opMenuSec)
            ansMenuSec = menuSec.show()

            if(ansMenuSec == "1"):
                nombre = input("Ingrese su nombre: ")
                iden = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")
                query= f'''insert into Alumno (nombre, identificador, edad, correo) values ('{nombre}','{iden}',{edad},'{correo}');'''
            if(ansMenuSec == "2"):
                nombre = input("Ingrese su nombre: ")
                iden = input("Ingrese su dni: ")
                edad = int(input("Ingrese su edad: "))
                correo = input("Ingrese su correo: ")
                query= f'''insert into Profesor (nombre, identificador, edad, correo) values ('{nombre}','{iden}',{edad},'{correo}');'''
            if(ansMenuSec == "3"):
                nombre = input("Ingrese su nombre: ")
                query= f'''insert into Curso (nombre) values ('{nombre}');'''
            if(ansMenuSec == "4"):
                query = "Select * from Curso;"
                header = ['codCurso','Nombre']
                query2 = "Select codProf, nombre from Profesor;"
                header2 = ['codProf','nombre']
                res = conexion.consultarBDD(query=query)
                print(tabulate(res, headers=header, tablefmt='fancy_grid'))
                res2 = conexion.consultarBDD(query=query2)
                print(tabulate(res2, headers=header2, tablefmt='fancy_grid'))

                input("Desea continuar??: ")
                curso = int(input("Ingrese código Curso: "))
                profesor = int(input("Ingrese código Profesor: "))
                query= f'''insert into cursoProfes (codCurso, codProf) values ({curso}, {profesor});'''

            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")


except Exception as error:
    print(str(error))