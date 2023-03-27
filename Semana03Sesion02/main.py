# import miModulo

# miModulo.saluda("desde el main")

# edad = miModulo.pedirInfo("Escribe tu edad ")

# print(f'tu edad es {edad} anos')

# nombre = input("Digame su nombre ")

# edad = input("Escribeme tu edad ")

# print(f'Su edad es: {edad} y la mitad de su edad es: {int(edad) / 2}')
# print("Su edad es: " + edad + " y la mitad de su edad es: "+ str(int(edad)/2))
# print("Su edad es:" , edad , "y la mitad de su edad es:", int(edad)/2)


## Manejo de Errores

# try:
#     edad = int(input("Escribe tu edad: "))
#     print(f"Tu edad es: {edad}")

# except Exception as ex:
#     print("Ocurrio un error: ",ex)
# finally:
#     print("Gracias por usar el programa")


# while True:
#     try:
#         x = int(input("Escribe un numero: "))
#         print(f"El numero ingresqado es {x} ")
#         break
#     except ValueError:
#         print("Debes ingresar un numero. Intenta nuevamente...")

## Condicionares IF, ELIF,ELSE

# nota = int(input("Escribe tu nota: "))

# if nota >= 14:
#     print(f"Aprobaste con {nota}.")
# else:
#     print("Lo siento no aprobaste.")


# opcion = int(input("Escribe la opcion en numeros."))

# if opcion == 1:
#     print(f"Escogiste la opcion {opcion}.")
# elif opcion == 2:
#     print(f"Escogiste la opcion {opcion}.")
# elif opcion == 3:
#     print(f"Escogiste la opcion {opcion}.")
# elif opcion == 4:
#     print(f"Escogiste la opcion {opcion}.")
# else:
#     print(f"Escogiste la opcion {opcion}.")


##Bluces  WHILE, FOR

# suma = 0
# i = 1
# while i <= 100:
#     suma += i
#     i += 1

# print(f"La suma final es: {suma}")


# lista = ['aviones','autos','barcos','triciclos','bicicletas']

# for transporte in lista:
#     print(f"Estas usando {transporte}")
#     if transporte == 'autos':
#         break

# for valor in range(0,10):
#     print(valor,sep="1")





def collatz_conjectura(n):
    # Asegurarse de que n sea un número entero positivo
    if n <= 0:
        print("El número debe ser un entero positivo.")
        return
    
    # Imprimir el número de partida
    print(f"El numero base es: {n}")
    
    # Continuar aplicando las reglas hasta llegar a 1
    contador = 0
    while n != 1:
        if n % 2 == 0:
            # Si es par, dividir por 2
            n = n // 2
        else:
            # Si es impar, multiplicar por 3 y sumar 1
            n = 3 * n + 1
        
        # Imprimir el siguiente número en la sucesión
        print(n)
        contador += 1
    else:
        if contador == 0:
            contador = 1
        else:
            contador = contador
        
    
    return "El numero de ciclos es {}".format(contador)




while True:
    try:
        numero_entero = int(input("Ingrese un numero entero positivo:"))
        print(collatz_conjectura(numero_entero))
        break
    except ValueError:
        print("Se debe ingresar un dato del tipo numerico.")






