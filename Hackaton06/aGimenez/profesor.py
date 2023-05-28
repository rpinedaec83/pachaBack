from clases import Profesor, Salon, SalonProfesor, CursoProfesor
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

def mostrarProfesores():
    header = ['Identificador Profesor', 'Nombre Profesor', 'Edad', 'Correo']
    query = "Select * from Profesor;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarProfesor():
    identProfesor = input("Ingrese Identificador de Profesor: ")
    header = ['Identificador Profesor', 'Nombre Profesor', 'Edad', 'Correo']
    query = f"Select * from Profesor where identProfesor = '{identProfesor}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))
    return identProfesor

def editarProfesor():
    identProfesor = buscarProfesor()
    identProfesorNuevo = input("Ingrese Identificador: ")
    nombre = input("Ingresa Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingresa Correo: ")
    query = f'''Update Profesor 
        set 
        identProfesor = '{identProfesorNuevo}',nombreProfesor = '{nombre}', 
        edad = {edad}, 
        correo = '{correo}'
        where identProfesor = '{identProfesor}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearProfesor():
    identificador = input("Ingrese Identificador: ")
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingrese Correo: ")
    profesor = Profesor(identificador, nombre, edad, correo)
    query = f'''insert into Profesor( identProfesor, nombreProfesor, edad, correo)
        values('{profesor.identificador}', '{profesor.nombre}', {profesor.edad}, '{profesor.correo}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarProfesor():
    identProfesor = buscarProfesor()
    query = f''' delete from Profesor
        where identProfesor = '{identProfesor}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")

def mostrarListaSalonProfesor():
    header = ['Codigo', 'Id Salon', 'Nombre Salon', 'Identificador Profesor', 'Nombre Profesor']
    query = f"Select idSalonProfesor, sl.IdSalon, sl.nombreSalon, pr.identProfesor, pr.nombreProfesor from SalonProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def mostrarSalonProfesor():
    identProfesor = input("Ingrese Identificador de Profesor: ")
    header = ['Id Salon', 'Nombre Salon','Identificador Profesor', 'Nombre Profesor']
    query = f"Select sl.IdSalon, sl.nombreSalon, pr.identProfesor, pr.nombreProfesor from SalonProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon where pr.IdentProfesor = '{identProfesor}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarSalonProfesor(identProfesor, IdSalon):
    header = ['Id Salon', 'Nombre Salon','Identificador Profesor', 'Nombre Profesor']
    query = f"Select sl.IdSalon, sl.nombreSalon, pr.identProfesor, pr.nombreProfesor  from SalonProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon where pr.IdentProfesor = '{identProfesor}' and sl.IdSalon = {IdSalon};"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def editarSalonProfesor():
    identProfesor = input("Ingrese Identificador de Profesor: ")
    IdSalon = int(input("Ingrese Salon: "))
    buscarSalonProfesor(identProfesor, IdSalon)
    IdSalonNuevo = input("Ingrese Id Salon Nuevo: ")
    query = f'''Update SalonProfesor 
        set 
        IdSalon = '{IdSalonNuevo}'
        where identProfesor = '{identProfesor}' and IdSalon = {IdSalon};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearSalonProfesor():
    identProfesor = input("Ingrese Identificador Profesor: ")
    IdSalon = int(input("Ingrese Id Salon: "))
    salonProfesor = SalonProfesor(IdSalon, identProfesor)
    query = f'''insert into SalonProfesor(IdSalon, IdentProfesor)
        values('{salonProfesor.IdSalon}', '{salonProfesor.IdentProfesor}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarSalonProfesor():
    mostrarListaSalonProfesor()
    identProfesor = input("Ingrese Identificador de Profesor: ")
    IdSalon = int(input("Ingrese Salon: "))
    buscarSalonProfesor(identProfesor, IdSalon)
    query = f''' delete from SalonProfesor
        where identProfesor = '{identProfesor}' and IdSalon = {IdSalon};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")

def mostrarListaCursoProfesor():
    header = ['Codigo', 'Id Curso', 'Nombre Curso', 'Identificador Profesor', 'Nombre Profesor']
    query = f"Select idCursoProfesor, sl.IdCurso, sl.nombreCurso, pr.identProfesor, pr.nombreProfesor from CursoProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Curso AS sl ON sa.IdCurso = sl.IdCurso;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def mostrarCursoProfesor():
    identProfesor = input("Ingrese Identificador de Profesor: ")
    header = ['Id Curso', 'Nombre Curso','Identificador Profesor', 'Nombre Profesor']
    query = f"Select sl.IdCurso, sl.nombreCurso, pr.identProfesor, pr.nombreProfesor from CursoProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Curso AS sl ON sa.IdCurso = sl.IdCurso where pr.IdentProfesor = '{identProfesor}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarCursoProfesor(identProfesor, IdCurso):
    header = ['Id Curso', 'Nombre Curso','Identificador Profesor', 'Nombre Profesor']
    query = f"Select sl.IdCurso, sl.nombreCurso, pr.identProfesor, pr.nombreProfesor  from CursoProfesor AS sa INNER JOIN Profesor AS pr ON sa.IdentProfesor = pr.IdentProfesor INNER JOIN Curso AS sl ON sa.IdCurso = sl.IdCurso where pr.IdentProfesor = '{identProfesor}' and sl.IdCurso = {IdCurso};"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def editarCursoProfesor():
    identProfesor = input("Ingrese Identificador de Profesor: ")
    IdCurso = int(input("Ingrese Curso: "))
    buscarCursoProfesor(identProfesor, IdCurso)
    IdCursoNuevo = input("Ingrese Id Curso Nuevo: ")
    query = f'''Update CursoProfesor 
        set 
        IdCurso = '{IdCursoNuevo}'
        where identProfesor = '{identProfesor}' and IdCurso = {IdCurso};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearCursoProfesor():
    identProfesor = input("Ingrese Identificador Profesor: ")
    IdCurso = int(input("Ingrese Id Curso: "))
    cursoProfesor = CursoProfesor(IdCurso, identProfesor)
    query = f'''insert into CursoProfesor(IdCurso, IdentProfesor)
        values('{cursoProfesor.IdCurso}', '{cursoProfesor.IdentProfesor}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarCursoProfesor():
    mostrarListaCursoProfesor()
    identProfesor = input("Ingrese Identificador de Profesor: ")
    IdCurso = int(input("Ingrese Curso: "))
    buscarCursoProfesor(identProfesor, IdCurso)
    query = f''' delete from CursoProfesor
        where identProfesor = '{identProfesor}' and IdCurso = {IdCurso};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")
