import utils
import time
import os
import json

class Persona:

    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    def toDic(self):
        d = {
            "dni":self.dni,
            "nombre":self.nombre,
            "edad":self.edad        
        }
        return d

class Alumno(Persona): 

    def __init__(self, dni, nombre, edad):
        super().__init__( dni, nombre, edad)

class Profesor(Persona):
    def __init__(self, dni, nombre, edad):
        super().__init__(dni, nombre, edad)


class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones


    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("\n")
            print("::::::::::::::::::::"+
                self.nombreMenu.upper()+"::::::::::::::::::::")   
            print("\n")
            for (key, value) in self.listaOpciones.items():
                print(key + " → " + value)
            print("\n")
            rpta = input("Por favor, ingrese su opción: ")
            print("\n")
            if(rpta.upper() == "0"):
                self.limpiarPantalla()
                print("Programa finalizado: Hasta, pronto")
                break
            b = 0
            for (key, value) in self.listaOpciones.items():
                if (value == rpta):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print("Opción no valida, escoja una opción valida")
                time.sleep(2)
        return rpta     
    
    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear() 

Home_op = {"Registro de Alumnos":"1","Registro de Docentes":"3","Exit":"0"}
Main_menu = Menu("menú",Home_op)

Alumno_op = {"Agregar alumno":"1", "Reporte de Alumnos":"2","Exit":"0"}
Menu_alumno = Menu("registro de alumnos",Alumno_op)

Docente_op = {"Agregar Docente":"1", "Reporte de Docentes":"2", "Exit":"0"}
Menu_docente = Menu("registro de docentes",Docente_op)




archivoAlumno = utils.fileManager("alumnos.txt")
listaAlumno = []
listaDicAlumno = []
def cargaInicialAlumno():
    res = archivoAlumno.leerArchivo()
    print(res)
    if (res != ""):
        listTempAlumno = json.loads(res)
        for dic in listTempAlumno:
            alumnoNuevo = Alumno(dic["dni"],dic["nombre"],dic["edad"])
            listaAlumno.append(alumnoNuevo)

archivoDocente = utils.fileManager("docentes.txt")
listaDocente = []
listaDicDocente = []
def cargaInicialDocente():
    res = archivoDocente.leerArchivo()
    print(res)
    if (res != ""):
        listTempDocente = json.loads(res)
        for dic in listTempDocente:
            docenteNuevo = Profesor(dic["dni"],dic["nombre"],dic["edad"])
            listaDocente.append(docenteNuevo)



f = True
while f:
    rpta  = Main_menu.show()
#Alumnos
    if (rpta.upper() == "1"):
        cargaInicialAlumno()
        rpta = Menu_alumno.show()
        if(rpta.upper() == "1"):
            print("===Ingrese los datos del alumno===\n")
            dni = input("DNI del alumno: ")
            nombre = input("Nombre del alumno: ")
            edad = input("Edad del alumno: ")
            print("")
            alumno_n = Alumno(dni,nombre,edad)
            listaAlumno.append(alumno_n)
            print("")
            print(f"Alumno {nombre} fue agregado ☑")
            listaDicAlumno.append(alumno_n.toDic())
            jsonString = json.dumps(listaDicAlumno)
            archivoAlumno.borrarArchivo()
            archivoAlumno.escribirArchivo(jsonString)
            break

        elif(rpta.upper() =="2"):
            print("Lista de Alumnos ☑:")
            for alumno in listaAlumno:
                print(f"|    DNI    | NOMBRE |  EDAD  |\n")
                print(f"|{alumno.dni}|{alumno.nombre}|{alumno.edad}|")
#Docente
    if (rpta.upper() == "3"):
        cargaInicialDocente()
        rpta = Menu_docente.show()
        if(rpta.upper() == "1"):
            print("===Ingrese los datos del docente===\n")
            dni = input("DNI del docente: ")
            nombre = input("Nombre del docente: ")
            edad = input("Edad del docente: ")
            print("")
            docente_n = Profesor(dni,nombre,edad)
            listaDocente.append(docente_n)
            print("")
            print(f"Docente {nombre} fue agregado ☑")
            listaDicDocente.append(docente_n.toDic())
            jsonString = json.dumps(listaDicDocente)
            archivoDocente.borrarArchivo()
            archivoDocente.escribirArchivo(jsonString)
            break

        elif(rpta.upper() =="2"):
            print("Lista de docentes ☑:")

            for docente in listaDocente:
                print(f"|    DNI    |  NOMBRE  |  EDAD  |\n")
                print(f"| {docente.dni} | {docente.nombre} | {docente.edad} |")            
    break