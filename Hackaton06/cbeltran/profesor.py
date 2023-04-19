from conexion import conexion
from tabulate import tabulate
import utils

class Profesor:

    def __init__(self, idProfesor, nombre, dni, edad, email):
        self.idProfesor = idProfesor
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.email = email

    __cn = conexion()  
    __lstProfesores = []

    def cargarProfesor():        
        query = "select * from profesor;"
        res = Profesor.__cn.ConsultarQuery(query=query)
        for prf in res:
            profesor = Profesor(prf[0], prf[1], prf[2], prf[3], prf[4])
            Profesor.__lstProfesores.append(profesor)

    def listarProfesor():
        header = ['ID','Nombre','DNI','Edad','Correo']
        query = "SELECT * FROM profesor;"
        res = Profesor.__cn.ConsultarQuery(query=query)
        print(utils.color.BLUE + tabulate(res, headers=header, tablefmt='fancy_grid')+ utils.color.END)
        input(utils.color.GREEN+"Presione 'Enter' para continuar..."+utils.color.END)

    def crearProfesor():
        try:
            nombre = input("Nombre de profesor: ")
            dni = input("DNI: ")
            edad = int(input("Edad: "))
            email = input("Correo electrónico: ")
            query= f'''insert into profesor(nombre,dni,edad,email,idSalon)
                    values('{nombre}','{dni}',{edad},'{email}');'''
            if(Profesor.__cn.EjecutarQuery(query=query)):
                Profesor.listarProfesor()
                print("Datos creados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)

    def editarProfesor():
        try:
            idprofesor = int(input("Ingrese el ID del profesor a editar: "))
            query = f"Select * from profesor where idProfesor = {idprofesor};"
            res = Profesor.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','DNI','Edad','Correo']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            nombre = input("Nombre de profesor: ")
            dni = input("DNI: ")
            edad = int(input("Edad: "))
            email = input("Correo electrónico: ")

            queryUpdate = f'''Update profesor 
                    set nombre = '{nombre}',
                    dni = '{dni}',
                    edad = {edad},
                    email = '{email}' where idProfesor = {idprofesor};'''
            if(Profesor.__cn.EjecutarQuery(query=queryUpdate)):
                Profesor.listarProfesor()
                print("Datos actualizados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)
        
    def eliminarProfesor():
        try:
            idprofesor = int(input("¿Que profesor deseas borrar?: "))
            query = f"Select * from profesor where idProfesor = {idprofesor};"
            res = Profesor.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','DNI','Edad','Correo']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            query = f''' delete from profesor
                where idProfesor = {idprofesor};'''
            if(Profesor.__cn.EjecutarQuery(query=query)):
                Profesor.listarProfesor()
                print("Datos borrados correctamente")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)