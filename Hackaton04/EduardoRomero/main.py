import os

class Persona:
    def __init__(self, nombre, apellido, edad, dni, sexo):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.correo = f"{self.nombre.lower()}.{self.apellido.lower()}@idat.edu.pe"
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido:{self.apellido} Edad: {self.edad} DNI: {self.dni} Sexo: {self.sexo} Correo: {self.correo}"
    
class Docente(Persona):
    def __init__(self, nombre, apellido, edad, dni, sexo, materia, cargo, sueldo):
        super().__init__(nombre, apellido, edad, dni, sexo,)
        self.materia = materia
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido:{self.apellido} Edad: {self.edad} DNI: {self.dni} Sexo: {self.sexo} Correo: {self.correo} Materia: {self.materia} Cargo: {self.cargo} Sueldo: {self.sueldo}"
    
    def exportar_docente(self):
        with open("docentes.txt", "a") as file:
            file.write(f"{self.nombre}-{self.apellido}-{self.edad}-{self.dni}-{self.sexo}-{self.correo}-{self.materia}-{self.cargo}-{self.sueldo}\n")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, dni, sexo, notas):
        super().__init__(nombre, apellido, edad, dni, sexo)
        self.notas = notas
        self.promedio = sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"{self.nombre}-{self.apellido}-{self.edad}-{self.dni}-{self.sexo}-{self.correo}-{self.notas}"

    def ordenarNotas(self):
        self.notas.sort()

    def exportar_estudiante(self):
        with open("estudiantes.txt", "a") as file:
            file.write(f"{self.nombre}-{self.apellido}-{self.edad}-{self.dni}-{self.sexo}-{self.correo}-{self.notas}-{self.promedio}\n")

def menu():
    print("Bievenido a la DATABASE de IDAT")
    print("1. Registrar Docente")
    print("2. Registrar Estudiante")
    print("3. Mostrar Docentes")
    print("4. Mostrar Estudiantes")
    print("5. Reporte Docentes")
    print("6. Reporte Estudiantes")
    print("7. Salir")

def registrarDocente():
    while True:
        try:
            print("REGISTRO DE DOCENTES")
            nombre = input("Ingrese el nombre del docente: ")
            apellido = input("Ingrese el apellido del docente: ")
            edad = int(input("Ingrese la edad del docente: "))
            dni = input("Ingrese el DNI del docente: ")
            sexo = input("Ingrese el sexo del docente: ")
            materia = input("Ingrese la materia del docente: ")
            cargo = input("Ingrese el cargo del docente: ")
            sueldo = float(input("Ingrese el sueldo del docente: "))
            break
        except ValueError:
            print("Ingrese correctamente los datos")
            limpiar_terminal()
    docente = Docente(nombre, apellido, edad, dni, sexo, materia, cargo, sueldo)
    docente.exportar_docente()
    print("Docente registrado correctamente")

def registrarEstudiante():
    while True:
        try:
            print("REGISTRO DE ESTUDIANTES")
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            dni = input("Ingrese el DNI del estudiante: ")
            sexo = input("Ingrese el sexo del estudiante: ")
            notas = []
            while True:
                try:
                    for i in range(4):
                        nota = float(input(f"Ingrese la nota E{i+1}: "))
                        if nota < 0 or nota > 20:
                            raise ValueError
                        notas.append(nota)
                    break
                except ValueError:
                    print("Ingrese correctamente las notas")
                    limpiar_terminal()
            break
        except ValueError:
            print("Ingrese correctamente los datos")
            limpiar_terminal()
    estudiante = Estudiante(nombre, apellido, edad, dni, sexo, notas)
    estudiante.ordenarNotas()
    estudiante.exportar_estudiante()
    print("Estudiante registrado correctamente")

def mostrarDocentes():
    print("LISTA DE DOCENTES")
    with open("docentes.txt", "r") as file:
        for line in file:
            print(line, end="")

def mostrarEstudiantes():
    print("LISTA DE ESTUDIANTES")
    with open("estudiantes.txt", "r") as file:
        for line in file:
            print(line, end="")
    
def reporteDocentes():
    print("REPORTE DE DOCENTES")
    listadocentes = []
    with open("docentes.txt", "r") as file:
        for line in file:
            datos = line.split("-")
            datos[-1] = datos[-1].replace("\n", "")
            listadocentes.append(datos)
    for docente in listadocentes:
        with open("reporte-docentes.txt", "a") as file:
            file.write(f"Docente: {docente[0]} {docente[1]} Edad: {docente[2]} DNI: {docente[3]}\n")
    print("El archivo se ha creado correctamente")

def reporteEstudiantes():
    print("REPORTE DE ESTUDIANTES")
    listaestudiantes = []
    with open("estudiantes.txt", "r") as file:
        for line in file:
            datos = line.split("-")
            datos[-1] = datos[-1].replace("\n", "")
            listaestudiantes.append(datos)
    for estudiante in listaestudiantes:
        estudiante[-2] = estudiante[-2].replace("[", "")
        estudiante[-2] = estudiante[-2].replace("]", "")
        estudiante[-2] = estudiante[-2].split(",")
        with open("reporte-estudiantes.txt", "a") as file:
            file.write(f"Alumno: {estudiante[0]} {estudiante[1]} Maxima nota: {estudiante[-2][0]} Minima nota: {estudiante[-2][-1]} Promedio: {estudiante[-1]}\n")
    print("El archivo se ha creado correctamente")

def limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def presionar_tecla():
    input("Presione una tecla para continuar...")
    limpiar_terminal()

def main():
    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            limpiar_terminal()
            registrarDocente()
        elif opcion == 2:
            limpiar_terminal()
            registrarEstudiante()
        elif opcion == 3:
            limpiar_terminal()
            mostrarDocentes()
        elif opcion == 4:
            limpiar_terminal()
            mostrarEstudiantes()
        elif opcion == 5:
            limpiar_terminal()
            reporteDocentes()
        elif opcion == 6:
            limpiar_terminal()
            reporteEstudiantes()
        elif opcion == 7:
            break
        else:
            print("Opción no válida")
        presionar_tecla()
        
if __name__ == "__main__":
    main()