import os
import shutil
import json
import time

#alt + shift + arrow -> to duplicate
#ctrl + } -> comentar


#os.makedirs
#os.removedirs
#directActual = os.getcwd()# current path
#archivoActual = "main.py"
#dirActual = os.getcwd()

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
    json = {}
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.DNI = DNI
        self.edad = edad

        self.json = {"Nombre": self.nombre,"Dni": self.DNI,"Edad": self.edad}

class Profesor(Persona):
    def __init__(self, nombre, edad, DNI):
        super().__init__(nombre, edad, DNI)

class Alumno(Persona):

    def __init__(self, nombre, edad, DNI, list_notas):
        super().__init__(nombre, edad, DNI)
        self.list_notas = list_notas[:4]

        self.json["Notas"] = {
        "NotasMax":self.get_MaxNota(),
        "NotasMin":self.get_MinNota(),
        "NotasEnTotal": self.list_notas
    }


    def get_MaxNota(self):
        return max(self.list_notas)
    

    def get_MinNota(self):
        return min(self.list_notas)

    def promedioNotas(self):
        resul = 0
        for i in self.list_notas:
            resul += i

        return resul/len(self.list_notas)

class JsonManager:

    def __init__(self):
        if((os.path.exists("Reportes_Jsons")) == False):
            os.makedirs("Reportes_Jsons")
        self.direccionFile_Alumnos = "Reportes_Jsons\JAlumnos.json"
        self.direccionFile_Profes = "Reportes_Jsons\JDocentes.json"
        self.initDictionaries()

    def initDictionaries(self):
        with open(self.direccionFile_Alumnos,"w") as file:
            json.dump({"Alumnos":{}},file, indent=4)

        with open(self.direccionFile_Profes,"w") as file:
            json.dump({"Docentes":{}},file, indent=4)

    def addAlumno(self, persona):

        dataJson = {}

        with open(self.direccionFile_Alumnos,"r") as file:
            dataJson = json.load(file)

            if persona.nombre not in dataJson["Alumnos"].keys():
                dataJson["Alumnos"][persona.nombre] = persona.json

        with open(self.direccionFile_Alumnos, "w") as file:
            json.dump(dataJson, file, indent=4)

    def removeAlumno(self, persona):

        dataJson = {}

        with open(self.direccionFile_Alumnos,"r") as file:
            dataJson = json.load(file)

            if persona.nombre in dataJson["Alumnos"].keys():
                del dataJson["Alumnos"][persona.nombre]

        with open(self.direccionFile_Alumnos, "w") as file:
            json.dump(dataJson, file, indent=4)

    def addProfesor(self, profesor):

        dataJson = {}

        with open(self.direccionFile_Profes,"r") as file:
            dataJson = json.load(file)

            if profesor.nombre not in dataJson["Docentes"].keys():
                dataJson["Docentes"][profesor.nombre] = profesor.json

        with open(self.direccionFile_Profes, "w") as file:
            json.dump(dataJson, file, indent=4)

    def removeDocente(self, profesor):

        dataJson = {}

        with open(self.direccionFile_Profes,"r") as file:
            dataJson = json.load(file)

            if profesor.nombre in dataJson["Docentes"].keys():
                del dataJson["Docentes"][profesor.nombre]

        with open(self.direccionFile_Profes, "w") as file:
            json.dump(dataJson, file, indent=4)


class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def limpiarPantalla(self):
        def clear():
                #return os.system('cls')
            return os.system('clear')
        clear()              



    
##################     MAIN                   ################################


menu_main = Menu("Registro", {"Alumno":"1","Docente":"2","Salir":"0"})
menu_alumno = Menu("Alumno", {"Agregar Alumno":"1","Remover Alumno":"2"})
menu_profesor = Menu("Docente", {"Agregar Docente":"1","Remover Docente":"2"})

jsonMANANGER = JsonManager()

a = 'p'
while a != 0:
        menu_main.limpiarPantalla()
        print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " + menu_main.nombreMenu.upper()+"::::::::::::::::::::"+color.END)  
        print("\n")
        for (key, value) in menu_main.listaOpciones.items():
            print(key+color.GREEN+" → "+color.END+value)
            print("\n")

        a = int(input("Elija una opcion "))

        if(a == 1):
            menu_alumno.limpiarPantalla()
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " + menu_alumno.nombreMenu.upper()+"::::::::::::::::::::"+color.END)    
            for (key, value) in menu_alumno.listaOpciones.items():
                print(key+color.GREEN+" → "+color.END+value)
                print("\n")
            a = int(input("Elija una opcion "))

            if(a == 1):
                nombre_ = input("Ingrese nombre del alumno ")
                edad = input("Ingrese edad del alumno ")
                dni = input("Ingrese dni del alumno ")
                notas_ = []
                for nota in range(0,4):
                    notas_.append(int(input(f"Ingrese la nota del alumno ")))

                alumno_tmp = Alumno(nombre_, edad, dni, notas_)
                jsonMANANGER.addAlumno(alumno_tmp)

            elif(a == 2):
                nombre_ = input("Ingrese nombre del alumno ")
                alumno_tmp = Alumno(nombre_, edad, dni, notas_)
                jsonMANANGER.removeAlumno(alumno_tmp)

        if(a == 2):
            menu_alumno.limpiarPantalla()
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " + menu_profesor.nombreMenu.upper()+"::::::::::::::::::::"+color.END)    
            for (key, value) in menu_profesor.listaOpciones.items():
                print(key+color.GREEN+" → "+color.END+value)
                print("\n")
            a = int(input("Elija una opcion "))

            if(a == 1):
                nombre_ = input("Ingrese nombre del docente ")
                edad = input("Ingrese edad del edad ")
                dni = input("Ingrese dni del dni ")
                notas_ = []

                profesor_tmp = Profesor(nombre_, edad, dni)
                jsonMANANGER.addProfesor(profesor_tmp)

            elif(a == 2):
                nombre_ = input("Ingrese nombre del docente ")
                profesor_tmp = Profesor(nombre_, edad, dni)
                jsonMANANGER.removeDocente(profesor_tmp)
