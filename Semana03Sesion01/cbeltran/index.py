nombre = "Cesar"
apellido = "Beltran"
edad = 24
email = "cbeltran.dev@outlook.com"
telefono = "982344766"

distanciaMetros = 333
distanciaMilimetros = 333.333

direccion = 'Jiron Echenique 920'

print (direccion[6:15])

fecha = '2023-03-21'
print("Year: " +fecha[0:4])
print("Mont: "+ fecha[5:7])
print("Day: " + fecha[8:10])

casado = False;
feliz = True;

print (str(10/2))#Resultado con decimales
print (str(10//2))#Resultado sin decimales
print (str(10%2))#Obtiene el residuo

A = 8
B = 5 

#Operadores lógicos
print (str(A + B))
print (str(A - B))
print (str(A * B))
print (str(A / B))
print (str(A ** B))

#Operadores de comparación
print (str(A == B))
print (str(A != B))
print (str(A < B))
print (str(A > B))
print (str(A <= B))
print (str(A >= B))


print (str(A < B) and (B<0))
print (str(A == B) and (A>0))
print (str(A and B))
print (str(A or B))

#Bucles o iteradores

vuelta = 1 
while vuelta > 10:
    print ("vuelta: " + str(vuelta))
    vuelta = vuelta + 1

for vuelta in range (1,10,2):
    print ( "Vuelta:" + str(vuelta)) 

#LISTAS 

numeros =  [1,2,3,4,5,6,7]
palabras = ["Hola","cómo","estás"]
listaCombinada = [True,False,0.001,23,"Palabra"]

print (str(len(numeros)))
print (str(numeros[5]))
numeros.append(8)
print (str(len(numeros)))
print (numeros)
numeros.remove(5)
print (numeros)
numeros.pop()
print (numeros)
numeros.extend(palabras)
print (numeros)
numeros.extend(listaCombinada)
print (numeros)

personas = ["Jorge", "Juan", "Carlos", 4, 5, 6]
personas.append("Dexter")
print (personas.index("Juan"))
print (personas.index(5))
personas.remove("Carlos")

tupla = (0,1,2,3,4,5,6,7,8,9)
tupla2 = tuple(range(0,10))
print (tupla)
print (tupla2)
tupla.index(5)

diccionario = {
    "Nombre" : "Cesar",
    "Apellido" : "Beltran",
    "Edad" : 24,
    "Mascotas" : ["Juanito", "Teodoro"]
}
print (diccionario)
print (diccionario["Mascotas"])

print (type(diccionario))
print (type(tupla))
print (type(personas))



