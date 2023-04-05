class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Docente(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)

    def registrar_docente(self):
        with open("docentes.txt", "a") as archivo:
            archivo.write(f"Nombre: {self.nombre},DNI: {self.dni},Edad: {self.edad}\n")
            
class Alumno(Persona):
    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)
        self.notas = []

    def agregar_nota(self, nota):
        if len(self.notas) < 4:
            self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def maxima_nota(self):
        return max(self.notas)
    
    def minima_nota(self):
        return min(self.notas)

    def registrar_alumno(self):
        with open("alumnos.txt", "a") as archivo:
            archivo.write(f"\n")
            archivo.write(f"Nombres: {self.nombre}, DNI: {self.dni},Edad: {self.edad},\n")
            archivo.write(f"Notas: {','.join(str(nota) for nota in self.notas)}\n")
            archivo.write(f"Maxima nota: {self.maxima_nota()}, Minina nota: {self.minima_nota()}, Promedio: {self.promedio()}\n")

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Registrar un docente")
        print("2. Registrar un alumno")
        print("3. Salir")
        opcion = input("> ")

        if opcion == "1":
            nombre = input("Nombre del docente: ")
            dni = input("DNI del docente: ")
            edad = int(input("Edad del docente: "))
            docente = Docente(nombre, dni, edad)
            docente.registrar_docente()
            print("Docente registrado con éxito.")
            
        elif opcion == "2":
            nombre = input("Nombre del alumno: ")
            dni = input("DNI del alumno: ")
            edad = int(input("Edad del alumno: "))
            alumno = Alumno(nombre, dni, edad)
            for i in range(4):
                nota = float(input(f"Nota {i+1}: "))
                alumno.agregar_nota(nota)
            alumno.registrar_alumno()
            print("Alumno registrado con éxito.")

        elif opcion == "3":
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()