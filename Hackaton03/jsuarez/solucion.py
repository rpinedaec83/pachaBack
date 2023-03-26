
# def ejercicio01():
#     #Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos
#     numero = int(input("Escribe un numero: "))
#     strnumero = str(numero)
#     if len(strnumero) == 3:
#         print(f"Este numero tiene {len(strnumero)} digitos")
#     else:
#         print(f"Este numero no cumple con la condicion solo tiene {len(strnumero)} digitos")

# def ejercicio02():
#     #2. Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
#     print("Es negativo o no")

# Ejercicio 1
def ejercicio01():
    # Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos.
    numero = int(input("Ingrese un número: "))
    if numero >= 100 and numero <= 999:
        print("El número tiene tres dígitos.")
    else:
        print("El número no tiene tres dígitos.")

# Ejercicio 2
def ejercicio02():
    # Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número no es negativo.")

# Ejercicio 3
def ejercicio03():
    # Hacer un programa en Python que lea un número y determinar si termina en 4.
    numero = int(input("Ingrese un número: "))
    if numero % 10 == 4:
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")

# Ejercicio 4
def ejercicio04():
    # Hacer un programa en Python que lea tres números enteros y los muestre de menor a mayor.
    numeros = []
    for i in range(3):
        numero = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
    numeros.sort()
    print("Los números en orden ascendente son:", numeros)

# Ejercicio 5
def ejercicio05():
    # Hacer un programa en Python para una tienda de zapatos que tiene una promoción de descuento para vender al mayor,
    # esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total
    # de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y
    # si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.
    numero_zapatos = int(input("Ingrese el número de zapatos que desea comprar: "))
    precio_zapato = 80
    total_compra = numero_zapatos * precio_zapato

    if numero_zapatos > 30:
        descuento = total_compra * 0.4
    elif numero_zapatos > 20:
        descuento = total_compra * 0.2
    elif numero_zapatos > 10:
        descuento = total_compra * 0.1
    else:
        descuento = 0

    precio_final = total_compra - descuento

    print(f"El precio final de la compra es: ${precio_final:.2f}")

def ejercicio06():
    #Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal,
    #se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas
    #entonces las horas extras se le pagarán a $25 por hora.
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
    if horas_trabajadas <= 40:
        sueldo = horas_trabajadas * 20
    else:
        sueldo = 40 * 20 + (horas_trabajadas - 40) * 25
    print(f"El sueldo semanal es: ${sueldo}")

def ejercicio07():
    #Hacer un programa en Python para una tienda de helado que da un descuento por compra a sus clientes con membresía
    #dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
    #Tipo A 10% de descuento Tipo B 15% de descuento Tipo C 20% de descuento
    precio_total = float(input("Ingrese el precio total de la compra: "))
    tipo_membresia = input("Ingrese el tipo de membresía (A, B o C): ")
    if tipo_membresia == "A":
        descuento = precio_total * 0.1
    elif tipo_membresia == "B":
        descuento = precio_total * 0.15
    elif tipo_membresia == "C":
        descuento = precio_total * 0.2
    else:
        print("El tipo de membresía ingresado no es válido.")
        return
    precio_final = precio_total - descuento
    print(f"El precio final de la compra es: ${precio_final}")


def ejercicio08():
    #Hacer un programa en Python para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de las notas es: {promedio}")
    if promedio >= 3:
        print("El estudiante aprobó.")
    else:
        print("El estudiante reprobó.")


def ejercicio09():
    #Hacer un programa en Python para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000
    #tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.
    salario_anterior = float(input("Ingrese el salario anterior: "))
    if salario_anterior > 2000:
        aumento = salario_anterior * 0.05
    else:
        aumento = salario_anterior * 0.1
    salario_nuevo = salario_anterior + aumento
    print(f"El aumento es de: ${aumento}")
    print(f"El salario nuevo es: ${salario_nuevo}")


def ejercicio10():
    # Hacer un programa en Python que lea un número entero por teclado y determine si es un número primo.
    numero = int(input("Escriba un numero entero: "))
    if numero < 2:
        print("El numero no es primo")
    elif numero == 2:
        print("El numero es primo")
    else:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print("El numero es primo")
        else:
            print("El numero no es primo")


def ejercicio11():
    # Hacer un programa en Python que lea tres números y diga cuál es el mayor.
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    if num1 > num2 and num1 > num3:
        print("El mayor es:", num1)
    elif num2 > num1 and num2 > num3:
        print("El mayor es:", num2)
    elif num3 > num1 and num3 > num2:
        print("El mayor es:", num3)
    else:
        print("Los tres números son iguales.")


def ejercicio12():
    # Hacer un programa en Python que lea dos números y diga cuál es el mayor.
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num1 > num2:
        print("El mayor es:", num1)
    elif num2 > num1:
        print("El mayor es:", num2)
    else:
        print("Los dos números son iguales.")


def ejercicio13():
    # Hacer un programa en Python que lea una letra y diga si es una vocal.
    letra = input("Ingrese una letra: ")
    if letra in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print("La letra es una vocal.")
    else:
        print("La letra es una consonante.")


def ejercicio14():
    # Hacer un programa en Python que lea un entero positivo del 1 al diez y determine si es un número primo.
    numero = int(input("Ingrese un número del 1 al 10: "))
    
    if numero in [1, 4, 6, 8, 9, 10]:
        print("El número no es primo.")
    elif numero in [2, 3, 5, 7]:
        print("El número es primo.")

    else:
        print("Ingresar un numero en el rango indicado: (1 al 10)")


def ejercicio15():
    # Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos.
    opcion = input("¿Qué desea convertir, centímetros o libras?: ")
    if opcion.lower() == "centimetros":
        cm = float(input("Ingrese la medida en centímetros: "))
        pulgadas = cm / 2.54
        print("La medida en pulgadas es:", pulgadas)
    elif opcion.lower() == "libras":
        lb = float(input("Ingrese el peso en libras: "))
        kg = lb / 2.20462
        print("El peso en kilogramos es:", kg)
    else:
        print("Opción inválida.")

def ejercicio16():
    dia = int(input("Ingrese un número del 1 al 7 para conocer el día de la semana: "))
    if dia == 1:
        print("El número corresponde al día Lunes.")
    elif dia == 2:
        print("El número corresponde al día Martes.")
    elif dia == 3:
        print("El número corresponde al día Miércoles.")
    elif dia == 4:
        print("El número corresponde al día Jueves.")
    elif dia == 5:
        print("El número corresponde al día Viernes.")
    elif dia == 6:
        print("El número corresponde al día Sábado.")
    elif dia == 7:
        print("El número corresponde al día Domingo.")
    else:
        print("El número ingresado no está en el rango del 1 al 7.")

def ejercicio17():
    hora = input("Ingrese la hora en formato HH:MM:SS: ")
    h, m, s = map(int, hora.split(':'))
    if s < 59:
        s += 1
    elif m < 59:
        s = 0
        m += 1
    elif h < 23:
        s = 0
        m = 0
        h += 1
    else:
        s = 0
        m = 0
        h = 0
    print(f"La hora dentro de un segundo es: {h:02d}:{m:02d}:{s:02d}")


def ejercicio18():
    # Definir los precios y la ganancia del vendedor
    PRECIO_1 = 10
    PRECIO_2 = 8
    PRECIO_3 = 7
    PRECIO_4 = 6
    GANANCIA = 0.0825

    # Leer la cantidad de CDs a vender
    cantidad = int(input("Ingrese la cantidad de CDs a vender: "))

    # Calcular el precio total para el cliente y la ganancia para el vendedor
    if cantidad < 10:
        precio_total = cantidad * PRECIO_1
    elif cantidad < 100:
        precio_total = cantidad * PRECIO_2
    elif cantidad < 500:
        precio_total = cantidad * PRECIO_3
    else:
        precio_total = cantidad * PRECIO_4

    ganancia_vendedor = precio_total * GANANCIA

    # Imprimir los resultados
    print(f"Precio total para el cliente: ${precio_total}")
    print(f"Ganancia para el vendedor: ${ganancia_vendedor:.2f}")


def ejercicio19():
    # Definimos los datos de cada tipo de empleado
    cajero = [56, "Cajero"]
    servidor = [64, "Servidor"]
    preparador = [80, "Preparador de mezclas"]
    mantenimiento = [48, "Mantenimiento"]

    # Pedimos al usuario el número identificador y la cantidad de días trabajados
    identificador = int(input("Ingrese el número identificador del empleado (1 para Cajero, 2 para Servidor, 3 para Preparador de mezclas o 4 para Mantenimiento): "))
    dias_trabajados = int(input("Ingrese la cantidad de días trabajados en la semana (máximo 6 días): "))

    # Obtenemos el salario correspondiente según el tipo de empleado
    if identificador == 1:
        salario = cajero[0] * dias_trabajados
        cargo = cajero[1]
    elif identificador == 2:
        salario = servidor[0] * dias_trabajados
        cargo = servidor[1]
    elif identificador == 3:
        salario = preparador[0] * dias_trabajados
        cargo = preparador[1]
    elif identificador == 4:
        salario = mantenimiento[0] * dias_trabajados
        cargo = mantenimiento[1]
    else:
        print("Número identificador de empleado inválido")
        return

    # Mostramos el salario a pagar al empleado
    print(f"El empleado de {cargo} que trabajó {dias_trabajados} días esta semana debe recibir {salario} pesos.")


def ejercicio20():
    numeros = []
    for i in range(4):
        numeros.append(int(input(f"Ingrese el {i+1}° número entero positivo: ")))
    
    # ¿Cuántos números son Pares?
    pares = [n for n in numeros if n % 2 == 0]
    print(f"Hay {len(pares)} números pares: {pares}")
    
    # ¿Cuál es el mayor de todos?
    mayor = max(numeros)
    print(f"El número mayor es: {mayor}")
    
    # Si el tercero es par, calcular el cuadrado del segundo.
    if numeros[2] % 2 == 0:
        cuadrado = numeros[1] ** 2
        print(f"El cuadrado del segundo número es: {cuadrado}")
    
    # Si el primero es menor que el cuarto, calcular la media de los 4 números.
    if numeros[0] < numeros[3]:
        media = sum(numeros) / len(numeros)
        print(f"La media de los 4 números es: {media}")
    
    # Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido entre los valores 50 y 700.
    # Si cumple se cumple la segunda condición, calcular la suma de los 4 números.
    if numeros[1] > numeros[2] and 50 <= numeros[2] <= 700:
        suma = sum(numeros)
        print(f"La suma de los 4 números es: {suma}")

def ejercicio21():
    # Hacer un programa en Python que permita calcular el factorial de un número.
    num = int(input("Ingrese un número entero para calcular su factorial: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")

def ejercicio22():
    # Hacer un programa en Python para calcular la suma de los n primeros números.
    n = int(input("Ingrese un número entero positivo: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los primeros {n} números es: {suma}")

def ejercicio23():
    # Hacer un programa en Python para calcular la suma de los números impares menores o iguales a n.
    n = int(input("Ingrese un número entero positivo: "))
    suma_impares = 0
    for i in range(1, n + 1, 2):
        suma_impares += i
    print(f"La suma de los números impares menores o iguales a {n} es: {suma_impares}")

def ejercicio24():
    # Hacer un programa en Python para realizar la suma de todos los números pares hasta el 1000.
    suma_pares = 0
    for i in range(2, 1001, 2):
        suma_pares += i
    print(f"La suma de todos los números pares hasta 1000 es: {suma_pares}")

def ejercicio25():
    # Hacer un programa en Python para calcular el factorial de un número de una forma distinta.
    num = int(input("Ingrese un número entero para calcular su factorial: "))
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print(f"El factorial es: {factorial}")


def ejercicio26():
    # Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas.
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    print(f"El cociente es {cociente} y el resto es {dividendo}")

def ejercicio27():
    # Hacer un programa en Python para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número negativo.
    numeros = []
    while True:
        numero = float(input("Ingrese un número positivo (ingrese un número negativo para salir): "))
        if numero < 0:
            break
        numeros.append(numero)
    if len(numeros) == 0:
        print("No se ingresaron números positivos.")
    else:
        media = sum(numeros) / len(numeros)
        print(f"La media de los números ingresados es: {media}")

def ejercicio28():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.
    i = 1
    suma = 0
    repeat = True
    while repeat:
        suma += i
        i += 1
        if i > 100:
            repeat = False
    print(f"La suma de los primeros cien números es: {suma}")

def ejercicio29():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo mientras.
    i = 1
    suma = 0
    while i <= 100:
        suma += i
        i += 1
    print(f"La suma de los primeros cien números es: {suma}")

def ejercicio30():
    # Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo para.
    suma = 0
    for i in range(1, 101):
        suma += i
    print(f"La suma de los primeros cien números es: {suma}")

def ejercicio31():
    # Hacer un programa en Python para calcular la media de los números pares e impares, sólo se ingresará diez números.
    numeros_pares = []
    numeros_impares = []
    for i in range(10):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    promedio_pares = sum(numeros_pares) / len(numeros_pares)
    promedio_impares = sum(numeros_impares) / len(numeros_impares)
    print(f"El promedio de los numeros pares es: {promedio_pares}")
    print(f"El promedio de los numeros impares es: {promedio_impares}")


def ejercicio32():
    # Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, Hacer un programa en Python que nos permita saber eso. Datos de Lambayeque, Lima, Loreto
    poblacion_lambayeque = int(input("Ingrese la poblacion de Lambayeque: "))
    poblacion_lima = int(input("Ingrese la poblacion de Lima: "))
    poblacion_loreto = int(input("Ingrese la poblacion de Loreto: "))
    ciudades = {
        "Lambayeque": poblacion_lambayeque,
        "Lima": poblacion_lima,
        "Loreto": poblacion_loreto
    }
    ciudad_mas_poblada = max(ciudades, key=ciudades.get)
    print(f"La ciudad con la poblacion mas grande es: {ciudad_mas_poblada}")


def ejercicio33():
    # Hacer un programa en Python que permita al usuario continuar con el programa.
    continuar = True
    while continuar:
        print("Este es un programa que se repite.")
        opcion = input("Desea continuar? (s/n): ")
        if opcion.lower() == "n":
            continuar = False


def ejercicio34():
    # Hacer un programa en Python que imprima la tabla de multiplicar de los números del uno al nueve.
    for i in range(1, 10):
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")


def ejercicio35():
    # Hacer un programa en Python que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
    numeros = []
    for i in range(20):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        numeros.append(numero)
    numero_mayor = max(numeros)
    numero_menor = min(numeros)
    print(f"El numero mayor es: {numero_mayor}")
    print(f"El numero menor es: {numero_menor}")


def ejercicio36():
    # Hacer un programa en Python para calcular la serie de Fibonacci.
    n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci a calcular: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def ejercicio37():
    # Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = mcd(num1, num2)
    print(f"El M.C.D de {num1} y {num2} es {resultado}")


def ejercicio38():
    # Hacer un programa en Python que nos permita saber si un número es un número perfecto.
    def es_perfecto(num):
        suma_divisores = 0
        for i in range(1, num):
            if num % i == 0:
                suma_divisores += i
        return suma_divisores == num

    numero = int(input("Ingrese un número: "))
    if es_perfecto(numero):
        print(f"{numero} es un número perfecto")
    else:
        print(f"{numero} no es un número perfecto")


def ejercicio39():
    # Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz.
    def aproximacion_pi(n):
        pi = 0
        signo = 1
        for i in range(1, n*2, 2):
            pi += signo * (4/i)
            signo *= -1
        return pi

    terminos = int(input("Ingrese la cantidad de términos a utilizar para la aproximación: "))
    pi_aprox = aproximacion_pi(terminos)
    print(f"La aproximación de Pi con {terminos} términos es: {pi_aprox}")


def ejercicio40():
    # Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Nilakantha.
    def aproximacion_pi(n):
        pi = 3
        signo = 1
        denominador = 2
        for i in range(n):
            termino = 4 / (denominador * (denominador + 1) * (denominador + 2))
            pi += signo * termino
            signo *= -1
            denominador += 2
        return pi

    terminos = int(input("Ingrese la cantidad de términos a utilizar para la aproximación: "))
    pi_aprox = aproximacion_pi(terminos)
    print(f"La aproximación de Pi con {terminos} términos es: {pi_aprox}")





