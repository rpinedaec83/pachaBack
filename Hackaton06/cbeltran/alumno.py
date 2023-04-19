from conexion import conexion
from tabulate import tabulate
import utils
class Alumno():
    
    def __init__(self, idAlumno, nombre, dni, edad, email, idSalon):
        self.idAlumno = idAlumno
        self.nombre = nombre
        self.dni = dni
        self. edad = edad
        self.email = email
        self.idSalon = idSalon

    __cn = conexion()  
    __lstAlumnos = []

    def cargarAlumnos():        
        query = "select * from alumno;"
        res = Alumno.__cn.ConsultarQuery(query=query)
        for alm in res:
            alumno = Alumno(alm[0], alm[1], alm[2], alm[3], alm[4], alm[5])
            Alumno.__lstAlumnos.append(alumno)

    def listarAlumno():
        header = ['ID','Nombre','dni','edad','correo', 'idsalon']
        query = "SELECT * FROM alumno;"
        res = Alumno.__cn.ConsultarQuery(query=query)
        print(utils.color.BLUE + tabulate(res, headers=header, tablefmt='fancy_grid')+ utils.color.END)
        input(utils.color.GREEN+"Presione 'Enter' para continuar..."+utils.color.END)


    def crearAlumno():
        try:
            nombre = input("Nombre de Alumno: ")
            dni = input("DNI: ")
            edad = int(input("Edad: "))
            email = input("Correo electrónico: ")
            idsalon = int(input("ID del Salón: "))
            query= f'''insert into alumno(nombre,dni,edad,email,idSalon)
                    values('{nombre}','{dni}',{edad},'{email}',{idsalon});'''
            if(Alumno.__cn.EjecutarQuery(query=query)):
                Alumno.listarAlumno()
                print("Datos creados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)

    def editarAlumno():
        try:
            idAlumno = int(input("Ingrese el ID del alumno a editar: "))
            query = f"Select * from alumno where idAlumno = {idAlumno};"
            res = Alumno.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','dni','edad','correo', 'idsalon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            nombre = input("Nombre de Alumno: ")
            dni = input("DNI: ")
            edad = int(input("Edad: "))
            email = input("Correo electrónico: ")
            idsalon = int(input("ID del Salón: "))

            queryUpdate = f'''Update alumno 
                    set nombre = '{nombre}',
                    dni = '{dni}',
                    edad = {edad},
                    email = '{email}',
                    idSalon = {idsalon} where idAlumno = {idAlumno};'''
            if(Alumno.__cn.EjecutarQuery(query=queryUpdate)):
                Alumno.listarAlumno()
                print("Datos actualizados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)
        
    def eliminarAlumno():
        try:
            idAlumno = int(input("¿Que alumno deseas borrar?: "))
            query = f"Select * from alumno where idAlumno = {idAlumno};"
            res = Alumno.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','dni','edad','correo', 'idsalon']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            query = f''' delete from alumno
                where idAlumno = {idAlumno};'''
            if(Alumno.__cn.EjecutarQuery(query=query)):
                Alumno.listarAlumno()
                print("Datos borrados correctamente")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)
