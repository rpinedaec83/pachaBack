import os

class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Docente(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)

class Alumno(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)

class Archivos:
    def __init__(self, archivo):
        self.archivo = archivo

    def viewArchivo(self):
        try:
            file = open(self.archivo, 'r')
            for line in file.readlines():
                print(line)

        except Exception as e:
            print("Error: ", e)
        else:
            file.close()

    def addPersona(self, persona):
        try:
            file = open(self.archivo, 'a')
            # file.write(" NOMBRE      DNI   EDAD\n")
            text = f"{persona.nombre}        {persona.dni}    {persona.edad}\n"
            file.write(text)
        except Exception as e:
            print("Error", e)
        else:
            file.close()
            # print(file)

    def addNotas(self, alumn):
        try:
            file = open(self.archivo, 'a')
            # file.write(" NOMBRE      DNI   EDAD\n")
            text = f"{alumn.nombre}      {alumn.n_max}   {alumn.n_min}   {alumn.n_prom}\n"
            file.write(text)
        except Exception as e:
            print("Error", e)
        else:
            file.close()

class Notas:
    def __init__(self, nombre, n_max, n_min, n_prom):
        self.nombre = nombre
        self.n_max =n_max
        self.n_min =n_min
        self.n_prom =n_prom

print("""
    1) Registrar Alumnos
    2) Registar Docentes
    3) Registar Notas
    """)

opcion=int(input("Seleccione una opción: "))

if(opcion == 1 or opcion == 2):
    name = input("Ingrese Nombre: ")
    dni = input("Ingrese Dni: ")
    age = int(input("Ingrese Edad: "))

    if(opcion == 1):
        alumno = Alumno(name, dni, age)
        archivo = Archivos("alumnos.txt")
        archivo.addPersona(alumno)
        archivo.viewArchivo()
    else:
        docente = Docente(name, dni, age)
        archivo = Archivos("docentes.txt")
        archivo.addPersona(docente)
        archivo.viewArchivo()

elif(opcion == 3):
    name = input("Ingrese Nombre: ")
    notas = []
    for i in range(4):
        n = int(input(f"Ingrese Nota {i+1}: "))
        notas.append(n)

    alumno = Notas(name, max(notas), min(notas), sum(notas)/4)
    archivo = Archivos("notas.txt")
    archivo.addNotas(alumno)

else:
    print("Opción no válida")


# eliminar archivos
# os.remove("alumnos.txt")
# os.remove("docentes.txt")