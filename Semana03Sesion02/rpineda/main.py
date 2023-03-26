# import miModulo

# miModulo.saluda("desde el main")

# edad = miModulo.pedirInfo("Escribe tu edad ")

# print(f'tu edad es {edad} anos')

# nombre  = input("Digame su nombre ")
# edad = input("Escribeme tu edad ")
# print(f'Su edad es: {edad} y la mitad de su edad es: {int(edad) / 2}')
# print("Su edad es: " + edad + " y la mitad de su edad es: "+ str(int(edad)/2))
# print("Su edad es:" , edad , "y la mitad de su edad es:", int(edad)/2)

# try:    
#     edad = int(input("Escribe tu edad "))
#     print(f"Tu edad es: {edad}")

# except Exception as ex:
#     print("Ocurrio un error: ",ex)
# finally:
#     print("Gracias por usar el programa")

# while True:
#     try:
#         x = int(input("Escribe un numero "))
#         print(f"El numero ingresado es {x}")
#         break
#     except ValueError:
#         print("Debes ingresar un numero. Intenta nuevamente...")

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)

# print(txt1,txt2,txt3)

# nota = int(input("Escribe tu nota"))
# if nota >= 14:
#     print(f"Aprobaste con {nota}")
# else:
#     print(f"Lo siento no aprobaste")

# opcion = int(input("Escribe la opcion en numeros"))

# if opcion == 1:
#     print(f"Escogiste la opcion {opcion}")
# elif opcion == 2:
#     print(f"Escogiste la opcion {opcion}")
# elif opcion == 3:
#     print(f"Escogiste la opcion {opcion}")
# elif opcion == 4:
#     print(f"Escogiste la opcion {opcion}")
# else:
#     print(f"Escogiste la opcion {opcion}")

# suma = 0
# i = 1
# while i <= 100:
#     suma +=  i
#     i += 1

# print(f"La suma final es: {suma}")

# lista = ['aviones', 'autos', 'barcos', 'triciclos', 'bicicletas']

# for transporte in lista:
#     print(f"Estas usuando {transporte}")
#     if transporte == 'autos':
#         break

# for valor in range(0,10,2):
#     print(valor)

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

#conjetura de Collatz

numero = int(input("Escribe un numero"))
saltos = 0

## 16 --> 16/2 = 8/2  = 4/2 = 2/2 = 1+3 = 4 
## 17 --> 17*3+1 = 52/2 = 26/2 = 13*3+1 = 40/2 = 20/2 = 10/2 = 5*3+1 = 16/2 = 8/2 = 4/2 = 2/2 = 1*3+1 = 4
##          1     2     3 *   4     5
## El numero de saltos  hasta 4 --> 2 --> 1 es : 5 saltos

print(f"El numero de saltos  hasta 4 --> 2 --> 1 es : {saltos} saltos")
