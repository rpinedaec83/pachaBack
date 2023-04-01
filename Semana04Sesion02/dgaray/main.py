import os
import shutil

directorioActual = os.getcwd()
print(directorioActual)


# crear carpeta
os.makedirs("MiPrimeraCarpeta")
# remover carpeta
# os.removedirs('MiPrimeraCarpeta')

listaDirectorios = os.listdir('../..')

archivoOrigen = 'main'

print(listaDirectorios)