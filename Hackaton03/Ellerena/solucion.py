def ejercicio01():
    #Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos
    numero = int(input("Escribe un numero: "))
    strnumero = str(numero)
    if len(strnumero) == 3:
        print(f"Este numero tiene {len(strnumero)} digitos")
    else:
        print(f"Este numero no cumple con la condicion solo tiene {len(strnumero)} digitos")

def ejercicio02():
    #2. Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    print("Es negativo o no")

def ejercicio03():
    numero = input("Ingresa un número: ")
    if numero[-1] == "4":
        print("El número termina en 4")
    else:
        print("El número no termina en 4")


def ejercicio04():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num1 <= num2 and num1 <= num3:
        menor = num1
        if num2 <= num3:
            medio = num2
            mayor = num3
        else:
            medio = num3
            mayor = num2
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        if num1 <= num3:
            medio = num1
            mayor = num3
        else:
            medio = num3
            mayor = num1
    else:
        menor = num3
        if num1 <= num2:
            medio = num1
            mayor = num2
        else:
            medio = num2
            mayor = num1

    print("Los números ordenados de menor a mayor son:", menor, medio, mayor)

def ejercicio05():
    precio_zapato = 80


    cantidad_zapatos = int(input("¿Cuántos zapatos desea comprar? "))


    precio_total = cantidad_zapatos * precio_zapato


    if cantidad_zapatos > 30:
        descuento = 0.4
    elif cantidad_zapatos > 20:
        descuento = 0.2
    elif cantidad_zapatos > 10:
        descuento = 0.1
    else:
        descuento = 0

    precio_descuento = precio_total - (precio_total * descuento)

    print("El precio total de la compra es:", precio_total)
    print("El descuento aplicado es:", descuento * 100, "%")
    print("El precio total con descuento es:", precio_descuento)

def ejercicio06():
    num_zapatos = int(input("Ingrese la cantidad de zapatos que desea comprar: "))
    precio_zapato = 80
    descuento = 0

    if num_zapatos > 30:
        descuento = 0.4
    elif num_zapatos > 20:
        descuento = 0.2
    elif num_zapatos > 10:
        descuento = 0.1

    total_sin_descuento = num_zapatos * precio_zapato
    total_con_descuento = total_sin_descuento * (1 - descuento)

    print("El precio total de su compra es:", total_con_descuento)

def ejercicio07():
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en la semana: "))
    pago_hora_normal = 20
    pago_hora_extra = 25

    if horas_trabajadas <= 40:
        sueldo_semanal = horas_trabajadas * pago_hora_normal
    else:
        horas_extras = horas_trabajadas - 40
    sueldo_semanal = 40 * pago_hora_normal + horas_extras * pago_hora_extra

    print("Su sueldo semanal es:", sueldo_semanal)

def ejercicio08():
    precio_helado = 100
    tipo_membresia = input("Ingrese su tipo de membresía (A, B o C): ")

    if tipo_membresia == "A":
        descuento = 0.1
    elif tipo_membresia == "B":
        descuento = 0.15
    elif tipo_membresia == "C":
        descuento = 0.2
    else:
        descuento = 0

    precio_final = precio_helado * (1 - descuento)

    print("El precio final de su helado es:", precio_final)

def ejercicio09():
    salario_actual = float(input("Ingrese su salario actual: "))

    if salario_actual > 2000:
        aumento = 0.05
    else:
        aumento = 0.1

    salario_nuevo = salario_actual * (1 + aumento)

    print("Su nuevo salario es:", salario_nuevo)

def ejercicio10():
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

def ejercicio11():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))

    if a >= b and a >= c:
        print("El número mayor es:", a)
    elif b >= a and b >= c:
        print("El número mayor es:", b)
    else:
        print("El número mayor es:", c)


def ejercicio12():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if a > b:
        print("El número mayor es:", a)
    else:
        print("El número mayor es:", b)

def ejercicio13():
    letra = input("Ingrese una letra: ")

    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("La letra es una vocal")
    else:
        print("La letra no es una vocal")

def ejercicio14():
    num = int(input("Ingrese un número entre 1 y 10: "))

    if num in [2, 3, 5, 7]:
        print("El número es primo")
    else:
        print("El número no es primo")


def ejercicio15():
    cm = float(input("Ingrese una longitud en centímetros: "))
    inches = cm / 2.54
    print("La longitud en pulgadas es:", inches)

    lbs = float(input("Ingrese un peso en libras: "))
    kg = lbs * 0.453592
    print("El peso en kilogramos es:", kg)


def ejercicio16():
    num = int(input("Ingrese un número del 1 al 7: "))

    if num == 1:
        print("Lunes")
    elif num == 2:
        print("Martes")
    elif num == 3:
        print("Miércoles")
    elif num == 4:
        print("Jueves")
    elif num == 5:
        print("Viernes")
    elif num == 6:
        print("Sábado")
    elif num == 7:
        print("Domingo")
    else:
        print("Número inválido. Debe ser un número del 1 al 7.")

def ejercicio17():
    hora = input("Ingrese la hora en formato HH:MM:SS: ")
    hora_siguiente = ""
    if len(hora) == 8 and hora[2] == ":" and hora[5] == ":":
        horas = int(hora[:2])
        minutos = int(hora[3:5])
        segundos = int(hora[6:])
        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59:
            print("Hora inválida.")
        else:
            if segundos == 59:
                segundos = 0
                if minutos == 59:
                    minutos = 0
                    if horas == 23:
                        horas = 0
                    else:
                        horas += 1
                else:
                    minutos += 1
            else:
                segundos += 1

            hora_siguiente = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            print(f"La hora siguiente es: {hora_siguiente}")
    else:
        print("Formato de hora inválido. Debe ser en formato HH:MM:SS.")


def ejercicio18():
    cantidad = int(input("Ingrese la cantidad de CDs a vender: "))
    precio_total = 0

    if cantidad < 1:
        print("Cantidad inválida. Debe ser un número entero positivo mayor que cero.")
    else:
        if cantidad < 10:
            precio_total = cantidad * 10
        elif cantidad < 100:
            precio_total = cantidad * 8
        elif cantidad < 500:
            precio_total = cantidad * 7
        else:
            precio_total = cantidad * 6

        ganancia_vendedor = precio_total * 0.0825
        precio_total += ganancia_vendedor

        print(f"Precio total para el cliente: ${precio_total:.2f}")
        print(f"Ganancia para el vendedor: ${ganancia_vendedor:.2f}")

def ejercicio19():
    def calcular_salario(identificador, dias_trabajados):
        salarios = {56: "Cajero", 64: "Servidor", 80: "Preparador de mezclas", 48: "Mantenimiento"}
        if identificador not in salarios:
            print("Identificador de empleado inválido")
            return
        salario_diario = salarios[identificador]
        salario_semanal = salario_diario * dias_trabajados
        print(f"El salario para el empleado {salario_diario} por {dias_trabajados} días es {salario_semanal}$")

    identificador = int(input("Ingrese el identificador del empleado (56, 64, 80, 48): "))
    dias_trabajados = int(input("Ingrese la cantidad de días trabajados (1-6): "))
    calcular_salario(identificador, dias_trabajados)



def ejercicio20():
    numeros = []

    for i in range(4):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    pares = [num for num in numeros if num % 2 == 0]
    print(f"Hay {len(pares)} números pares")

    mayor = max(numeros)
    print(f"El número mayor es {mayor}")

    if numeros[2] % 2 == 0:
        segundo_cuadrado = numeros[1] ** 2
        print(f"El cuadrado del segundo número es {segundo_cuadrado}")

    if numeros[0] < numeros[3]:
        media = sum(numeros) / len(numeros)
        print(f"La media de los 4 números es {media}")


    if numeros[1] > numeros[2] and 50 <= numeros[2] <= 700:
        suma = sum(numeros)
        print(f"La suma de los 4 números es {suma}")

def ejercicio21():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
        
def ejercicio22():
    def suma_n(n):
     return sum(range(1, n+1))

def ejercicio23():
    def suma_impares(n):
        return sum(range(1, n+1, 2))
def ejercicio24():
    def suma_pares():
        return sum(range(0, 1001, 2))
    
def ejercicio25():
    def factorial2(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

def ejercicio26():
    dividendo = int(input("Introduce el dividendo: "))
    divisor = int(input("Introduce el divisor: "))

    cociente = 0

    while dividendo >= divisor:
        dividendo -= divisor
    cociente += 1

    resto = dividendo

    print("El cociente es:", cociente)
    print("El resto es:", resto)

def ejercicio27():
    suma = 0
    numeros = 0

    while True:
        numero = float(input("Introduce un número positivo (introduce un negativo para acabar): "))
        if numero < 0:
            suma += numero
            numeros += 1

        if numeros > 0:
            media = suma / numeros
            print("La media es:", media)
        else:
            print("No se introdujo ningún número positivo.")



def ejercicio28():
    suma = 0
    contador = 1

    while contador <= 100:
        suma += contador
        contador += 1

    print("La suma de los primeros cien números es:", suma)


def ejercicio29():
    suma = 0
    contador = 1

    while contador <= 100:
        suma += contador
    contador += 1

    print("La suma de los primeros cien números es:", suma)

def ejercicio30():
    suma = 0

    for contador in range(1, 101):
        suma += contador

    print("La suma de los primeros cien números es:", suma)

def ejercicio31():
    suma_pares = 0
    num_pares = 0
    suma_impares = 0
    num_impares = 0

    for i in range(10):
        num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        suma_pares += num
        num_pares += 1
    else:
        suma_impares += num
        num_impares += 1

    if num_pares > 0:
        media_pares = suma_pares / num_pares
        print("La media de los números pares es:", media_pares)
    else:
        print("No se ingresaron números pares.")

    if num_impares > 0:
        media_impares = suma_impares / num_impares
        print("La media de los números impares es:", media_impares)
    else:
        print("No se ingresaron números impares.")

def ejercicio32():
    provincias = ["Lambayeque", "Lima", "Loreto"]
    ciudades = [[500000, 600000, 700000], [800000, 900000, 1000000], [1100000, 1200000, 1300000]]

    poblacion_max = 0
    ciudad_max = ""

    for i in range(len(provincias)):
        for j in range(len(ciudades[i])):
            if ciudades[i][j] > poblacion_max:
                poblacion_max = ciudades[i][j]
    ciudad_max = "Ciudad " + str(j+1) + " de " + provincias[i]

    print("La ciudad con la población más grande es:", ciudad_max)

def ejercicio33():
    while True:
        opcion = input("¿Desea continuar con el programa? (S/N): ")


def ejercicio34():
    for i in range(1, 10):
        print("Tabla de multiplicar del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
        print()

def ejercicio35():
    numeros = []
    for i in range(20):
        num = int(input("Ingrese un número: "))
        numeros.append(num)

        num_mayor = max(numeros)
        num_menor = min(numeros)

    print("El número mayor es:", num_mayor)
    print("El número menor es:", num_menor)

def ejercicio36():
    n = int(input("Ingrese un número: "))

    fibonacci = [0, 1]

    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    print("La serie de Fibonacci de longitud", n, "es:", fibonacci)

def ejercicio37():
    def mcd(a, b):
        if b == 0:
            return a
        else:
            return mcd(b, a % b)

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    resultado = mcd(num1, num2)

    print("El M.C.D de", num1, "y", num2, "es:", resultado)

def ejercicio38():
    def es_perfecto(num):
        div = 1
        suma = 0
        while div < num:
            if num % div == 0:
                suma += div
                div += 1
        if suma == num:
            return True
        else:
            return False

    num = int(input("Ingrese un número: "))

    if es_perfecto(num):
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto.")

def ejercicio39():
    num_iteraciones = int(input("Ingrese el número de iteraciones para la aproximación de pi: "))

    pi = 0
    signo = 1

    for i in range(1, num_iteraciones*2, 2):
        termino = 4/i * signo
    pi += termino
    signo = -signo

    print("La aproximación de pi con", num_iteraciones, "iteraciones es:", pi)

def ejercicio40():
    num_iteraciones = int(input("Ingrese el número de iteraciones para la aproximación de pi: "))


    pi = 3
    signo = 1
    divisor = 2

    for i in range(num_iteraciones):
        termino = 4/(divisor * (divisor + 1) * (divisor + 2)) * signo
    pi += termino
    signo = -signo
    divisor += 2

    print("La aproximación de pi con", num_iteraciones, "iteraciones es:", pi)





















