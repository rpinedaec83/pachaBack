import os
import shutil
directorio_actual = os.getcwd()
print(directorio_actual)

os.makedirs("MiPrimeraCarpeta")
'''os.removedirs("MiPrimeraCapeta")'''

listaDirectorios = os.listdir('../..')
print(listaDirectorios)

archivoOrigen = 'main.py'
directorioDestion = f'{directorio_actual}/MiPrimeraCarpeta'
shutil.copy(archivoOrigen,directorioDestion)