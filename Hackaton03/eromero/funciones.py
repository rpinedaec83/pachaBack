def funcion1(): # Función que determina si un número tiene 3 dígitos
    numero = int(input("Introduce un número: "))
    if 100 <= numero < 1000:
        print("El número tiene tres dígitos.")
    else:
        print("El número no tiene tres dígitos.")
    
def funcion2(): # Función que determina si un número es negativo
    numero = int(input("Introduce un número entero: "))
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número no es negativo.")
    
def funcion3(): # Función que determina si un número termina en 4
    num = int(input("Introduce un número: "))
    if num % 10 == 4:
        print("El número ingresado termina en 4.")
    else:
        print("El número ingresado no termina en 4.")
    
def funcion4(): # Función que ordena 3 números de menor a mayor
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    numero3 = int(input("Introduce el tercer número: "))
    
    numerosOrdenados = sorted([numero1, numero2, numero3])
    print(numerosOrdenados[0])
    print(numerosOrdenados[1])
    print(numerosOrdenados[2])
    
def funcion5(): # Función que calcula el total a pagar de zapatos
    totalZapatos = int(input("Introduce la cantidad de zapatos que se desea comprar: "))
    precio = 80
    total = precio * totalZapatos
    descuento = 0
    if totalZapatos > 30:
        descuento = 0.4
    elif totalZapatos > 20:
        descuento = 0.2
    elif totalZapatos > 10:
        descuento = 0.1
    print(f"El total a pagar con el descuento incluido es: ${total * (1 - descuento)}")
    
def funcion6(): # Función que calcula el sueldo semanal de un trabajador
    horasTrabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
    sueldoPorSemana = horasTrabajadas * 20 if horasTrabajadas <= 40 else (40 * 20) + ((horasTrabajadas - 40) * 25)
    print(f"El sueldo semanal del trabajador es ${sueldoPorSemana}")
    
def funcion7(): # Función que calcula el total a pagar de helados
    totalCompra = float(input("Ingrese el monto total del valor de compra de los helados: "))
    tipoMembresia = input("Ingrese el tipo de membresía (A, B o C): ")
    descuento = totalCompra * 0.1 if tipoMembresia == "A" else totalCompra * 0.15 if tipoMembresia == "B" else totalCompra * 0.2 if tipoMembresia == "C" else 0
    totalFinal = totalCompra - descuento
    print(f'El tipo de membresia es {tipoMembresia:.2f}, el descuento es de {descuento:.2f} y el precio final de compra es {totalFinal:.2f}')
    
def funcion8(): # Función que calcula el promedio de 3 notas y determina si el estudiante aprobó o no
    nota1 = float(input("Ingrese nota1: "))
    nota2 = float(input("Ingrese nota2: "))
    nota3 = float(input("Ingrese nota3: "))
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio >= 10.5:
        print("El estudiante aprobó la materia cursada con una nota final promedio de", promedio)
    else:
        print("El estudiante reprobó la materia cursada. Infelizmente, su nota final promedio fue", promedio)
    
def funcion9(): # Función que calcula el nuevo sueldo de un trabajador
    sueldoActual = int(input("Introduce el sueldo actual del trabajador: "))
    if sueldoActual > 2000:
        aumentoTrabajador = sueldoActual * 0.05
    else:
        aumentoTrabajador = sueldoActual * 0.10
    sueldoNuevo = sueldoActual + aumentoTrabajador
    print(f"El nuevo sueldo del trabajador es: {sueldoNuevo}")
    
def funcion10(): # Función que determina si un número es par o impar
    numero = int(input("Introduce un número: "))
    
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    
def funcion11(): # Función que determina el mayor de 3 números
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    numero3 = int(input("Introduce el tercer número: "))
    
    mayor = max(numero1, numero2, numero3)
    print(f"El mayor es {mayor}")
    
def funcion12(): # Función que determina el mayor de 2 números
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    
    mayor = numero1 if numero1 > numero2 else numero2
    print(f"El mayor es {mayor}")
    
def funcion13(): # Función que determina si una letra es vocal o no
    letra = input("Introduce una letra: ")
    
    if letra.lower() in 'aeiou':
        print(f"{letra} es una vocal")
    else:
        print(f"{letra} no es una vocal")
    
def funcion14(): # Función que determina si un número es primo o no
    numero = int(input("Introduce un número entero positivo del 1 al 9: "))
    if numero < 1 or numero > 9:
        print("El número debe estar entre 1 y 9")
    else:
        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")
    
def funcion15(): # Función que convierte de centímetros a pulgadas y de libras a kilos
    centimetros = float(input("Ingrese la cantidad en centímetros: "))
    pulgadas = centimetros / 2.54
    print(f"{centimetros} centímetros equivale a {pulgadas} pulgadas")
    
    libras = float(input("Ingrese la cantidad en libras: "))
    kilos = libras / 2.20462
    print(f"{libras} libras equivale a {kilos} kilos")
    
def funcion16(): # Función que convierte un número del 1 al 7 a su equivalente en día de la semana
    numero = int(input("Introduce un número del 1 al 7: "))
    
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miércoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sábado")
    elif numero == 7:
        print("Domingo")
    else:
        print("Número no válido. Introduzca un número del 1 al 7.")
    
def funcion17(): # Función que calcula la hora siguiente a la introducida por el usuario
    hora = int(input("Ingresa la hora: "))
    minuto = int(input("Ingresa el minuto: "))
    segundo = int(input("Ingresa los segundos: "))
    
    if (hora < 24 and minuto < 60 and segundo < 60):
        segundo = segundo + 1
    if (segundo == 60):
        segundo = 0
        minuto = minuto + 1
    if (minuto == 60):
        minuto = 0
        hora = hora + 1
    
    print(f"{hora} : {minuto} : {segundo}")
    
def funcion18(): # Función que calcula el precio total a pagar por un cliente y la ganancia del vendedor
    cantidad = int(input('Ingrese la cantidad de CDs a vender: '))
    if cantidad < 10:
        precioUnitario = 10
        precioTotal = precioUnitario * cantidad
        gananciaVendedor = precioTotal * 0.0825
    elif cantidad < 100:
        precioUnitario = 8
        precioTotal = precioUnitario * cantidad
        gananciaVendedor = precioTotal * 0.0825
    elif cantidad < 500:
        precioUnitario = 7
        precioTotal = precioUnitario * cantidad
        gananciaVendedor = precioTotal * 0.0825
    else:
        precioUnitario = 6
        precioTotal = precioUnitario * cantidad
        gananciaVendedor = precioTotal * 0.0825
    print(f'El precio total a pagar para el cliente es: ${precioTotal}')
    print(f'La ganancia por las ventas para el vendedor es: ${gananciaVendedor}')
    
def funcion19(): # Función que calcula el sueldo de un trabajador
    sueldos = {
        1: 56, # Cajero
        2: 64, # Servidor
        3: 80, # Preparador de mezclas
        4: 48  # Mantenimiento
    }
    
    codEmpleado = int(input('Ingrese el codigo del empleado (1-4): '))
    diasTrabajados = int(input('Ingrese la cantidad de días trabajados (máximo 6): '))
    
    if codEmpleado in sueldos and 0 < diasTrabajados <= 6:
        sueldoDiario = sueldos[codEmpleado]
        sueldoTotal = sueldoDiario * diasTrabajados
        print(f'El sueldo que el trabajador recibira esta semana es de: ${sueldoTotal}')
    else:
        print('Los datos ingresados no válidos')
    
def funcion20(): # Función que calcula el sueldo de un trabajador
    numeros = []
    for i in range(1, 5):
        numeros.append(int(input(f'Ingrese el número {i}: ')))
    
    pares = sum(1 for n in numeros if n % 2 == 0)
    print(f'Hay {pares} números pares')
    
    mayor = max(numeros)
    print(f'El mayor de todos es: {mayor}')
    
    if numeros[2] % 2 == 0:
        cuadrado = numeros[1] ** 2
        print(f'El cuadrado del segundo es: {cuadrado}')
    
    if numeros[0] < numeros[3]:
        media = sum(numeros) / len(numeros)
        print(f'La media de los 4 números es: {media}')
    
    if numeros[1] > numeros[2]:
        if 50 < numeros[2] < 700:
            suma = sum(numeros)
            print(f'La suma de los 4 números es: {suma}')
    
def funcion21(): # Función que calcula el factorial de un número
    from math import factorial
    n = int(input('Introduce un número: '))
    print(f'El factorial de {n} es: {factorial(n)}')

def funcion22(): # Función que calcula la suma de los primeros n números naturales
    n = int(input("Ingrese un número: "))
    sumaTotal = n * (n + 1) // 2
    print(f" La suma de los {n} números es: {sumaTotal}") 
    
def funcion23(): # Función que calcula la suma de los números impares menores o iguales a n
    n = int(input("Ingrese un número: "))
    cantidadImpares = (n + 1) // 2
    sumaTotal = cantidadImpares ** 2
    print(f"La suma de los números impares menores o iguales a {n} es {sumaTotal}.")
    
def funcion24(): # Función que calcula la suma de los números pares menores o iguales a 1000
    cantidadPares = 1000 // 2
    sumaTotal = cantidadPares * (cantidadPares + 1)
    print(f"La suma de todos los números pares hasta el 1000 es {sumaTotal}.")
    
def funcion25(): # Función que calcula el factorial de un número
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
    n = int(input("Ingrese un número: "))
    print(f"El factorial de {n} es {factorial(n)}.")
    
def funcion26(): # Función que calcula el cociente y el resto de la división de dos números
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    cociente = 0
    residuo = dividendo
    while residuo >= divisor:
        residuo -= divisor
        cociente += 1
    print(f"El cociente es {cociente} y el resto es {residuo}.")
    
def funcion27(): # Función que calcula la media de una serie de números positivos
    cuenta = 0
    total = 0
    while True:
        numero = int(input("Ingrese un número positivo (o un número negativo para terminar): "))
        if numero < 0:
            break
        cuenta += 1
        total += numero
    if cuenta > 0:
        media = total / cuenta
        print(f"La media de los números ingresados es: {media}.")
    else:
        print("Error, falta ingresar los números.")
    
def funcion28(): # Función que calcula la suma de los primeros cien números naturales
    suma = 0
    for n in range(1, 100 + 1):
        suma += n
    print(f"La suma de los primeros cien numeros es: {suma}")
    
def funcion29(): # Función que calcula la suma de los primeros cien números naturales
    suma = 0
    x = 1
    while x <= 100:
        suma += x
        x += 1
    print(f"La suma de los primeros cien numeros es: {suma}")
    
def funcion30(): # Función que calcula la suma de los primeros cien números naturales
    suma = 0
    for x in range(1, 101):
        suma += x
    print(f"La suma de los primeros cien numeros es{suma}")
    
def funcion31(): # Función que calcula la media de los números pares e impares de una serie de 10 números
    numeros = [int(input("Introduce un número: ")) for _ in range(10)]
    
    sumaPares = 0
    sumaImpares = 0
    cantidadPares = 0
    cantidadImpares = 0
    
    for num in numeros:
        if num % 2 == 0:
            sumaPares += num
            cantidadPares += 1
        else:
            sumaImpares += num
            cantidadImpares += 1
    
    mediaPares = sumaPares / cantidadPares if cantidadPares > 0 else 0
    mediaImpares = sumaImpares / cantidadImpares if cantidadImpares > 0 else 0
    
    print("La media de números pares es:", mediaPares)
    print("La media de números impares es:", mediaImpares)
    
def funcion32(): # Función que calcula la población mayor de cada provincia
    contadorCiudad = 0
    contadorProvincia = 1
    ciudad = 0
    mayorPoblacion = 0
    
    while(contadorProvincia <= 3):
        mayorPoblacion = 0
        contadorCiudad = 1
        print(f"Provincia {contadorProvincia}")
        while (contadorCiudad <= 11):
            ciudad = int(input("Los habitantes de ciudad son: "))
            if(ciudad > mayorPoblacion):
                mayorPoblacion = ciudad
                contadorCiudad = contadorCiudad + 1
            print(f"La poblacion mayor de la provincia {contadorProv} es {mayorPoblacion}")
            contadorProv = contadorProv + 1
    
def funcion33(): # Función que calcula la población mayor de cada provincia
    while True:
        print("Continua programa...")
        continua = input("¿Desea continuar? (s/n): ")
        if continua.lower() != 's':
            break
    print("Salir del programa...")
    
def funcion34(): # Función que calcula la tabla de multiplicar
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()
    
def funcion35(): # Función que calcula el número mayor y menor de una serie de 20 números
    numeros = []
    for i in range(20):
        num = int(input("Introduce un número: "))
        numeros.append(num)
    
    mayor = max(numeros)
    menor = min(numeros)
    
    print("El número mayor es:", mayor)
    print("El número menor es:", menor)
    
def funcion36(): # Función que calcula la serie de Fibonacci
    a, b = 0, 1
    while b < 100:
        print(b)
        a, b = b, a + b
    
def funcion37(): # Función que calcula el M.C.D de dos números
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    print(f"El M.C.D de {num1} y {num2} es {mcd(num1, num2)}")
    
def funcion38(): # Función que calcula si un número es perfecto
    def es_perfecto(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma == n
    
    num = int(input("Introduce un número: "))
    
    if es_perfecto(num):
        print(f"{num} es un número perfecto")
    else:
        print(f"{num} no es un número perfecto")
    
def funcion39(): # Función que calcula la sucesión de pi
    i = 0
    contador = 0
    pi = 0
    
    print("Ingrese un numero")
    numero = int(input("Para calcular la sucesion de pi"))
    for i in range (1, numero, 2):
        if (contador % 2 == 0):
             pi = pi + (4 / i)
        else:
             pi = pi - (4 / i)
    
    print(f"Pi se aproxima a: {pi}")
    
def funcion40(): # Función que calcula la sucesión de pi
    i = 0
    contador = 0
    pi = 0
    print ("Ingrese un numero")
    numero = int(input("Para calcular la sucesion de pi "))
    for i in range (2, numero, 2):
        if(contador % 2 == 0):
            pi = pi + (4/(i*(i+1)*(i+2)))
        else:
            pi = pi - (4/(i*(i+1)*(i+2)))
            contador = contador + 1
    print(f"Pi se aproxima a: {pi}")