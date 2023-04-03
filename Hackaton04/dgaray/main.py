


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
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def notaMaxima(self):
        return max(self.notas)

    def notaMinima(self):
        return min(self.notas)
    
class Docente(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)


def registrarAlumno():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    alumno = Alumno(nombre, dni, edad)
    for i in range(4):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        alumno.agregarNota(nota)
    promedio = alumno.promedio()
    notaMaxima = alumno.notaMaxima()
    notaMinima = alumno.notaMinima()
    with open("alumnos.txt", "a") as file:
        file.write(f"Alumno: {nombre}, maxima nota: {notaMaxima}, minima nota: {notaMinima}, promedio: {promedio}\n")

def registrarDocente():
    nombre = input("Ingrese el nombre del docente: ")
    dni = input("Ingrese el DNI del docente: ")
    edad = input("Ingrese la edad del docente: ")
    docente = Docente(nombre, dni, edad)
    with open("docentes.txt", "a") as file:
        file.write(f"Docente: {nombre}, Edad: {edad}, DNI: {dni}\n")

opcion = ""
while opcion != "3":
    print("MENU\n1. Registrar Alumno\n2. Registrar Docente\n3. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        registrarAlumno()
    elif opcion == "2":
        registrarDocente()