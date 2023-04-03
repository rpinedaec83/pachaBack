class Persona: 
    def __init__(self,nombre, apellido, edad, sexo ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

class Archivo: 
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def MostrarArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        else:
            file.close()

    def AgregarPersona(self, persona):
        try:
            file = open(self.nombreArchivo,'a')
            text_agregar = f"{persona.nombre}, {persona.edad}, {persona.sexo} \n"
            file.write(text_agregar)
        except Exception as ex:
            print(ex)
        else:
            file.close()


persona = Persona('Cesar', 'Beltran', 24,'Masculino')
archivo = Archivo("MiPersona.txt")

archivo.AgregarPersona(persona)
archivo.MostrarArchivo()