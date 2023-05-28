from conexion import conexion
from tabulate import tabulate
import utils
class Salon:

    def __init__(self, idSalon, nombre, anioEscolar):
        self.idSalon = idSalon
        self.nombre = nombre
        self.anioEscolar = anioEscolar


    __cn = conexion()  
    __lstSalones = []

    def cargarSalon():        
        query = "select * from salon;"
        res = Salon.__cn.ConsultarQuery(query=query)
        for sln in res:
            salon = Salon(sln[0], sln[1], sln[2])
            Salon.__lstSalones.append(salon)

    def listarSalon():
        header = ['ID','Nombre','Año Escolar']
        query = "SELECT * FROM salon;"
        res = Salon.__cn.ConsultarQuery(query=query)
        print(utils.color.BLUE + tabulate(res, headers=header, tablefmt='fancy_grid')+ utils.color.END)
        input(utils.color.GREEN+"Presione 'Enter' para continuar..."+utils.color.END)

    def crearSalon():
        try:
            nombre = input("Nombre de salon: ")
            anio = input("Año Escolar: ")
            query= f'''insert into salon(nombre,anioEscolar)
                    values('{nombre}',{anio});'''
            if(Salon.__cn.EjecutarQuery(query=query)):
                Salon.listarsalon()
                print("Datos creados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)

    def editarSalon():
        try:
            idsalon = int(input("Ingrese el ID del salon a editar: "))
            query = f"Select * from salon where idSalon = {idsalon};"
            res = Salon.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','Año Escolar']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            nombre = input("Nombre de salon: ")
            anio = input("Año Escolar: ")

            queryUpdate = f'''Update salon 
                    set nombre = '{nombre}',
                    anioEscolar = '{anio}' where idSalon = {idsalon};'''
            if(Salon.__cn.EjecutarQuery(query=queryUpdate)):
                Salon.listarsalon()
                print("Datos actualizados correctamente")
                input("¿Desea Continuar S/N? -> ")
        except Exception as ex:
            print("Error al ingresar los datos",ex)
        
    def eliminarSalon():
        try:
            idsalon = int(input("¿Que salon deseas borrar?: "))
            query = f"Select * from salon where idSalon = {idsalon};"
            res = Salon.__cn.ConsultarQuery(query=query)
            header = ['ID','Nombre','Año Escolar']
            print(tabulate(res, headers=header, tablefmt='fancy_grid'))
            input("¿Desea Continuar S/N? -> ")
            query = f''' delete from salon
                where idSalon = {idsalon};'''
            if(Salon.__cn.EjecutarQuery(query=query)):
                Salon.listarsalon()
                print("Datos borrados correctamente")
                input("¿Desea Continuar S/N? -> ")          
        except Exception as ex:
            print("Error al ingresar los datos",ex)