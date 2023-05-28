from clases import Alumno, NotasBimetrales, Salon, SalonAlumno
from conexion import conexion
from tabulate import TableFormat, tabulate

conexion = conexion()

def mostrarAlumnos():
    header = ['Identificador Alumno', 'Nombre Alumno', 'Edad', 'Correo']
    query = "Select * from Alumno;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))
  
def buscarAlumno():
    identAlumno = input("Ingrese Identificador de Alumno: ")
    header = ['Identificador Alumno', 'Nombre Alumno', 'Edad', 'Correo']
    query = f"Select * from Alumno where identAlumno = '{identAlumno}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))
    return identAlumno

def editarAlumno():
    identAlumno = buscarAlumno()
    identAlumnoNuevo = input("Ingrese Identificador: ")
    nombre = input("Ingresa Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingresa Correo: ")
    query = f'''Update Alumno 
        set 
        identAlumno = '{identAlumnoNuevo}',nombreAlumno = '{nombre}', 
        edad = {edad}, 
        correo = '{correo}'
        where identAlumno = '{identAlumno}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearAlumno():
    identificador = input("Ingrese Identificador: ")
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingresa Edad: "))
    correo = input("Ingrese Correo: ")
    alumno = Alumno(identificador, nombre, edad, correo)
    query = f'''insert into Alumno( identAlumno, nombreAlumno, edad, correo)
        values('{alumno.identificador}', '{alumno.nombre}', {alumno.edad}, '{alumno.correo}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarAlumno():
    identAlumno = buscarAlumno()
    query = f''' delete from Alumno
        where identAlumno = '{identAlumno}';'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")

def mostrarListaSalonAlumno():
    header = ['Codigo', 'Id Salon', 'Nombre Salon', 'Identificador Alumno', 'Nombre Alumno']
    query = f"Select idSalonAlumno, sl.IdSalon, sl.nombreSalon, al.identAlumno, al.nombreAlumno from SalonAlumno AS sa INNER JOIN Alumno AS al ON sa.IdentAlumno = al.IdentAlumno INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon;"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def mostrarSalonAlumno():
    identAlumno = input("Ingrese Identificador de Alumno: ")
    header = ['Id Salon', 'Nombre Salon','Identificador Alumno', 'Nombre Alumno']
    query = f"Select sl.IdSalon, sl.nombreSalon, al.identAlumno, al.nombreAlumno from SalonAlumno AS sa INNER JOIN Alumno AS al ON sa.IdentAlumno = al.IdentAlumno INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon where al.IdentAlumno = '{identAlumno}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def buscarSalonAlumno(identAlumno, IdSalon):
    header = ['Id Salon', 'Nombre Salon','Identificador Alumno', 'Nombre Alumno']
    query = f"Select sl.IdSalon, sl.nombreSalon, al.identAlumno, al.nombreAlumno  from SalonAlumno AS sa INNER JOIN Alumno AS al ON sa.IdentAlumno = al.IdentAlumno INNER JOIN Salon AS sl ON sa.IdSalon = sl.IdSalon where al.IdentAlumno = '{identAlumno}' and sl.IdSalon = {IdSalon};"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))

def editarSalonAlumno():
    identAlumno = input("Ingrese Identificador de Alumno: ")
    IdSalon = int(input("Ingrese Salon: "))
    buscarSalonAlumno(identAlumno, IdSalon)
    IdSalonNuevo = input("Ingrese Id Salon Nuevo: ")
    query = f'''Update SalonAlumno 
        set 
        IdSalon = '{IdSalonNuevo}'
        where identAlumno = '{identAlumno}' and IdSalon = {IdSalon};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearSalonAlumno():
    identAlumno = input("Ingrese Identificador Alumno: ")
    IdSalon = int(input("Ingrese Id Salon: "))
    salonAlumno = SalonAlumno(IdSalon, identAlumno)
    query = f'''insert into SalonAlumno(IdSalon, IdentAlumno)
        values('{salonAlumno.IdSalon}', '{salonAlumno.IdentAlumno}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarSalonAlumno():
    mostrarListaSalonAlumno()
    identAlumno = input("Ingrese Identificador de Alumno: ")
    IdSalon = int(input("Ingrese Salon: "))
    buscarSalonAlumno(identAlumno, IdSalon)
    query = f''' delete from SalonAlumno
        where identAlumno = '{identAlumno}' and IdSalon = {IdSalon};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")

def buscarNotaAlumno():
    identAlumno = input("Ingrese Identificador de Alumno: ")
    header = ['Codigo', 'Identificador Alumno', 'Nota', 'Año Escolar', 'Bimestre']
    query = f"Select * from NotaBimestral where identAlumno = '{identAlumno}';"
    res = conexion.consultarBDD(query = query)
    print(tabulate(res, headers=header, tablefmt='youtrack'))
    return identAlumno

def editarNotaAlumno():
    identAlumno = buscarNotaAlumno()
    codigo = int(input("Ingrese Codigo de Nota que desea editar: "))
    nota = float(input("Ingresa Nota: "))
    añoEscolar = int(input("Ingresa Año Escolar: "))
    bimestre = input("Ingresa Bimestre: ")
    query = f'''Update NotaBimestral 
        set 
        nota = '{nota}', 
        anioEscolar = {añoEscolar}, 
        bimestre = '{bimestre}'
        where idNotaBimestral = {codigo};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos actualizados correctamente")

def crearNotaAlumno():
    identificador = input("Ingrese Identificador: ")
    nota = float(input("Ingrese Nota: "))
    añoEscolar = int(input("Ingresa Año Escolar: "))
    bimestre = input("Ingrese Bimestre: ")
    notaBimestral = NotasBimetrales(identificador, nota, añoEscolar, bimestre)
    query = f'''insert into NotaBimestral(identAlumno, nota, anioEscolar, bimestre)
        values('{notaBimestral.identificador}', {notaBimestral.nota}, {notaBimestral.añoEscolar}, '{notaBimestral.bimestre}');'''
    if(conexion.ejecutarBDD(query)):
        print("Datos creados correctamente")

def eliminarNotaAlumno():
    identAlumno = buscarNotaAlumno()
    codigo = int(input("Ingrese Codigo de Nota que desea eliminar: "))
    query = f''' delete from NotaBimestral
        where idNotaBimestral = {codigo};'''
    if(conexion.ejecutarBDD(query)):
        print("Datos borrados correctamente")
