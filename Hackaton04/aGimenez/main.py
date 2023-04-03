import os

class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Docente(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)
    
    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} DNI: {self.dni}"

    def grabarDocente(self):
        with open("docentes.txt", "a") as file:
            file.write(f"{self.nombre}, {self.edad}, {self.dni}\n")

class Alumno(Persona):
    def __init__(self, nombre, dni, edad, notas):
        super().__init__(nombre, dni, edad)
        self.notas = notas
        self.promedio = sum(self.notas) / len(self.notas)

    def grabarAlumno(self):
        with open("alumnos.txt", "a") as file:
            file.write(f"{self.nombre}, {self.edad}, {self.dni}, {self.notas}, {self.promedio}\n")


def menuPrincipal():
    print("----------BIENVENIDO AL MENU----------")
    print("-----------ELIJA UNA OPCION-----------")
    print("1. Docentes")
    print("2. Alumnos")
    print("3. Salir")

def menuDocente():
    print("---MENU DOCENTES---")
    print("--Elija una opcion--")
    print("1. Registrar Docente")
    print("2. Mostrar Docente")
    print("3. Reporte Docentes")
    print("4. Volver al Menu Anterior")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        limpiarPantalla()
        ingresarDocente()
    elif opcion == 2:
        limpiarPantalla()
        mostrarDocentes()
    elif opcion == 3: 
        limpiarPantalla()
        reporteDocentes()
    elif opcion == 4:
        limpiarPantalla()
        menuPrincipal()
    else:
        print("No es correcta la opcion")
    apretarTecla()
            

def menuAlumno():
    print("---MENU ALUMNOS---")
    print("--Elija una opcion--")
    print("1. Registrar Alumno")
    print("2. Mostrar Alumnos")
    print("3. Reporte Alumnos")
    print("4. Volver al Menu Anterior")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        limpiarPantalla()
        ingresarAlumno()
    elif opcion == 2:
        limpiarPantalla()
        mostrarAlumnos()
    elif opcion == 3: 
        limpiarPantalla()
        reporteAlumnos()
    elif opcion == 4:
        limpiarPantalla()
        menuPrincipal()
    else:
        print("No es correcta la opcion")
    apretarTecla()
            

def ingresarDocente():
    while True:
        try:
            print("Registro de Docentes: ")
            nombre = input("Nombre del Docente: ")
            edad = input("Edad del Docente: ")
            dni = input("Dni del Docente: ")
            break
        except ValueError:
            print("Hubo un ingreso erroneo de datos")
            limpiarPantalla()
    docente = Docente(nombre, dni, edad)
    docente.grabarDocente()
    print("Docente ingresado correctamente")

def ingresarAlumno():
    while True:
        try:
            print("Registro de Alumnos: ")
            nombre = input("Nombre del Alumno: ")
            edad = input("Edad del Alumno: ")
            dni = input("Dni del Alumno: ")
            notas = []
            while True:
                try:
                    for i in range(4):
                        nota = float(input(f"Ingrese nota {i+1} "))
                        if nota < 0 or nota > 20:
                            raise ValueError()
                        notas.append(nota)
                    break
                except ValueError:
                    print("Hubo un ingreso erroneo de datos")
                    limpiarPantalla()
            break
        except ValueError:
            print("Hubo un ingreso erroneo de datos")
    alumno = Alumno(nombre, dni, edad, notas)
    alumno.grabarAlumno()
    print("Alumno ingresado correctamente")

def mostrarDocentes():
    print("---Estos son los docentes---")
    with open("docentes.txt", "r") as file:
        for line in file:
            print(line, end=" ")

def mostrarAlumnos():
    print("---Estos son los Alumnos---")
    with open("alumnos.txt", "r") as file:
        for line in file:
            print(line, end=" ")

def reporteDocentes():
    print("---Reporte de los Docentes---")
    listaDocentes = []
    with open("docentes.txt", "r") as file:
        for line in file:
            datos = line.split(", ")
            datos[-1] = datos[-1].replace("\n", " ")
            listaDocentes.append(datos)
    for docente in listaDocentes:
        with open("reporteDocente.txt", "a") as file:
            file.write(f"Docente: {docente[0]}. Edad: {docente[1]}. Dni: {docente[2]}")
    print("Archivo Creado Correctamente!!")

def reporteAlumnos():
    print("---Reporte de los Alumnos---")
    listaAlumnos = []
    with open("alumnos.txt", "r") as file:
        for line in file:
            datos = line.split(", ")
            datos[-1] = datos[-1].replace("\n", " ")
            listaAlumnos.append(datos)
    for alumno in listaAlumnos:
        alumno[-2] = alumno[-2].replace("[", " ")
        alumno[-2] = alumno[-2].replace("]", " ")
        alumno[-2] = alumno[-2].split(", ")
        with open("reporteAlumnos.txt", "a") as file:
            file.write(f"Alumno: {alumno[0]}. Nota Maxima: {alumno[-2][0]}. Nota Minima: {alumno[-2][-1]} Promedio: {alumno[-1]}\n")
    print("Archivo Creado Correctamente!!")

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def apretarTecla():
    input("Presione una tecla para continuar..")
    limpiarPantalla()

def main():
    while True:
        menuPrincipal()
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 1:
            limpiarPantalla()
            menuDocente()
        elif opcion == 2:
            limpiarPantalla()
            menuAlumno()
        elif opcion == 3:
            limpiarPantalla()
            break
        else:
            limpiarPantalla()
            print("No es correcta la opcion")
            apretarTecla()
            
main()