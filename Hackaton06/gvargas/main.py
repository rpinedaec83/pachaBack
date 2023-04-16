from utils import Menu
from tablas import Alumnos
from tablas import Profesores
from tablas import Salones
from tablas import Cursos
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()
lstAlumnos = []
lstSalones = []
lstCursos = []
lstProfesores = []

def cargaAlumnos():
    query = "Select * from Alumnos;"
    res = conexion.consultarBDD(query=query)
    for alu in res:
        alumno = Alumnos(alu[0], alu[1], alu[2], alu[3], alu[4], alu[5])
        lstAlumnos.append(alumno)
cargaAlumnos()
def cargaSalones():
    query = "Select * from Salon;"
    res = conexion.consultarBDD(query=query)
    for sal in res:
        salon = Salones(sal[0], sal[1])
        lstSalones.append(salon)
cargaSalones()
def cargaCursos():
    query = "Select * from Cursos;"
    res = conexion.consultarBDD(query=query)
    for cur in res:
        curso = Cursos(cur[0], cur[1])
        lstCursos.append(curso)
cargaCursos()
def cargaProfesores():
    query = "Select * from Profesor;"
    res = conexion.consultarBDD(query=query)
    for pro in res:
        profesor = Profesores(pro[0], pro[1], pro[2], pro[3], pro[4])
        lstProfesores.append(profesor)
cargaProfesores()
try:
    opMenuPrincipal = {"Mostrar Alumnos": "1", "Editar Alumnos": "2","Crear Alumno": "3","Borrar Alumno":"4", "Mostrar Profesores": "5", "Editar Profesor": "6","Crear Profesor": "7","Borrar Profesor":"8", "Mostrar Cursos": "9", "Editar Curso": "10","Crear Curso": "11","Borrar Curso":"12","Mostrar Salones": "13", "Editar Salon": "14","Crear Salon": "15","Borrar Salon":"16","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        if(ansMenuPrincipal == "1"):
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            query = "Select * from Alumnos;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "2"):
            IdAlumno = int(input("Que alumno deseas editar: "))
            query = f"Select * from Alumnos where IdAlumno = {IdAlumno};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            nota = int(input("Dime tu nota: "))
            query = f'''Update Alumnos 
                set Nombre = '{nombre}',
                Edad = {edad},
                Correo = {correo},
                Salon = {salon},
                Notas = {nota},
                where IdAlumno = {IdAlumno};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="3"):
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            nota = int(input("Dime tu nota: "))
            query= f'''insert into Alumnos(Nombre,Edad,Correo,Salon,Notas)
                     values('{nombre}',{edad},'{correo}',{salon},{nota});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "4"):
            IdAlumno = int(input("Que alumno deseas borrar: "))
            query = f"Select * from Alumnos where IdCliente = {IdAlumno};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','Edad','Correo','Salon', 'Notas']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from Alumnos
                where IdAlumno = {IdAlumno};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "5"):
            header = ['ID','Nombre','Edad','Correo','Salon']
            query = "Select * from Profesor;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "6"):
            IdProfesor = int(input("Que profesor deseas editar: "))
            query = f"Select * from Profesor where IdProfesor = {IdProfesor};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','Edad','Correo','Salon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            query = f'''Update Profesor 
                set Nombre = '{nombre}',
                Edad = {edad},
                Correo = {correo},
                Salon = {salon},
                where IdProfesor = {IdProfesor};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="7"):
            nombre = input("Dime tu nombre: ")
            edad = int(input("Dime tu edad: "))
            correo = int(input("Dime tu correo: "))
            salon = int(input("Dime tu salon: "))
            query= f'''insert into Profesor(Nombre,Edad,Correo,Salon)
                     values('{nombre}',{edad},'{correo}',{salon});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "8"):
            IdProfesor = int(input("Que profesor deseas borrar: "))
            query = f"Select * from Profesor where IdProfesor = {IdProfesor};"
            res = conexion.consultarBDD(query=query)
            header = ['ID','Nombre','Edad','Correo','Salon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from Profesor
                where IdProfesor = {IdProfesor};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "9"):
            header = ['Nombre','Profesor']
            query = "Select * from Cursos;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "10"):
            Nombre = int(input("Que curso deseas editar: "))
            query = f"Select * from Cursos where Nombre = {Nombre};"
            res = conexion.consultarBDD(query=query)
            header = ['Nombre','Profesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            profesor = input("Dime tu profesor: ")
            query = f'''Update Profesor 
                set profesor = '{profesor}',
                where Nombre = {Nombre};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="11"):
            profesor = input("Dime tu profesor: ")
            query= f'''insert into Cursos(Profesor)
                     values('{profesor});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "12"):
            Nombre = int(input("Que curso deseas borrar: "))
            query = f"Select * from Cursos where Nombre = {Nombre};"
            res = conexion.consultarBDD(query=query)
            header = ['Nombre','Profesor']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from Cursos
                where Nombre = {Nombre};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "13"):
            header = ['Nombre','Año escolar']
            query = "Select * from Salon;"
            res = conexion.consultarBDD(query=query)
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
        if(ansMenuPrincipal == "14"):
            Nombre = int(input("Que salon deseas editar: "))
            query = f"Select * from Salon where Nombre = {Nombre};"
            res = conexion.consultarBDD(query=query)
            header = ['Nombre','Año']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            anho = input("Dime tu año escolar: ")
            query = f'''Update Salon 
                set Año_escolar = '{anho}',
                where Nombre = {Nombre};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos actualizados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal=="15"):
            anho = input("Dime tu año escolar: ")
            query= f'''insert into Salon(Año_escolar)
                     values('{anho});'''
            if(conexion.ejecutarBDD(query)):
                print("Datos creados correctamente")
                input("Desea continuar???")
        if(ansMenuPrincipal == "16"):
            Nombre = int(input("Que salon deseas borrar: "))
            query = f"Select * from Salon where Nombre = {Nombre};"
            res = conexion.consultarBDD(query=query)
            header = ['Nombre','Año escolar']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("Desea contunuar??")
            query = f''' delete from Salon
                where Nombre = {Nombre};'''
            if(conexion.ejecutarBDD(query)):
                print("Datos borrados correctamente")
                input("Desea continuar???")
except Exception as error:
    print(str(error))
