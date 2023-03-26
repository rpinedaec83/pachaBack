# nombres = "Herless Grimaldo"
# apellidos = "Acuña Zavala"
# edad = 40
# email = "herlessacuna@gmail.com"
# telefono = "969080671"

# distanciaEnMetros = 333
# distanciaEnMilimetros = 33333333.9999999

# direccion = 'Teodoro Cardenas 456'
# direccionAlterna = "Av Mexico"
# direccionCompuesta = '''Mi primera linea
# mi segunda linea
# mi tercera linea'''

# direccionSecundaria = "hdknd"

# print(direccion[0:7])
# print(direccion)

# fecha='2023-03-21'
# print("Year: "+fecha[0:4])
# print("Month: "+fecha[5:7])
# print("Day: "+fecha[8:10])

# casado = False
# feliz = True

# print(str(10/2))
# print(str(10//2))

# A = 8
# B = 5

# print(str(A + B))
# print(str(A - B))
# print(str(A * B))
# print(str(A / B))
# print(str(A ** B))

# print(str(A == B))
# print(str(A != B))
# print(str(A < B))
# print(str(A > B))
# print(str(A >= B))
# print(str(A <= B))

# print(str(A > B) and (B<0))
# print(str(A == B) and (A>0))
# print(str(A and B))
# print(str(A or B))
# print(str(A > B) or (B<0))

# vuelta = 1
# while vuelta < 100:
#     print("Vuelta: "+str(vuelta))
#     vuelta = vuelta + 1

# for vuelta in range(1,10,2):
#     print("Vuelta:" +str(vuelta))

# # for vuelta in range(1,10):
# #     print("Vuelta:" +str(vuelta))

# for vuelta in range(100,1,-5):
#   print("Vuelta:" +str(vuelta))

#Listas
# numeros = [1,2,3,4,5,6,7]
# palabras = ["Hola", "como", 'estas']
# combinada = [True, False, 0.0001, 23, 'Palabra']

personas = ['Juan', 'Juan Carlos', 4, 5, 6]
personas.append('Dexter')
print(personas.index('Juan Carlos'))
print(personas.index(5))
personas.remove('Juan Carlos')
print(personas)

miTupla = (1,2,3,4,5,6,7,8,9)
miSegundaTupla = (5,10,15,20)
miTerceraTupla = tuple(range(0,10))

print(miTupla)
print(miSegundaTupla)

miDic = {
    "Nombre":"Herless",
    "Apellido": "Acuña",
    "Edad": 40,
    "Mascotas":["swift","lentes"]
}
print(miDic)

print(type(miDic))
print(type(personas))
print(type(miSegundaTupla))

