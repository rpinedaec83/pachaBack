import itertools
def ejercicio01():
    #Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos.
    numero = input("Ingresa un numero: ")
    if (len(numero) == 3):
        print (f"El numero {numero} tiene 3 digitos.")
    else:
        print(f"El numero {numero} no tiene 3 digitos. Tiene {len(numero)} digitos.")

def ejercicio02():
    #Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    numero = int(input("Ingresa un numero: "))
    if (numero < 0):
        print (f"El numero {numero} es negativo.")
    else:
        print (f"El numero {numero} es positivo.")

def ejercicio03():
    #Hacer un programa en Python que lea un número y determinar si termina en 4.
    numero = int(input("Ingresa un numero: "))
    if (numero%10==4):
        print(f"El numero {numero} termina en 4")
    else:
        print(f"El numero {numero} no termina en 4")

def ejercicio04():
    #Hacer un programa en Python que lea tres números enteros y los muestre de menor a mayor.
    numero1 = int(input("Ingresa un numero: "))
    numero2 = int(input("Ingresa otro numero: "))
    numero3 = int(input("Ingresa un ultimo numero: "))

    #Compara los numeros para ver cual es el menor
    if (numero1 < numero2 and numero1 < numero3):
        print(f"El menor es {numero1}")
    elif(numero2 < numero1 and numero2 < numero3):
        print(f"El menor es {numero2}")
    else:
        print(f"El menor es {numero3}")
    #Compara los numero para ver cual es el del medio
    if (numero1 < numero2 and numero1 > numero3):
        print(f"El del medio es {numero1}")
    elif (numero2 > numero1 and numero2 < numero3):
        print(f"El del medio es {numero2}")
    else:
        print(f"El del medio es {numero3}")
    #Compara los numero para ver cual es el mayor
    if (numero1 > numero2 and numero1 > numero3):
        print(f"El mayor es {numero1}")
    elif (numero2 > numero1 and numero2 > numero3):
        print(f"El mayor es {numero2}")
    else:
        print(f"El mayor es {numero3}")

def ejercicio05():
    #Hacer un programa en Python para una tienda de zapatos que tiene una promoción de descuento para vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.
    nroZapatos = int(input("Ingresa un cantidad de zapatos a comprar: "))
    if (nroZapatos < 10):
        totalAPagar = nroZapatos * 80
        print("No hay descuento")
        print(f"Total a Pagar: $ {totalAPagar}")
    elif (nroZapatos >=10 and nroZapatos < 20):
        totalAPagar = nroZapatos * 80
        print("Descuento de 10%")
        print(f"Total a Pagar: $ {totalAPagar - (totalAPagar * 0.10)}")
    elif (nroZapatos >=20 and nroZapatos < 30):
        totalAPagar = nroZapatos * 80
        print("Descuento de 20%")
        print(f"Total a Pagar: $ {totalAPagar - (totalAPagar * 0.20)}")
    else:
        totalAPagar = nroZapatos * 80
        print("Descuento de 40%")
        print(f"Total a Pagar: $ {totalAPagar - (totalAPagar * 0.40)}")

def ejercicio06():
    #Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
    horasTrabajadas = int(input("Ingrese Cantidad de Horas Trabajadas: "))
    if (horasTrabajadas < 40):
        sueldoSemana = horasTrabajadas * 20
    else:
        sueldoSemana = 40 * 20 + (horasTrabajadas - 40) * 25
    
    print(f"Sueldo de la Semana: $ {sueldoSemana}")

def ejercicio07():
    #Hacer un programa en Python para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
    #Tipo A 10% de descuento Tipo B 15% de descuento Tipo C 20% de descuento
    cantHelado = int(input("Ingrese Cantidad de Helados a Comprar: "))
    precioUnitario = int(input("Ingrese Precio Unitario: $"))
    precioTotal = cantHelado * precioUnitario
    tipoMembresia = input("Ingrese Tipo de Membresia: ")

    if (tipoMembresia == 'A' or tipoMembresia == 'a'):
        precioTotal = precioTotal - (precioTotal * 0.10)
        print(f"Total a Pagar: ${precioTotal}")
        print(("Descuento 10%"))
    elif (tipoMembresia == 'B' or tipoMembresia == 'b'):
        precioTotal = precioTotal - (precioTotal * 0.15)
        print(f"Total a Pagar: ${precioTotal}")
        print(("Descuento 15%"))
    elif (tipoMembresia == 'C' or tipoMembresia == 'c'):
        precioTotal = precioTotal - (precioTotal * 0.20)
        print(f"Total a Pagar: ${precioTotal}")
        print(("Descuento 20%"))
    else:
        print("Tipo de Membresia Equivocada")

def ejercicio08():
    #Hacer un programa en Python para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
    nota1 = int(input("Ingrese Nota1: "))
    nota2 = int(input("Ingrese Nota2: "))
    nota3 = int(input("Ingrese Nota3: "))

    promedio = (nota1 + nota2 + nota3) / 3

    if (promedio > 14):
        print(f"Promedio: {promedio}")
        print("Alumno Aprobado")
    else:
        print(f"Promedio: {promedio}")
        print("Alumno No Aprobado")

def ejercicio09():
    #Hacer un programa en Python para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.
    sueldo = int(input("Ingrese Sueldo: "))

    if(sueldo > 2000):
        sueldoAumento = sueldo + (sueldo * 0.05)
        print(f"Sueldo con Aumento: ${sueldoAumento}")
        print("Aumento 5%")
    else:
        sueldoAumento = sueldo + (sueldo * 0.10)
        print(f"Sueldo con Aumento: ${sueldoAumento}")
        print("Aumento 10%")

def ejercicio10():
    #Hacer un programa en Python que diga si un número es par o impar.

    numero = int(input("Ingrese un numero: "))

    if(numero %2 == 0):
        print(f"El numero {numero} es Par")
    else:
        print(f"El numero {numero} es Impar")

def ejercicio11():
    #Hacer un programa en Python que lea tres números y diga cuál es el mayor.
    numero1 = int(input("Ingresa un numero: "))
    numero2 = int(input("Ingresa otro numero: "))
    numero3 = int(input("Ingresa un ultimo numero: "))

    if (numero1 > numero2 and numero1 > numero3):
        print(f"El mayor es {numero1}")
    elif (numero2 > numero1 and numero2 > numero3):
        print(f"El mayor es {numero2}")
    else:
        print(f"El mayor es {numero3}")

def ejercicio12():
    #Hacer un programa en Python que lea dos números y diga cuál es el mayor.

    numero1 = int(input("Ingresa un numero: "))
    numero2 = int(input("Ingresa otro numero: "))

    if(numero1 > numero2):
        print(f"El mayor es: {numero1}")
    else:
        print(f"El mayor es: {numero2}")

def ejercicio13():
    #Hacer un programa en Python que lea una letra y diga si es una vocal.

    letra = input("Ingrese una letra: ")

    if (letra == "a" or letra == "A"):
        print(f"La letra {letra} es vocal")
    elif (letra == "e" or letra == "E"):
        print(f"La letra {letra} es vocal")
    elif (letra == "i" or letra == "I"):
        print(f"La letra {letra} es vocal")
    elif (letra == "o" or letra == "O"):
        print(f"La letra {letra} es vocal")
    elif (letra == "u" or letra == "U"):
        print(f"La letra {letra} es vocal")
    else:
        print(f"La letra {letra} no es vocal")

def ejercicio14():
    #Hacer un programa en Python que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo.

    numero = int(input("Ingrese un numero: "))
    x = 1
    contador = 0

    while (x <= numero):
        if (numero % x == 0):
            contador = contador + 1
        x = x + 1

    if (contador == 2 or numero == 1):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

def ejercicio15():
    #Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos.

    numero = int(input("Ingrese un numero a convertir en cms a Pulgadas y Libras a Kg: "))

    print("Centimetros a Pulgadas")
    pulgadas = numero / 2.54
    print(f"Centimetros: {numero}")
    print(f"Pulgadas: {pulgadas}")
    print("-------------------------")
    print("Libras a Kilogramos")
    kilogramos = numero * 0.45359237
    print(f"Libras: {numero}")
    print(f"Kilogramos: {kilogramos}")

def ejercicio16():
    #Hacer un programa en Python que lea un número y según ese número, indique el día que corresponde.

    dia = int(input("Ingrese un numero para devolver un dia correspondiante: "))

    if(dia == 1):
        print(f"El numero {dia} corresponde al dia Lunes")
    elif(dia == 2):
        print(f"El numero {dia} corresponde al dia Martes")
    elif(dia == 3):
        print(f"El numero {dia} corresponde al dia Miercoles")
    elif(dia == 4):
        print(f"El numero {dia} corresponde al dia Jueves")
    elif(dia == 5):
        print(f"El numero {dia} corresponde al dia Viernes")
    elif(dia == 6):
        print(f"El numero {dia} corresponde al dia Sabado")
    elif(dia == 7):
        print(f"El numero {dia} corresponde al dia Domingo")
    else:
        print(f"El numero {dia} no corresponde a ningun dia")

def ejercicio17():
    #Hacer un programa en Python donde se ingrese una hora y nos calcule la hora dentro de un segundo.
    hora = int(input("Ingrese Hora: "))
    minuto = int(input("Ingrese Minutos: "))
    segundo = int(input("Ingrese Segundos: "))

    if(hora < 24 and minuto < 60 and segundo < 60):
        segundo = segundo + 1
        if (segundo == 60):
            segundo = 0
            minuto = minuto + 1
            if (minuto == 60):
                minuto = 0
                hora = hora + 1
                if (hora == 24):
                    hora = 0
    
    print(f"{hora} : {minuto} : {segundo}")

def ejercicio18():
    #Hacer un programa en Python para una empresa se encarga de la venta y distribución de CD vírgenes. Los clientes pueden adquirir los artículos (supongamos un único producto de una única marca) por cantidad. Los precios son:
    #$10. Si se compran unidades separadas hasta 9.
    #$8. Si se compran entre 10 unidades hasta 99
    #$7. Entre 100 y 499 unidades.
    #$6. Para mas de 500 unidades.
    #La ganancia para el vendedor es de 8,25 % de la venta. Realizar un algoritmo en Pseint que dado un número de CDs a vender calcule el precio total para el cliente y la ganancia para el vendedor.

    cantCD = int(input("Ingrese Cantidad de CD a Comprar: "))

    if (cantCD < 10):
        print("Precio Unitario: $10")
        totalAPagar = cantCD * 10
        gananciaVendedor = totalAPagar * 0.0825
        print(f"Total a Pagar: ${totalAPagar}")
        print(f"Ganancia Vendedor: ${gananciaVendedor}")
    elif (cantCD >= 10 and cantCD < 100):
        print("Precio Unitario: $8")
        totalAPagar = cantCD * 8
        gananciaVendedor = totalAPagar * 0.0825
        print(f"Total a Pagar: ${totalAPagar}")
        print(f"Ganancia Vendedor: ${gananciaVendedor}")
    elif (cantCD >= 100 and cantCD < 500):
        print("Precio Unitario: $7")
        totalAPagar = cantCD * 7
        gananciaVendedor = totalAPagar * 0.0825
        print(f"Total a Pagar: ${totalAPagar}")
        print(f"Ganancia Vendedor: ${gananciaVendedor}")
    else:
        print("Precio Unitario: $6")
        totalAPagar = cantCD * 6
        gananciaVendedor = totalAPagar * 0.0825
        print(f"Total a Pagar: ${totalAPagar}")
        print(f"Ganancia Vendedor: ${gananciaVendedor}")

def ejercicio19():
    #Hacer un programa en Python para una heladería se tienen 4 tipos de empleados ordenados de la siguiente forma con su número identificador y salario diario correspondiente:
    #Cajero (56$/día).
    #Servidor (64$/día).
    #Preparador de mezclas (80$/día).
    #Mantenimiento (48$/día).
    # El dueño de la tienda desea tener un programa donde sólo ingrese dos números enteros que representen al número identificador del empleado y la cantidad de días que trabajó en la semana (6 días máximos). Y el programa le mostrará por pantalla la cantidad de dinero que el dueño le debe pagar al empleado que ingresó

    def calculoSueldo(sueldoHs):
        diasTrabajados = int(input("Dias Trabajados (Max 6): "))
        sueldoSemanal = diasTrabajados * sueldoHs
        mensaje = print(f"El empleado {nroIdentificadorEmpleado} recibe esta semana ${sueldoSemanal}")
        return mensaje

    nroIdentificadorEmpleado = int(input("Ingrese el Numero de Identificador de Empleado [1- Cajero, 2- Servidor, 3- Preparador de Mezclas, 4- Mantenimiento]: "))
    if (nroIdentificadorEmpleado == 1):
        sueldoSemanal = calculoSueldo(56)
    elif (nroIdentificadorEmpleado == 2):        
        sueldoSemanal = calculoSueldo(64)
    elif (nroIdentificadorEmpleado == 3):
        sueldoSemanal = calculoSueldo(80)
    elif (nroIdentificadorEmpleado == 4):
        sueldoSemanal = calculoSueldo(48)
    else:
        print("No corresponde a un Identificador de Empleado")

def ejercicio20():
    #Hacer un programa en Python que que lea 4 números enteros positivos y verifique y realice las siguientes operaciones:
    #¿Cuántos números son Pares?
    #¿Cuál es el mayor de todos?
    #Si el tercero es par, calcular el cuadrado del segundo.
    #Si el primero es menor que el cuarto, calcular la media de los 4 números.
    #Si el segundo es mayor que el tercero, verificar si el tercero esta comprendido entre los valores 50 y 700. Si cumple se cumple la segunda condición, calcular la suma de los 4 números.

    numero1 = int(input("Ingrese el Primer Numero: "))
    numero2 = int(input("Ingrese el Segundo Numero: "))
    numero3 = int(input("Ingrese el Tercer Numero: "))
    numero4 = int(input("Ingrese el Cuarto Numero: "))
    #contador = 0

    def contandoPares(numero):
        contador = 0
        if (numero % 2 == 0):
            contador = contador + 1
        return contador

    print("Contando Pares")
    contadorTotal = contandoPares(numero1) + contandoPares(numero2) + contandoPares(numero3) + contandoPares(numero4)
    print(f"Hay {contadorTotal} pares")

    if (numero1 > numero2 and numero1 > numero3 and numero1 > numero4):
        print(f"El mayor es el {numero1}")
    elif (numero2 > numero1 and numero2 > numero3 and numero2 > numero4):
        print(f"El mayor es el {numero2}")
    elif (numero3 > numero1 and numero3 > numero2 and numero3 > numero4):
        print(f"El mayor es el {numero3}")
    else:
        print(f"El mayor es el {numero4}")

    if(numero3 % 2 == 0):
        print(f"Como el 3ero es par, el cuadrado del 2do es: {numero2 * numero2}")
    if(numero1 < numero4):
        print(f"Como el 1ero es menor que el 4to, la media de los cuatro es: {(numero1 + numero2 + numero3 + numero4) / 4}")
    if(numero2 > numero3):
        if(numero3 > 49 and numero3 < 700):
            print(f"Como el 2do es Mayor que el 3ero y el 3ro esta entre el 50 y el 700, la suma de los cuatro es:  {(numero1 + numero2 + numero3 + numero4)}")

def ejercicio21():
    #Hacer un programa en Python que permita calcular el factorial de un número.
    
    numero = int(input("Ingrese un numero: "))

    def factorial(numero):
        if(numero == 0 or numero == 1):
            resultado = 1
        elif (numero > 1):
            resultado = numero * factorial(numero - 1)
        return resultado

    resultado = factorial(numero)

    print(f"El factorial de {numero} es {resultado}")

def ejercicio22():
    #Hacer un programa en Python para calcular la suma de los n primeros números.
    suma = 0
    numero = int(input("Ingrese un numero: "))
    for i in range(1, numero+1, 1):
        suma = suma + i

    print(f"La suma de los numeros hasta {numero} es {suma}" )

def ejercicio23():
    #Hacer un programa en Python para calcular la suma de los números impares menores o iguales a n.
    suma = 0
    numero = int(input("Ingrese un numero: "))
    for i in range(1, numero + 1, 1):
        if(i % 2 != 0):
            suma = suma + i
    
    print(f"La suma de los numeros impares hasta {numero} es {suma}" )

def ejercicio24():
    #Hacer un programa en Python para realizar la suma de todos los números pares hasta el 1000.

    suma = 0
    for i in range(1, 1001, 1):
        if(i % 2 == 0):
            suma = suma + i
    
    print(f"La suma de los numeros impares hasta 1000 es {suma}" )

def ejercicio25():
    #Hacer un programa en Python para calcular el factorial de un número de una forma distinta.
    factorial = 0
    numero = int(input("Ingrese un numero: "))

    if(numero < 0):
        print(f"El numero {numero} no se puede calcular")
    else:
        x = 1
        factorial = 1
        while (x < numero+1):
            factorial = factorial * x
            x = x + 1

    print(f"El factoral de {numero} es {factorial}")

def ejercicio26():
    #Hacer un programa en Python para calcular el resto y cociente por medio de restas sucesivas.
    cociente = 0
    numero1 = int(input("Ingrese el Primer Numero: "))
    numero2 = int(input("Ingrese el Segundo Numero: "))

    while (numero1 >= numero2):
        numero1 = numero1 - numero2
        cociente = cociente + 1
    
    print(f"El cociente es {cociente}")
    print(f"El resto es {numero1}")

def ejercicio27():
    #Hacer un programa en Python para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número negativo.

    lista = []
    suma = 0
    numero = int(input("Ingrese un numero positivo "))

    while(numero > 0):
        lista.append(numero)
        numero = int(input("Ingrese un numero positivo "))

    for numero in lista:
        suma = suma + numero

    print(f"Suma de la lista de numero positivos: {suma}")

def ejercicio28():
    #Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo repetir.

    numero = 100
    valor = 1
    suma = 0

    for num in itertools.repeat(valor, numero):
        suma = suma + valor
        valor = valor + 1

    print(f"La suma de los primeros cien numeros es {suma}")

def ejercicio29():
    #Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo mientras.
    suma = 0
    x = 1

    while (x < 101):
        suma = suma + x
        x = x + 1
   
    print(f"La suma de los primeros cien numeros es {suma}")
    
def ejercicio30():
    #Hacer un programa en Python para calcular la suma de los primeros cien números con un ciclo para.
    suma = 0

    for i in range (1, 101, 1):
        suma = suma + i
    
    print(f"La suma de los primeros cien numeros es {suma}")

def ejercicio31():
    #Hacer un programa en Python parar calcular la media de los números pares e impares, sólo se ingresará diez números.

    contador = 0
    contadorPar = 0
    contadorImpar = 0
    sumaPares = 0
    sumaImpares = 0
    
    while (contador < 10):
        numero = int(input("Ingresar numero: "))
        if (numero != 0):
            if (numero % 2 == 0):
                contadorPar = contadorPar + 1
                sumaPares = sumaPares + numero
            else:
                contadorImpar = contadorImpar + 1
                sumaImpares = sumaImpares + numero
        contador = contador + 1
    
    print(f"La Suma de los Numeros Pares es: {sumaPares}")
    print(f"Cantidad de Numeros Pares es: {contadorPar}")
    print(f"El Promedio de Numeros Pares es: {sumaPares/contadorPar}")
    print(f"---------------------------------------------")
    print(f"La suma de Los Numeros Impares es: {sumaImpares}")
    print(f"Cantidad de Numeros Impares es: {contadorImpar}")
    print(f"El Promedio de Numeros Impares es: {sumaImpares/contadorImpar}")

def ejercicio32():
    #Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, Hacer un programa en Python que nos permita saber eso. Datos de Lambayeque, Lima, Loreto
    contadorCiudad = 0
    contadorProv = 1
    ciudad = 0
    mayorPoblacion = 0

    while(contadorProv <= 3):
        mayorPoblacion = 0
        contadorCiudad = 1
        print(f"Provincia {contadorProv}")
        while (contadorCiudad <= 11):
            ciudad = int(input("Habitantes de ciudad: "))
            if(ciudad > mayorPoblacion):
                mayorPoblacion = ciudad
            contadorCiudad = contadorCiudad + 1
        print(f"La poblacion mayor de la provincia {contadorProv} es {mayorPoblacion}")
        contadorProv = contadorProv + 1

def ejercicio33():
    #Hacer un programa en Python que permita al usuario continuar con el programa.
    respuesta = "x"

    while (respuesta != "n"):
        respuesta = input("Ingrese si->s, no->n ")
        if(respuesta == "s"):
            print("El programa se continua ejecutando")
        else:
            print("El programa se va a cerrar")
            break

def ejercicio34():
    #Hacer un programa en Python que imprima la tabla de multiplicar de los números del uno nueve.
    i = 1
    for i in range(i, 11, 1):
        print(f"9 * {i} = {9 * i}")

def ejercicio35():
    #Hacer un programa en Python que nos permita saber cuál es el número mayor y menor, se debe ingresar sólo veinte números.
    contador = 0
    numeroMayor = 0
    numeroMenor = 999999

    while (contador != 21):
        numero = int(input("Escribir un numero: "))
        if (numero < numeroMenor):
            numeroMenor = numero
        if (numero > numeroMayor):
            numeroMayor = numero
        contador = contador + 1
    
    print(f"El Numero Menor es {numeroMenor}")
    print(f"El Numero Mayor es {numeroMayor}")

def ejercicio36():
    #Hacer un programa en Python para calcular la serie de Fibonacci.
    a = 0
    b = 1
    x = 1
    while(x <= 100):
        print(a)
        c = a + b
        a = b
        b = c
        x = x + 1

def ejercicio37():
    #Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
    a = 123922
    b = 870
    aux = 0
    print("Ingresar Dos Numeros")
    numero1 = int(input("Numero Uno "))
    numero2 = int(input("Numero Dos "))
    if (a < b):
        aux = a
        a = b
    while (b != 0):
        resto = a % b
        a = b
        b= resto
    print(f"Resultado Final: {a}")

def ejercicio38():
    #Hacer un programa en Python que nos permita saber si un número es un número perfecto.
    contador = 0
    cantidad = 0
    suma = 0
    resto = 0

    numero(int(input("Ingrese un numero ")))
    while (numero != contador):
        contador = contador + 1
        if (contador != numero):
            resto = numero % contador
            if (resto == 0):
                cantidad = cantidad + contador
        else:
            contador = numero
    print(f"Suma de los divisores: {cantidad}")
    if (numero == cantidad):
        print("Es perfecto")
    else:
        print("No es perfecto")

def ejercicio39():
    #Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es: Pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
    i = 0
    contador = 0
    pi = 0

    print("Ingrese un numero")
    numero = int(input("Para calcular la sucesion de pi"))
    for i in range (1, numero, 2):
        if(contador % 2 == 0):
            pi = pi + (4 / i)
        else:
            pi = pi - (4 / i)
    
    print(f"Pi se aproxima a: {pi}")

def ejercicio40():
    #Hacer un programa en Python que cumpla con la aproximación del número pi con la serie de Nilakantha. La formula que se debe aplicar es: Pi = = 3 + 4/(234) - 4/(456) + 4/(678) - 4/(8910) + 4/(101112) - 4/(121314) ...
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