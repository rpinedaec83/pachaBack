from archivo_personas import Persona

class Docente(Persona):
    def guardar_datos(self):
        with open("docentes.txt", "a") as archivo:
            archivo.write(f"{self.nombre},{self.dni},{self.edad}\n")

