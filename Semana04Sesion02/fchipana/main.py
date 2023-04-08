import os
import shutil

## Obtener directorio actual
# directorioActual = os.getcwd()
# print(directorioActual)

## Crear Carpetas especifica en directorio actual
# os.makedirs("MiPrimeraCarpeta")

## Eliminar Carpetas especifica en directorio actual
# os.removedirs("MiPrimeraCarpeta")

## Obtener directorio actual
# listaDirectorios = os.listdir('../..')
# listaDirectorios = os.listdir('.')
# print(listaDirectorios)

### Crear una copia de un archivo especifico en una carpeta especifica

# directorioActual = os.getcwd()
# os.makedirs("MiPrimeraCarpeta")
# listaDirectorios = os.listdir('../..')
# archivoOrigen = 'main.py'
# directorioDestino = f"{directorioActual}/MiPrimeraCarpeta"
# shutil.copy(archivoOrigen,directorioDestino)

# print(listaDirectorios)


##Leer contenido de libro de un paso
# try:
#     archivo = open("data.txt","r")
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

##Leer contenido de un libro paso por paso (linea por linea)

# try:
#     archivo = open("data.txt","r")
#     for linea in archivo.readlines():
#         # if (linea == "David"):
#         #     print("Este es el Alterego")
#         print(linea)
# except Exception as ex:
#     print(ex)


### Sobreescribir y leer archivo plano

##Crear y Sobreescribir archivo plano

# try:
#     archivo = open("nombres.txt","w")
#     archivo.write("Davis")
# except Exception as ex:
#     print(ex)

##Leer archivo plano

# try:
#     archivo = open("nombres.txt","r")
#     print(archivo.read())
# except Exception as ex:
#     print(ex)

### Agregar Registros y leer archivo plano
## Agregar registros al archivo plano

# try:
#     archivo = open("nombres.txt","a")
#     archivo.write("Pineda")
#     archivo.write("\n")
# except Exception as ex:
#     print(ex)

##Leer archivo plano
# try:
#     archivo = open("nombres.txt","r")
#     print(archivo.read())
# except Exception as ex:
#     print(ex)


class Persona:
    def __init__(self,nombre,apellido,edad,sexo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

class Archivo:
    def __init__(self, nombreArchivo) -> None:
        self.nombreArchivo = nombreArchivo

    def mostrarArchivo(self):
        try:
            file = open(self.nombreArchivo,"r")
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        else:
            file.close()


    def agregarPersonas(self,persona):
        try:
            file = open(self.nombreArchivo,"a")
            texto_agregar = f"{persona.nombre},{persona.apellido},{persona.edad},{persona.sexo} \n"
            file.write(texto_agregar)
        except Exception as ex:
            print(ex)
        else:
            file.close

persona = Persona('Roberto','Pineda',30,'Masculino')
archivo = Archivo("miPersona.txt")
archivo.agregarPersonas(persona)
archivo.mostrarArchivo()




