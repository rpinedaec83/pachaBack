nombres = "Fabrizio"
apellidos = "Chipana Mariano"
edad = 22
email = "fabrizio.chipanamariano2000@hotmail.com"
telefono = "963852741"

distancia_en_metros = 333
distancia_en_milimetros = 33333333.999999

direccion = 'Direccion 01'
direccion_alterna = "Direccion 02"
direccion_compuesta = '''Mi primera linea
Mi segunda linea
Mi tercera linea'''

direccion_secundaria = "Direccion 03"

print(direccion)
print(direccion[0:9])

fecha = '2023-03-21'
print("Year: {} ".format(fecha[0:4]))

A = 8
B = 5

print(str(A+B))
print(str(A-B))
print(str(A*B))
print(str(A/B))
print(str(A**B))

print(str(A==B))
print(str(A!=B))
print(str(A<B))
print(str(A>B))
print(str(A<=B))
print(str(A>=B))

print(str(A>B) and (B<0))
print(str(A==B) and (A>0))
print(str(A and B))
print(str(A>B) and (B<0))

vuelta = 1
while vuelta < 10:
    print("Vuelta: {}".format(vuelta))
    vuelta = vuelta + 1 


for vuelta in range(1,10):
    print("Vuelta: " + str(vuelta))

for vuelta in range(1,10,2):
    print("Vuelta: " + str(vuelta))

for vuelta in range(100,1,-5):
    print("Vuelta: " + str(vuelta))

#LISTAS

numeros = [1,2,3,4,5,6,7]
palabras = ["Hola","como",'estas']
combinada = [True,False,0.0001,23,'Palabra']

print(str(len(numeros)))
print(str(numeros[5]))
#Agregar elemento a lista
numeros.append(8)
print(str(len(numeros)))
print(numeros)
#Eliminar elemento a lista
numeros.remove(5)
print(numeros)
#Eliminar ultimo elemento de la lista
numeros.pop()
print(numeros)
#Añadir una lista a otra
numeros.extend(palabras)
print(numeros)
numeros.extend(combinada)
print(numeros)


personas = ["Juan", "Carlos", 4,5,6]
personas.append("Dexter")
print(personas.index("Juan"))
print(personas.index(5))
personas.remove("Carlos")
print(personas)


#TUPLAS

miTupla = (1,2,3,4,5,6,7,8,9,0)
miSegundaTupla = tuple(range(0,10))

print(miTupla)
print(miSegundaTupla)

#DICCIONARIO

miDic = {
    "Nombre":"Fabrizio",
    "Apellido":"Chipana",
    "Edad":22,
    "Mascotas":["Perro_1","Perro_2"]
}

print(miDic)

print(miDic["Mascotas"])
print(miDic["Nombre"])

print(type(miDic))
print(type(miTupla))
print(type(personas))

print(type(miDic["Edad"]))