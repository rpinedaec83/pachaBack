import os
ruta_actual = os.getcwd()
alumno_txt = "Alumnos.txt"
profesores_txt = "Profesores.txt"

ruta_archivo_alumno = os.path.join(ruta_actual, alumno_txt)
ruta_archivo_profesor = os.path.join(ruta_actual, profesores_txt)


class Persona:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento


class Profesor(Persona):
    def __init__(self, nombre, apellido, documento, materia):
        super().__init__(nombre, apellido, documento)
        self.materia = materia

    def toDict(self):
        diccionario = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Documento": self.documento,
            "Materia": self.materia,
        }
        return diccionario


class Alumno(Persona):
    def __init__(self, nombre, apellido, documento, nota1=0, nota2=0, nota3=0, nota4=0):
        super().__init__(nombre, apellido, documento)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def numMayor(self):
        mayorNota = max([self.nota1, self.nota2, self.nota3, self.nota4])
        return mayorNota

    def numMenor(self):
        menorNota = min([self.nota1, self.nota2, self.nota3, self.nota4])
        return menorNota

    def promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        return promedio

    def toDict(self):
        self.numMayor()
        self.promedio()
        self.numMenor()

        diccionario = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Documento": self.documento,
            "Nota Mayor": self.numMayor(),
            "Nota Menor": self.numMenor(),
            "Nota Promedio": self.promedio(),
        }
        return diccionario


def ProgramaDeRegistro():
    while True:
        print(
            "*" * 55,
            "\n",
            "Bienvenido, escoge una opcion o presiona 0 para salir",
            "\n",
            "*" * 55,
        )
        print(
            """
                1.- Registrar Alumno
                2.- Registrar Profesor
                ************************
                presiona 0 para salir
            """
        )

        opcion = int(input("Escoge un opcion valida: "))

        if opcion == 1:
            nombre = input("Ingresa el NOMBRE del alumno: ")
            apellido = input("Ingresa el APELLIDO del alumno: ")
            documento = input("Ingresa el DOCUMENTO del alumno: ")
            nota1 = int(input("Ingresa LA NOTA 1 del alumno: "))
            nota2 = int(input("Ingresa LA NOTA 2 del alumno: "))
            nota3 = int(input("Ingresa LA NOTA 3 del alumno: "))
            nota4 = int(input("Ingresa el LA NOTA 4 del alumno: "))

            AlumnoRegistrado = Alumno(
                nombre, apellido, documento, nota1, nota2, nota3, nota4
            )

            with open(ruta_archivo_alumno, "a") as archivo:
                texto = str(AlumnoRegistrado.toDict()) + "\n"
                archivo.write(texto)
                break

        if opcion == 2:
            nombre = input("Ingresa el NOMBRE del profesor: ")
            apellido = input("Ingresa el APELLIDO del profesor: ")
            documento = input("Ingresa el DOCUMENTO del profesor: ")
            materia = input("Ingresa la MATERIA del profesor: ")

            ProfesorRegistrado = Profesor(nombre, apellido, documento, materia)

            with open(ruta_archivo_profesor, "a") as archivo:
                texto = str(ProfesorRegistrado.toDict()) + "\n"
                archivo.write(texto)
                break

        if opcion == 0:
            break


if __name__ == "__main__":
    ProgramaDeRegistro()
