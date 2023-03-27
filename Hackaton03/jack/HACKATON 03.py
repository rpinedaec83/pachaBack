num = int(input("Ingrese un número: ")) 

if num >= 100 and num <= 999: 
    print("El número", num, "tiene tres dígitos.")
else:
    print("El número", num, "no tiene tres dígitos.")


    #ejercicio 2
num = int(input("ingresa un número: ")) 
if num < 0:
 print("el numero", num, "es negativo ")
else:
 print("el numero ", num, "no es negativo")

#ejercicio 3

num = int(input("ingresa un numero: "))

if num % 10 ==4: 
   print("El numero", num, "termina en 4")
else: 
   print("El numero", num,  "no termina en 4")
 

 #ejercicio 4
num = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
num3 = int(input("ingrese un numero: "))

ordenados = sorted([ num, num2, num3])
print("Los numeros de menor a mayor son: ", ordenados[0 ], ordenados[1], ordenados[2])

#ejercicio 5

precio = 80 # precio de cada zapato
cantidad = int(input("Ingrese la cantidad de zapatos a comprar: ")) 
if cantidad > 30: 
    descuento = 0.4
elif cantidad > 20: 
    descuento = 0.2 
elif cantidad > 10: 
    descuento = 0.1 
else: 
    descuento = 0 

total = cantidad * precio * (1 - descuento) 
print("El total a pagar es:", total) 

#ejercicio 6 
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: ")) 
if horas_trabajadas <= 40:
    sueldo_semanal = horas_trabajadas * 20 
else: 
    sueldo_base = 40 * 20
    horas_extra = horas_trabajadas - 40 
    sueldo_extra = horas_extra * 25 
    sueldo_semanal = sueldo_base + sueldo_extra 
print("El sueldo semanal del trabajador es: $", sueldo_semanal) 

#ejercicio 7
precio_helado = 50  
tipo_membresia = input("Ingrese el tipo de membresía (A, B o C): ") 

if tipo_membresia == "A": 
    descuento = 0.1 
elif tipo_membresia == "B": 
    descuento = 0.15 
elif tipo_membresia == "C": 
    descuento = 0.2 
else: 
    descuento = 0 
    print("Tipo de membresía no válido. No se otorga descuento.")

precio_final = precio_helado * (1 - descuento)
print("El precio final del helado es: $", precio_final)

#ejercicio 8
num1 =int(input("primera nota: "))
num2 =int(input("segunda nota: "))
num3 =int(input("tercera nota: "))

promedio= (num1 + num2 + num3)/3 

if promedio> 10: 
   print("Usted a aprobado con: ", promedio)
else: 
   print("Usted a desaprobado con: ", promedio)
#ejercicio 9
salario_actual = float(input("Ingrese el salario actual: "))

if salario_actual > 2000:
    aumento = salario_actual * 0.05
else:
    aumento = salario_actual * 0.1

nuevo_salario = salario_actual + aumento

print(f"El aumento de sueldo es de: ${aumento:.2f}")
print(f"El nuevo salario es de: ${nuevo_salario:.2f}")

#ejercicio 10 
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#ejercicio 11
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 > num2 and num1 > num3:
    print(num1, "es el mayor")
elif num2 > num1 and num2 > num3:
    print(num2, "es el mayor")
else:
    print(num3, "es el mayor")

#ejercicio 12
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero2 > numero1:
    print(f"El número {numero2} es mayor que {numero1}.")
else:
    print("Los dos números son iguales.")

#ejercicio 13
letra = input("Introduce una letra: ")

if letra in ['a', 'e', 'i', 'o', 'u']:
    print("La letra introducida es una vocal")
else:
    print("La letra introducida no es una vocal")

#ejercicio 14
numero = int(input("Ingrese un número entero positivo del 1 al diez y al 9: "))

es_primo = True
if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

#ejercicio 15
CM_TO_INCH = 0.393701
LB_TO_KG = 0.453592

cm = float(input("Introduce la cantidad en centímetros: "))
lb = float(input("Introduce la cantidad en libras: "))

inch = cm * CM_TO_INCH
print(cm, "centímetros equivalen a", inch, "pulgadas")

kg = lb * LB_TO_KG
print(lb, "libras equivalen a", kg, "kilogramos")

#ejercicio 16
numero = int(input("Ingresa un número del 1 al 7: "))

if numero == 1:
    dia = "lunes"
elif numero == 2:
    dia = "martes"
elif numero == 3:
    dia = "miércoles"
elif numero == 4:
    dia = "jueves"
elif numero == 5:
    dia = "viernes"
elif numero == 6:
    dia = "sábado"
elif numero == 7:
    dia = "domingo"
else:
    dia = "Día inválido"

print(f"El número {numero} corresponde al día {dia}.")

#ejercicio 17
hora = input("Introduce la hora en formato hh:mm:ss: ")

hora, minuto, segundo = hora.split(":")

hora = int(hora)
minuto = int(minuto)
segundo = int(segundo)

segundo += 1

if segundo == 60:
    segundo = 0
    minuto += 1

if minuto == 60:
    minuto = 0
    hora += 1

if hora == 24:
    hora = 0

hora = str(hora).zfill(2)  
minuto = str(minuto).zfill(2)
segundo = str(segundo).zfill(2)

print("La hora dentro de un segundo es:", hora + ":" + minuto + ":" + segundo)

#ejercicio 18
unidades = int(input("Ingrese la cantidad de unidades a comprar: "))

if unidades < 1:
    print("Cantidad no válida.")
elif unidades < 10:
    precio = unidades * 10
    print("El precio total es de $", precio)
elif unidades < 100:
    precio = unidades * 8
    print("El precio total es de $", precio)
elif unidades < 500:
    precio = unidades * 7
    print("El precio total es de $", precio)
else:
    precio = unidades * 6
    print("El precio total es de $", precio)

#ejercicio 19
salarios = {56: 56, 64: 64, 80: 80, 48: 48}

empleado = int(input("Ingrese el número identificador del empleado: "))
dias_trabajados = int(input("Ingrese la cantidad de días trabajados en la semana: "))

salario_semanal = salarios.get(empleado) * dias_trabajados

print("El empleado con el número identificador", empleado, "trabajó", dias_trabajados, "días y su salario semanal es de $", salario_semanal)

#ejercicio 20 
num1 = int(input("Introduce el primer número entero positivo: "))
num2 = int(input("Introduce el segundo número entero positivo: "))
num3 = int(input("Introduce el tercer número entero positivo: "))
num4 = int(input("Introduce el cuarto número entero positivo: "))

num_pares = 0
if num1 % 2 == 0:
    num_pares += 1
if num2 % 2 == 0:
    num_pares += 1
if num3 % 2 == 0:
    num_pares += 1
if num4 % 2 == 0:
    num_pares += 1
print("Hay", num_pares, "números pares.")


mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
if num4 > mayor:
    mayor = num4
print("El número mayor es:", mayor)

if num3 % 2 == 0:
    cuadrado = num2 ** 2
    print("El cuadrado del segundo número es:", cuadrado)

if num1 < num4:
    media = (num1 + num2 + num3 + num4) / 4
    print("La media de los cuatro números es:", media)

if num2 > num3 and num3 >= 50 and num3 <= 700:
    suma = num1 + num2 + num3 + num4
    print("La suma de los cuatro números es:", suma)
#ejercicio 21
num= int(input("Ingresa un numero: "))

if num < 0: 
    print("El numero debe ser positivo")
else: 
    factorial = 1
    for i in range(1, num+1): 
        factorial *=i 
        print(f"el factorial de", num, "es", factorial)


#ejercicio 22
n = int(input("Ingresa el valor de n: "))
suma = n * (n + 1) / 2
print("La suma de los primeros", n, "números es:", suma)

#ejercicio 23
n = int(input("Introduce un número entero positivo: "))
suma = 0

for i in range(1, n+1, 2):
    suma += i

print("La suma de los números impares menores o iguales a", n, "es:", suma)

#ejercicio 24
suma = 0

for i in range(2, 1001, 2):
    suma += i

print("La suma de los números pares hasta 1000 es:", suma)

#ejercicio 25
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#ejercicio 26 
def restas_sucesivas(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    resto = dividendo
    return cociente, resto
#ejercicio 27
numeros = []
while True:
    num = float(input("Ingrese un número positivo (ingrese un número negativo para terminar): "))
    if num < 0:
        break
    numeros.append(num)

if len(numeros) == 0:
    print("No se ingresaron números positivos.")
else:
    media = sum(numeros) / len(numeros)
    print("La media de los números ingresados es:", media)

#ejercicio 28

suma = 0 

for i in  range(1, 101): 
  suma +=1
print("la suma de los primeros cien numeros es: ", suma )

#ejercicio 29
i = 1
suma = 0 
while i <=100: 
    suma += i 
    i += 1 
print("La suma de los primeros cien numeros es:", suma)
#ejercicio 30 
i = 1 
suma = 0 

while True: 

    suma +=i 
    i += 1 
    if i > 100: 
        break 
    print("la suma de los primeros cien números es:", suma)

#ejercicio 31
numeros = []
num_pares = []
num_impares = []

for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)

media_pares = sum(num_pares) / len(num_pares)
media_impares = sum(num_impares) / len(num_impares)


print("La media de los números pares es:", media_pares)
print("La media de los números impares es:", media_impares)

#ejercicio 32
#ejercicio 33
while True: 
    respuesta = input("Quieres continuar aquí? s/n" )
    if respuesta.lower() =="n":
        break
#ejercicio 34
for i in range(1, 10):
    for j in range(1,11):
        print(i, "x", j, "=", i*j)
        print()
#ejercicio 35
numero_mayor = int(input("Ingresa un número: "))
numero_menor = numero_mayor

for i in range(19):
    numero = int(input("Ingresa otro número: "))
    if numero > numero_mayor:
        numero_mayor = numero
    if numero < numero_menor:
        numero_menor = numero

print("El número mayor es:", numero_mayor)
print("El número menor es:", numero_menor)

#ejercicio 36
n = int(input("Ingrese el número hasta el que desea calcular la serie de Fibonacci: "))

a = 0
b = 1

while b <= n:
    print(b)
    a, b = b, a+b

#ejercicio 37
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

print("El M.C.D de los dos números es:", num1)

#ejercicio 38 
numero = int(input("Ingrese un número: "))

suma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print(numero, "es un número perfecto")
else:
    print(numero, "no es un número perfecto")

#ejercicio 39
n = int(input("Ingrese el número de términos a sumar: "))

pi = 0
signo = 1

for i in range(n):
    termino = 4 / (2*i + 1)
    pi += signo * termino
    signo *= -1

print("La aproximación de Pi es:", pi)


#ejercicio 40 
n = int(input("Ingrese el número de términos a sumar: "))

pi = 3

denominador = 2

for i in range(n):
    termino = 4 / (denominador * (denominador + 1) * (denominador + 2))
    pi += ((-1) ** i) * termino
    denominador += 2

pi *= 4

print("La aproximación de Pi es:", pi)
