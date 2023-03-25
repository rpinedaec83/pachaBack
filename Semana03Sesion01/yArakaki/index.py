nombres = "Roberto David"
apellidos = "Pineda Lopez"
edad = 39
email = "rpineda@x-codec.net"
telefono = "916730940"

distancaEnMetros= 333
distanciaEnMilimetros = 33333333.9999999

direccion = 'Teodoro Cardenas 456'
direccionAlterna = "Va Mexico"
direccionCompuesta = '''Mi primera linea 
mi segunda linea
mi tercera linea'''

direccionSecundaria ="dsajkdh"

print(direccion)
print(direccion[0:7])


fecha='2023-03-21'
print("Year: "+fecha[0:4])
print("Month: "+ fecha[5:7])
print("Day: "+ fecha[8:10])

casado = False
feliz = True

print(str(10/2))
print(str(10//2))

A = 8
B = 5

print(str(A + B))
print(str(A - B))
print(str(A * B))
print(str(A / B))
print(str(A ** B))

print(str(A == B))
print(str(A != B))
print(str(A < B))
print(str(A > B))
print(str(A >= B))
print(str(A <= B))

print(str(A > B) and (B < 0))
print(str(A == B) and (A > 0))
print(str(A and B))
print(str(A > B) or (B < 0))

vuelta = 1
while vuelta < 100:
   print("Vuelta: "+ str(vuelta))
   vuelta = vuelta + 1

for vuelta in range(100,1,-5):
    print("Vuelta:" +str(vuelta))

#LISTAS

numeros = [1,2,3,4,5,6,7]
palabras = ["Hola", "como", 'estas']
combinada = [True,False,0.0001,23,'Palabra']

print(str(len(numeros)))
print(str(numeros[5]))
numeros.append(8)
print(str(len(numeros)))
print(numeros)
numeros.remove(5)
print(numeros)
numeros.pop()
print(numeros)
numeros.extend(palabras)
print(numeros)
numeros.extend(combinada)
print(numeros)
personas = ['Juan','Carlos',4,5,6]
personas.append('Dexter')
print(personas.index('Juan'))
print(personas.index(5))
personas.remove('Carlos')
print(personas)

miTupla = (1,2,3,4,5,6,7,8,9,0)
miSegundaTupla = tuple(range(0,10))

print(miTupla)
print(miSegundaTupla)

miDic = {
    "Nombre":"Roberto",
    "Apellido":"Pineda",
    "Edad":39,
    "Mascotas":["Selina","Pancho"]
}
print(miDic)

print(miDic["Mascotas"])
print(miDic["Nombre"])

print(type(miDic))
print(type(miTupla))
print(type(personas))

print(type(miDic['Edad']))