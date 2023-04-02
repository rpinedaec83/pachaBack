import os
import shutil


#  INI Manejo de Carpetas
# directorioActual = os.getcwd()
# print(directorioActual)

# os.makedirs("MiPrimeraCarpeta")
#os.removedirs("MiPrimeraCarpeta")

# listaDirectorios = os.listdir('../..')

# archivoOrigen = 'main.py'
# directorioDestino = f"{directorioActual}/MiPrimeraCarpeta"
# shutil.copy(archivoOrigen,directorioDestino)

# print(listaDirectorios)
# #FIN

# # INI Manejo de Archivos
# try:
#     archivo = open("data.txt",'r')
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("data.txt",'r')
#     for linea in archivo.readlines():
#         # if(linea == 'David'):
#         #     print("Este es el Alterego")
#         print(linea)
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("nombres.txt",'w')
#     archivo.write("Lopez")
# except Exception as ex:
#     print(ex)


# try:
#     archivo = open("nombres.txt",'r')
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("nombres.txt",'a')
#     archivo.write("Pineda")
#     archivo.write("\n")
# except Exception as ex:
#     print(ex)

# try:
#     archivo = open("nombres.txt",'r')
#     print(archivo.read())
# except Exception as ex:
#     print(ex)
# # FIN

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
            # print(file)

persona = Persona('Roberto','Pineda',39,'Masculino')
archivo = Archivo("miPersona.txt")
archivo.agregarPersona(persona)
archivo.mostrarArchivo()

