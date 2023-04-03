import os
import shutil

'''directorio_actual = os.getcwd()
print(directorio_actual)'''

#Crear y remover carpetas
'''os.makedirs("MiPrimeraCarpeta")'''
'''os.removedirs("MiPrimeraCapeta")'''

#Mostrar uno o varios directorios mediante una array/lista
'''listaDirectorios = os.listdir('../..')
print(listaDirectorios)
listaDirectorios = os.listdir('.')
print(listaDirectorios)'''


#Copiar archivos a diferentes directorios con el método 'copy()' de la libreria 'shutil'
'''archivoOrigen = 'main.py'
directorioDestion = f'{directorio_actual}/MiPrimeraCarpeta'''
'''shutil.copy(archivoOrigen,directorioDestion)'''

#Lectura de archivos con 'read()'

try:
    archivo = open("data.txt",'r')
    print(archivo.read())
except Exception as ex:
    print(ex)

try:
    archivo = open("data.txt",'r')
    for linea in archivo.readline():
        print(linea)
        if (linea == "David"):
            print("Este es el Alterego")
except Exception as ex:
    print(ex)

#Escritura de archivos

try:
    archivo = open("nombres.txt",'w')
    archivo.write("Cesar")
    print(archivo.read())
except Exception as ex:
    print(ex)