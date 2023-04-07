import os
import time
import utils
import json


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


# ----------------------------------------------------------------------------------


class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


class Alumno(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def nota_maxima(self):
        return max(self.notas)

    def nota_minima(self):
        return min(self.notas)

    def toDic(self):
        d = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "id": self.edad,
            "codigoCliente": self.codigoCliente,
        }
        return d


class Docente(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)


class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system("clear")

        clear()

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("\n")
            print(
                color.BLUE
                + "::::::::::::::::::::"
                + "ESTE ES EL MENU DE "
                + self.nombreMenu.upper()
                + "::::::::::::::::::::"
                + color.END
            )
            print("\n")
            for key, value in self.listaOpciones.items():
                print(key + color.GREEN + " → " + color.END + value)
            print("\n")
            ans = input(color.YELLOW + "Por favor, ingrese su opción: " + color.END)
            print("\n")
            if ans.upper() == "0":
                print("Hasta, pronto")
                break
            b = 0
            for key, value in self.listaOpciones.items():
                if value == ans:
                    b = b + 1
            if b > 0:
                a = False
            else:
                print(
                    color.RED + "Opción no valida, escoja una opción valida" + color.END
                )
                time.sleep(3)
        return ans


Home_options = {"Alumnos": "1", "Docentes": "2", "Exit": "0"}
Main_menu = Menu("home", Home_options)

Alumno_options = {
    "Agregar alumnos": "1",
    "Lista de alumnos": "2",
    "Remover alumno": "3",
    "Exit": "0",
}
Menu_alumno = Menu("cliente", Alumno_options)

Teacher_options = {
    "Agregar docente": "1",
    "Lista de docentes": "2",
    "Remover docente": "3",
    "Exit": "0",
}
Menu_Teacher = Menu("inventario", Teacher_options)

student_list = []
teacher_list = []
student_listDic = []

fileStudent = utils.fileManager("alumnos.txt")


def cargainicial():
    res = fileStudent.leerArchivo()
    print(res)
    if (res != ""):
        listTempStudent = json.loads(res)
        for dic in listTempStudent:
            newStudent = Alumno(
                dic["nombre"], dic["dni"], dic["edad"]
            )
            student_listDic.append(newStudent.toDic())
            student_list.append(newStudent)


cargainicial()

f = True
while f:
    ans = Main_menu.show()
    print(ans)
    if ans.upper() == "1":
        ans = Menu_alumno.show()
        if ans.upper() == "1":
            print("Ingrese la información del alumno:")
            nombre = input("Nombre del alumno     : ")
            dni = input("Apellido del alumno: ")
            edad = input("Edad del alumno:")
            alumno = Alumno(nombre, dni, edad)
            for i in range(4):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                alumno.agregar_nota(nota)
            promedio = alumno.promedio()
            nota_maxima = alumno.nota_maxima()
            nota_minima = alumno.nota_minima()
            print("")
            o = True
            while o:
                print(
                    f"Esta seguro que desea agregar al alumno {nombre} a lista de clientes? (Y/N)"
                )
                ans = input(color.YELLOW + "Answer: " + color.END)
                if ans.upper() == "Y":
                    student_n = Alumno(nombre, dni, edad, alumno.promedio, alumno.nota_maxima, alumno.nota_minima)
                    student_list.append(student_n)
                    print("")
                    print(color.GREEN + f"{nombre} fue agregado ☑" + color.END)
                    student_listDic.append(student_n.toDic())
                    jsonString = json.dumps(student_listDic)
                    fileStudent.borrarArchivo()

                    fileStudent.escribirArchivo(jsonString)
                    break
                elif ans.upper() == "N":
                    print("")
                    break
                else:
                    print("")
                    print(
                        color.RED
                        + "Opción no valida, escoja una opción valida"
                        + color.END
                    )
                    print("")
        elif ans.upper() == "2":
            print(color.GREEN + "Esta es la lista de clientes ☑:" + color.END)
            for client in student_list:
                print(
                    f"|{client.nombre}|{client.apellido}|{client.edad}|{client.id}|{client.codigoCliente}|"
                )
            g = True
            while g:
                print("")
                print("Desea ir al menu o salir del programa? (M/0)")
                ans = input(color.YELLOW + "Answer: " + color.END)
                if ans.upper() == "M":
                    g = False
                    break
                elif ans.upper() == "0":
                    g = False
                    f = False
                    break
                else:
                    print("")
                    print(
                        color.RED
                        + "Opción no valida, escoja una opción valida"
                        + color.END
                    )
                    print("")

    elif ans == "2":
        ans = Menu_Teacher.show()
