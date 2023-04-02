from archivo_personas import Persona


class Alumno(Persona):
    def __init__(self, nombre, dni, edad, notas):
        super().__init__(nombre, dni, edad)
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def obtener_nota_maxima(self):
        return max(self.notas)

    def guardar_datos(self):
        with open("alumnos.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.dni},{self.edad}")
            for nota in self.notas:
                archivo.write(f",{nota}")
            archivo.write("\n")

    def registrar_datos(self):
        notas = []
        for i in range(4):
            nota = int(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        self.notas = notas
