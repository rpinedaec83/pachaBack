from clases import Salon
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

def mostrarSalones():
    header = ['Id Salon', 'Nombre']
    query = "Select * from Salon;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarSalon():
    nombre = input("Ingrese Nombre Salon: ")
    header = ['Id Salon', 'Nombre']
    query = f"Select * from Salon where nombreSalon = '{nombre}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def editarSalon():
    buscarSalon()
    IdSalon = int(input("Ingrese Id de Salon que desea editar: "))
    nombreNuevo = input("Ingrese Nombre: ")
    query = f'''Update Salon
        set 
        nombreSalon = '{nombreNuevo}'
        where IdSalon = '{IdSalon}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearSalon():
    nombre = input("Ingrese Nombre: ")
    salon = Salon(nombre)
    query = f'''insert into Salon(nombreSalon)
        values('{salon.nombre}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarSalon():
    buscarSalon()
    IdSalon = int(input("Ingrese Id de Salon que desea eliminar: "))
    query = f''' delete from Salon
        where IdSalon = '{IdSalon}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")
