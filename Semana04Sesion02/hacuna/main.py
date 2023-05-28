import os
import shutil

# #Manejo de Carpetas
# directorioActual = os.getcwd()
# print(directorioActual)

# os.makedirs("MiPrimeraCarpeta") #Crea carpeta
# os.removedirs("MiPrimeraCarpeta") #Remueve la carpeta

# listaDirectorios = os.listdir('.')
# print(listaDirectorios) #Ver lista de directorios

# listaDirectorios = os.listdir('..')
# print(listaDirectorios)     #El nivel anterior de trabajo

# listaDirectorios = os.listdir('../..')
# print(listaDirectorios)     #Lista un array de todas las cosas que uno tiene en la carpeta Pachaback-1

# listaDirectorios = os.listdir('../..')
# listaDirectorios = os.listdir('.')

# archivoOrigen = 'main.py'
# directorioDestino = f"{directorioActual}/MiPrimeraCarpeta"
# shutil.copy(archivoOrigen, directorioDestino)
# print(listaDirectorios)         #Copiar un archivo en una carpeta creada en linea 7


# #Manejo de archivos
# try:
#     archivo = open("data.txt", 'r')
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("data.txt", 'r')
#     for linea in archivo.readlines():
#         print(linea)
#     print(archivo.read())
# except Exception as ex:
#     print(ex)       #Escribe lo que esta en data.txt linea por linea


# try:
#     archivo = open("nombres.txt", 'w')
#     archivo.write("Acuña")
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("nombres.txt", 'a')
#     archivo.write("Zavala")
#     archivo.write("\n")
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("nombres.txt", 'r')
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

class Persona:
    def __init__(self, nombre, apellido, edad, sexo): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    def mostrarArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        else:
            file.close()

    def agregarPersona(self, persona):
        try:
            file = open(self.nombreArchivo, 'a')
            text_agregar = f"{persona.nombre}, {persona.apellido}, {persona.edad}, {persona.sexo} \n"
            file.write(text_agregar)
        except Exception as ex:
            print(ex)
        else:
            file.close()
            #print(file)            

persona = Persona('Herless', 'Acuña', 40, 'Masculino' )
archivo = Archivo("miPersona.txt")
archivo.agregarPersona(persona)
archivo.mostrarArchivo()