# name = "Maritza"
# lastname = "Rodriguez"
# age = 25
# email = "maritzarg2020@gmail.com"
# phone = "999888777"

# distanceInMeters = 333
# distanceInMilimeters = 3333333.9999999

# # strings
# address = 'Lima 123'
# addressReference = "city park"
# addressCompuesta = ''' first line
# second line
# thirtd line'''

# secondaryAddress = "abc ancddddd"

# print(address)
# print(address[0:5])

# date = "2023-12-21"
# print("Year: " + date[0:4])
# print("Month: " + date[5:7])
# print("Day: " + date[8:10])

# # booleans
# married = False
# happy = True


# # sobre division
# print(str(10/2))  # division / (no es 100% exacta en la pc)
# print(str(10//2))  # division exacta //


# # str = string

# A = 8
# B = 5

# print(str(A + B))
# print(str(A - B))
# print(str(A * B))
# print(str(A / B))  # 1.6
# print(str(A // B))  # 1
# print(str(A % B))
# print(str(A ** B))


# # comparacion
# print("***Comparacion")
# print(str(A == B))
# print(str(A != B))
# print(str(A < B))
# print(str(A > B))
# print(str(A >= B))
# print(str(A <= B))


# # logicos
# print("***Logicos AND")
# print(str(True & True))
# print(str(True & False))
# print(str(False & True))
# print(str(False & False))

# print("***Logicos OR")
# print(str(True | True))
# print(str(True | False))
# print(str(False | True))
# print(str(False | False))

# print("*Testing Logicos")
# print(str(A > B) and (B < 0))
# print(str(A == B) and (A > 0))
# print(str(A and B))
# print(str((A > B) or (B > A)))


# # BUCLES O ITERADORES
# # while
# cicle = 1
# while cicle < 10:
#     print("Cicle: " + str(cicle))
#     cicle = cicle + 1

# # for
# for cicle in range(100, 10, -5):  # (a, b, pasos)
#     print("Cicle: " + str(cicle))

# LISTAS o arrays
# numbers = [1, 2, 3, 4, 5, 6, 7]
# words = ["Hi", "como", "estas"]
# combinated = [True, False, 0.001, 23, "Palabra"]

# print(str(len(numbers)))
# print(str(numbers[5]))
# numbers.append(8)  # Agregar: with append
# print(str(len(numbers)))

# print(numbers)
# numbers.pop()  # eliminar ultimo
# print(numbers)

# numbers.extend(words)  # agregar lista
# print(numbers)
# numbers.extend(combinated)  # agregar lista
# print(numbers)

# EJERCICO lista
'''Crea una lista llamada personas cuyo contenido sera de los nombres Jorge, Juan  Carlos y 3 numeros cuyos valores son 4, 5, 6
Ahora  añade un nuevo elemento a la lista con el valor “Dexter”
Ahora obtén el índice del elemento cuyo valor sea Juan
Obtén el índice del valor 5
Finalmente elimina el elemento cuyo valor es Carlos'''

# people = ["Juan", "Carlos", 4, 5, 6]
# people.append("Dexter")
# print(people)
# print(people.index("Juan"))
# print(people.index(5))
# people.remove("Carlos")
# print(people)


# TUPLAS (son datos inmutables) ()
myTupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
mySecondTupla = tuple(range(0, 10))
print(myTupla)
print(mySecondTupla)

# DICCIONARIOS: define una relación uno a uno entre claves y valores
myDict = {
    "name": "Mari",
    "lastname": "R",
    "age": "25",
    "pets": ["Tom, Hap"],
}

print(myDict["pets"])
print(myDict["name"])


# TIPOS ver
print(type(myTupla))
print(type(myDict))

# value = int(input("Ingresa: "))
# print(value + 50)
