import os
import time
import fun
import json

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class Alumno(Persona):
    def __init__(self, nombre, edad, dni, notamay, notamen, promedio):
        super().__init__(nombre, edad, dni)
        self.notamay = notamay
        self.notamen = notamen
        self.promedio = promedio

class Docente(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
     
    def limpiarPantalla(self):
        def clear():
                #return os.system('cls')
            return os.system('clear')
        clear()

f = True

fileDocente = fun.fileManager("docentes.txt")
fileAlumno = fun.fileManager("alumnos.txt")

notas = []
alumno_list = []
docente_list = []
alumno_listDic = []
docente_listDic = []

def cargainicial():
    res = fileDocente.leerArchivo()
    print(res)
    if(res != ""):
        listTempDocente = json.loads(res)
        for dic in listTempDocente:
            newDocente = Docente(dic["Docente"],dic["Edad"],dic["Dni"])
            docente_listDic.append(newDocente.toDic())
            docente_list.append(newDocente)

    res = fileAlumno.leerArchivo()
    print(res)
    if(res != ""):
        listTempAlumno = json.loads(res)
        for dic in listTempAlumno:
            newAlumno = Docente(dic["Alumno"],dic["máxima nota"],dic["minima nota"],dic["promedio"])
            alumno_listDic.append(newAlumno.toDic())
            alumno_list.append(newAlumno)

cargainicial()

clase = input("Usted es: Docente(1) o Alumno(2): ")
if clase == "1":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dni = input("Ingrese su dni: ")
    nuevo_docente = Docente(nombre,edad,dni)
    docente_listDic.append(nuevo_docente.toDic())
    jsonString = json.dumps(docente_listDic)
    fileDocente.borrarArchivo()
    fileDocente.escribirArchivo(jsonString)
elif clase == "2":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dni = input("Ingrese su dni: ")
    n = 0
    while n < 4 & f == True:
        notas[n] = int(input("Ingrese su nota: "))
        m = n + 1
        if n<3:
            c = input("Desea ingresar otra nota, Si(1), No(2): ")
            if c == 2:
                f = False

    suma = 0
    notamay = 0
    notamen = 20
    m = n

    while n > 0:
        suma = suma + notas[n]
        if notas[n]>notamay:
            notamay = notas[n]
        if notas[n]<notamen:
            notamen = notas[n]
        if n == 1:
            promedio = suma/m

    
    nuevo_alumno = Alumno(nombre,edad,dni,notamay,notamen,promedio)
    alumno_listDic.append(nuevo_alumno.toDic())
    jsonString = json.dumps(alumno_listDic)
    fileAlumno.borrarArchivo()
    fileAlumno.escribirArchivo(jsonString)
else:
    print("Usted ingreso una clave incorrecta")



# while f:
