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

    def promedio_notas(self):
        return sum(self.notas) / len(self.notas)

    def nota_maxima(self):
        return max(self.notas)

    def nota_minima(self):
        return min(self.notas)

    def reporte(self):
        maxima = self.nota_maxima()
        minima = self.nota_minima()
        promedio = self.promedio_notas()
        reporte = f"Alumno: {self.nombre}\nMáxima nota: {maxima}\nMínima nota: {minima}\nPromedio: {promedio}\n"
        return reporte

class Docente(Persona):
    def reporte(self):
        reporte = f"Docente: {self.nombre} \nEdad: {self.edad}\nDNI: {self.dni}"
        return reporte