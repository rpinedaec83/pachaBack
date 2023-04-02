class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

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

class Docente(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)

def registrar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    alumno = Alumno(nombre, dni, edad)
    for i in range(4):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        alumno.agregar_nota(nota)
    promedio = alumno.promedio()
    nota_maxima = alumno.nota_maxima()
    nota_minima = alumno.nota_minima()
    with open("alumnos.txt", "a") as file:
        file.write(f"Alumno: {nombre}, maxima nota: {nota_maxima}, minima nota: {nota_minima}, promedio: {promedio}\n")

def registrar_docente():
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
        registrar_alumno()
    elif opcion == "2":
        registrar_docente()