def ejercicio01():
    #Hacer un programa en Python que lea un número por el teclado y determinar si tiene tres dígitos.
    num = input("Inserte numero para verificar si tiene 3 cifras: ")
    if(len(num) == 3):
        print("El numero ingresado es de 3 cifras")
    else:
        print("El numero ingresado no es de 3 cifras")

def ejercicio02():
    #Hacer un programa en Python que lea un número entero por el teclado y determinar si es negativo.
    num = int(input("Insgrese un numero para verificar si es negativo: "))
    if(num < 0):
        print("El numero negativo")
    else:
        print("El numero es positivo")

def ejercicio03():
    #Hacer un programa en Python que lea un número y determinar si termina en 4.
    print("Ingrese valor a evaluar:")
    n = int(input())
    if(n % 10 ==4):
        print ("El numero {n} , SI termina en 4")
    else: 
        print(f"el numero {n} no termina en 4")

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
    # Hacer un programa en Python para una tienda de zapatos que tiene una promoción de descuento para vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.
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
    # Hacer un programa en Python para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.
    horas_trabajadas = None

    while horas_trabajadas is None:
        try:
            horas_trabajadas = int(
                input("Ingrese las horas trabajadas: "))
            if horas_trabajadas > 0 and horas_trabajadas < 40:
                sueldo = horas_trabajadas * 20
            elif horas_trabajadas >= 40:
                horas_extras = horas_trabajadas - 40
                sueldo = 800 + (horas_extras * 25)
            else:
                print("solo numeros positivos")
                break
            print(f'El sueldo es {sueldo}')
        except ValueError:
            print("Solo numeros: ")

def ejercicio07():
    #Hacer un programa en Python para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes: Tipo A 10% de descuento Tipo B 15% de descuento Tipo C 20% de descuento
    

    membresiaCliente = input("Cual es la membresia del cliente(A,B,C)?")

    if(membresiaCliente == "A"):
        print(f"Tienes un descuento del 10%")
    elif(membresiaCliente == "B"):
        print(f"Tienes un descuento del 15%")
    elif(membresiaCliente == "C"):
        print(f"Tienes un descuento del 20%")
    else:
        print(f"Tipo de membresia incorrecta")

def ejercicio08():
    #Hacer un programa en Python para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.

    nota1 = float(input("Ingrese la primera nota"))
    nota2 = float(input("Ingrese la segunta nota"))
    nota3 = float(input("Ingrese la tercera nota"))
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de las notas es: {promedio}")
    if promedio >= 3:
        print("El estudiante aprobó.")
    else:
        print("El estudiante reprobó.")
	
def ejercicio09():
    #Hacer un programa en Python para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.

    salario_actual = float(input("Ingrese su salario actual: "))

    if salario_actual > 2000:
        aumento = 0.05
    else:
        aumento = 0.1

    salario_nuevo = salario_actual * (1 + aumento)

    print("Su nuevo salario es:", salario_nuevo)

def ejercicio10():
    #Hacer un programa en Python que diga si un número es par o impar.
    num = int(input("Numero para verificar si es par o impar? "))

    if(num%2==0):
        print("EL numero es par")
    else:
        print("el numero es impar")

    
def ejercicio11():
    #Hacer un programa en Python que lea tres números y diga cuál es el mayor.
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
    #Hacer un programa en Python que lea dos números y diga cuál es el mayor.
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num1 > num2:
        print("El mayor es:", num1)
    elif num2 > num1:
        print("El mayor es:", num2)
    else:
        print("Los dos números son iguales.")

def ejercicio13():
    #Hacer un programa en Python que lea una letra y diga si es una vocal.
    entrada = input(f"Ingresa un input para verificar si es una vocal: ")
    listaVocal = ["a", "b", "c", "d", "e"]
    
    for vocal in listaVocal:
        if(vocal == entrada.lower()):
            print("Es una vocal")

def ejercicio14():
    #Hacer un programa en Python que lea un entero positivo del 1 al diez y al 9 y determine si es un número primo.
    numero = int(input("Ingrese un número del 1 al 10: "))
    
    if numero in [1, 4, 6, 8, 9, 10]:
        print("El número no es primo.")
    elif numero in [2, 3, 5, 7]:
        print("El número es primo.")

    else:
        print("Ingresar un numero en el rango indicado: (1 al 10)")


def ejercicio15():
    #Hacer un programa en Python que convierta centímetros a pulgadas y libras a kilogramos.
    pulgadas = 0
    libra = 0
    centimetros = float(input("Ingresa el los centimetros por convertir a pulgadas: "))
    kilo = float(input("Ingresa el peso en kilogramos por convertir a libras: "))
        
    pulgadas = centimetros*0.393701
    libra = kilo*2.205

    print(f"La conversin de centimetros a pulgadas es: {pulgadas}")
    print(f"La conversin de kilogramos a libras es: {libra}")


def ejercicio16():
    #Hacer un programa en Python que lea un número y según ese número, indique el día que corresponde.

    day = float(input("Ingrese un numero del 1 al 7 para indicar el día: "))

    if day==1:
         print("El dia segun el numero ingresado es Lunes.")
    elif day==2:
        print("El dia segun el numero ingresado es Marte.")
    elif day==3:
        print("El dia segun el numero ingresado es Miercoles.")
    elif day==4:
        print("El dia segun el numero ingresado es Jueves.")
    elif day==5:
        print("El dia segun el numero ingresado es Viernes.")
    elif day==6:
        print("El dia segun el numero ingresado es Sabado.")
    elif day==7:
        print("El dia segun el numero ingresado es Domingo.")
    else:
        print("No existe, inserte un numero del 1 al 7")


def ejercicio17():
    #Hacer un programa en Python donde se ingrese una hora y nos calcule la hora dentro de un segundo.


    hora = int(input("Ingrese la hora: "))
    min = int(input("Ingrese la minuto: "))
    seg = int(input("Ingrese el segundo: "))

    seg += 1

    if(seg == 59):
        seg = 0
        min += 1
        if(min == 60):
            min = 0
            hora += 1

    print(f"Son las {hora}:{min}:{seg}")

def ejercicio18():
	#Hacer un algoritmo en Python para una empresa se encarga de la venta y distribucin de CD vrgenes. Los clientes pueden adquirir los artculos (supongamos un nico producto de una nica marca) por cantidad. Los precios son:")
	numerocds = 0
	preciototal = 0
	print("Numero de cds que comprara el cliente")
	numerocds = float(input())
	if numerocds<=9:
		preciototal = numerocds*10
	if numerocds>=10 and numerocds<=99:
		preciototal = numerocds*8
	if numerocds>=100 and numerocds<=499:
		preciototal = numerocds*7
	if numerocds>500:
		preciototal = numerocds*6
	print("Precio total del cliente: ",preciototal)
	print("Ganancia para el vendedor: ",preciototal*8.25/100)
        
def ejercicio19():
	#Hacer un algoritmo en Python para una heladera se tienen 4 tipos de empleados ordenados de la siguiente forma con su nmero identificador y salario diario correspondiente:
	input2 = int()
	tarifa = 0
	input2 = 0
	ind_input1 = False
	while ind_input1==False:
		print("Ingrese el tipo de empleado:")
		print("Digita 1 para Cajero (56$/da)")
		print("Digita 2 para Servidor (64$/da)")
		print("Digita 3 para Preparador de mezclas (80$/da)")
		print("Digita 4 para Mantenimiento (48$/da)")
		input1 = float(input())
		if input1==1:
			input1 = input1
			tarifa = 56
			ind_input1 = True
		elif input1==2:
			input1 = input1
			tarifa = 64
			ind_input1 = True
		elif input1==3:
			input1 = input1
			tarifa = 80
			ind_input1 = True
		elif input1==4:
			input1 = input1
			tarifa = 48
			ind_input1 = True
		else:
			print("Opcion No valida para tipo de empleado.")
			print("")
			ind_input1 = False
	ind_input2 = False
	while ind_input2==False:
		print("Ingrese cantidad de dias laborados:")
		input2 = int(input())
		if input2>0 and input2<7:
			input2 = input2
			ind_input2 = True
		else:
			print("La cantidad de dias no puede ser superior a 6 o igual a 0")
			print("")
			ind_input2 = False
	print("La cantidad a pagar al empleado es de : $/ ",tarifa*input2)
        
def ejercicio20():
	#Hacer un algoritmo en Python que que lea 4 nmeros enteros positivos y verifique y realice las siguientes operaciones:")

	regla_01 = False
	contador_pares = 0
	regla_02 = True
	numero_mayor = 0
	regla_03 = False
	cuadrado_segundo = 0
	regla_04 = False
	media = 0
	regla_05 = False
	suma_numeros = 0
	print("Ingrese 4 numeros enteros:")

	n1 = float(input("Primer numero: "))
	if n1%2==0:
		contador_pares = contador_pares+1
	if n1>numero_mayor:
		numero_mayor = n1

	n2 = float(input("Segundo numero: "))
	if n2%2==0:
		contador_pares = contador_pares+1
	if n2>numero_mayor:
		numero_mayor = n2

	n3 = float(input("Tercer numero: "))
	if n3%2==0:
		regla_03 = True
		contador_pares = contador_pares+1
		cuadrado_segundo = n2**2
	if n3>numero_mayor:
		numero_mayor = n3

	n4 = float(input("Cuardo numero: "))
	if n4%2==0:
		contador_pares = contador_pares+1
	if n4>numero_mayor:
		numero_mayor = n4
	if n1<n4:
		regla_04 = True
		media = (n1+n2+n3+n4)/4
	if n2>n3:
		if n3>50 and n3<700:
			regla_05 = True
			suma_numeros = (n1+n2+n3+n4)
	if contador_pares!=0:
		regla_01 = True
	if regla_01==True:
		print("La cantidad de numeros pares encontrados es : ",contador_pares)
	if regla_02==True:
		print("El numero mayor es : ",numero_mayor)
	if regla_03==True:
		print("El cuadrado del segundo numero es : ",cuadrado_segundo)
	if regla_04==True:
		print("La media aritmetica de los 4 numeros es: ",media)
	if regla_05==True:
		print("La suma de los 4 numeros es: ",suma_numeros)

def ejercicio21():
	#Hacer un algoritmo en Python que permita calcular el factorial de un nmero.
	num = int()
	contador = int()
	factorial = int()
	print("Digite un numero entero:")
	num = int(input())
	contador = 1
	factorial = 1
	for contador in range(1,num+1):
		factorial = factorial*contador
	print("El factorial del numero ingresado es: ",factorial)

def ejercicio22():
	#Hacer un algoritmo en Python para calcular la suma de los n primeros nmeros.
	ingreso = int()
	suma = 0
	contador = 1
	print("Ingrese un numero para sumar sus predecesores:")
	ingreso = int(input())
	for contador in range(1,(ingreso-1)+1):
		suma = suma+contador
	print("La suma de los predecesores es: ",suma)

def ejercicio23():
	#Hacer un algoritmo en Python para calcular la suma de los nmeros impares menores o iguales a n.

	numeroenteroingresado = float(input("Ingrese un numero entero positivo:"))
	count = 0
	for i in range(1,numeroenteroingresado+1,2):
		count = count+i
	print("La suma de los numeros es: ",count)
	
def ejercicio24():
	#Hacer un algoritmo en Python para realizar la suma de todos los nmeros pares hasta el 1000.
	count = 0
	i = 0
	while i<=1000:
		if i%2==0:
			count = count+i
		i = i+1
	print("La suma de los 1000 numeros pares es: ",count)

def ejercicio25():
	#Hacer un algoritmo en Python para calcular el factorial de un nmero de una forma distinta.
    numero = int()
    factorial = int()
    print("Brindame un numero y te doy el factorial")
    numero = int(input())
    if numero<0:
            print("El numero ",numero,"no se puede calcular")
    else:
            x = 1
            factorial = 1
            while True:# no hay 'repetir' en python
                factorial = factorial*x
                x = x+1
                if x>numero: break
            print(factorial)

def ejercicio26():
	#Hacer un algoritmo en Python para calcular el resto y cociente por medio de restas sucesivas.

	divisor = float(input("Ingrese el divisor: "))
	dividendo = float(input("Ingrese el dividendo: "))
	cociente = 0
	while divisor>=dividendo:
		divisor = divisor-dividendo
		cociente = cociente+1
	print("El cociente es: ",cociente)
	print("El resto es: ",divisor)

def ejercicio27():
	#Hacer un algoritmo en Python para determinar la media de una lista indefinida de nmeros positivos, se debe acabar el programa al ingresar un nmero positivo.
	x = 1
	suma = 0
	c = 0
	while x>=0:
		x = float(input("Ingresa cualquier numero positivo."))
		if x>=0:
			suma = suma+x
			c = c+1
	if c>0:
		print("La media es: ",suma/c)

def ejercicio28():
	#Hacer un algoritmo en Python para calcular la suma de los primeros cien nmeros con un ciclo repetir.
	count = 1
	suma = 0
	while True:# no hay 'repetir' en python
		suma = suma+count
		count = count+1
		if count==101: break
	print("(ciclo Repetir) La suma de 1 a 100 es : ",suma)

def ejercicio29():
	#Hacer un algoritmo en Python para calcular la suma de los primeros cien nmeros con un ciclo mientras.
	count = 1
	suma = 0
	while count<=100:
		suma = suma+count
		count = count+1
	print("(Ciclo Mientras) La suma de 1 a 100 es: ",suma)

def ejercicio30():
	#Hacer un algoritmo en Python para calcular la suma de los primeros cien nmeros con un ciclo para.
	suma = 0
	for i in range(1,101):
		suma = suma+i
	print("(Ciclo Para) La suma de 1 a 100 es : ",suma)

def ejercicio31():
	#Hacer un algoritmo en Python parar calcular la media de los nmeros pares e impares, slo se ingresar diez nmeros.
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
	#Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, Hacer un programa en Python que nos permita saber eso. Datos de Lambayeque, Lima, Loreto

    lima = 8575 #millones
    lambayeque = 1356202
    loreto = 1068132

    print("La poblacion con mayor poblacio es Lima")

def ejercicio33():
	#Hacer un algoritmo en Python que permita al usuario continuar con el programa.
	ingreso = ""
	while ingreso!="N" and ingreso!="n":
		print("Quieres continuar con el programa")
		print("(Any)Si")
		print("(N)No")
		ingreso = input()

def ejercicio34():
	#Hacer un algoritmo en Python que imprima la tabla de multiplicar de los nmeros del uno nueve.
	for i in range(10):
		print("Tabla de Multiplicacion del: ",i)
		for j in range(10):
			print(i," x ",j," = ",i*j)

def ejercicio35():
	#Hacer un algoritmo en Python que nos permita saber cul es el nmero mayor y menor, se debe ingresar slo veinte numeros.
	numeros_ingresados = [str() for ind0 in range(5)]
	for i in range(1,6):
		numeros_ingresados[i-1] = input()
	numeromayor = numeros_ingresados[0]
	numeromenor = numeros_ingresados[0]
	for i in range(1,6):
		if numeros_ingresados[i-1]>numeromayor:
			numeromayor = numeros_ingresados[i-1]
		if numeros_ingresados[i-1]<numeromenor:
			numeromenor = numeros_ingresados[i-1]
	print(numeromayor)
	print(numeromenor)

def ejercicio36():
	#Hacer un algoritmo en Python para calcular la serie de Fibonacci."
	numerodedigitosenserie = 0
	numeroacumulado = 0
	n_anterior = 0
	n_actual = 1

	numerodedigitosenserie = float(input("Cuantos terminos tendra la sucesion?"))
	if numerodedigitosenserie==1 or numerodedigitosenserie==2:
		print(1)
	else:
		for i in range(numerodedigitosenserie-1):
			numeroacumulado = n_anterior+n_actual
			n_anterior = n_actual
			n_actual = numeroacumulado
		print(numeroacumulado)

def mcdRecursivo(a, b):
	if a<b:
		mcd_ = mcdRecursivo(b,a)
	else:
		if b==0:
			mcd_ = a
		else:
			mcd_ = mcdRecursivo(b,a%b)
	return mcd_

def ejercicio37():
	#Hacer un programa en Python para conseguir el M.C.D de un número por medio del algoritmo de Euclides.
	print("Hacer un algoritmo en Pseint para conseguir el M.C.D de un nmero por medio del algoritmo de Euclides.")
	print("El M.C.D. entre 1 y 12 es: ",mcdRecursivo(1,12))




def ejercicio38():
	#Hacer un algoritmo en Python que nos permita saber si un nmero es un nmero perfecto.
	numeroperfecto_ = 0
	acumulador = 0
	print("Inserte numero para comprobar si es perfecto")
	numeroperfecto_ = float(input())
	for i in range(1,numeroperfecto_):
		if numeroperfecto_%i==0:
			acumulador = acumulador+i
			
	if numeroperfecto_==acumulador:
		print("Es un numero perfecto")
	else:
		print("No es un numero perfecto")

def ejercicio39():
	#Hacer un algoritmo en Python que cumpla con la aproximacin del nmero pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:
	i = 0
	iteraciones_max = int(input("Inserte # de iteraciones para aproximacion de pi "))
	pi_value = 0
	denominador = 1
	signo = 1
	while i<iteraciones_max:
		pi_value = pi_value+(4/denominador*signo)
		denominador = denominador+2
		signo = signo*(-1)
		i = i+1
	print(pi_value)

def ejercicio40():
	#Hacer un algoritmo en Python que cumpla con la aproximacin del nmero pi con la serie de Nilakantha. La formula que se debe aplicar es:
	i = 0
	iteraciones_max = int(input("Inserte # de iteraciones para aproximacion de pi "))
	pi_value = 3
	denominador = 2
	signo = 1
	

	while i<iteraciones_max:
		pi_value = pi_value+((4/(denominador*(denominador+1)*(denominador+2)))*signo)
		denominador = denominador+2
		signo = signo*(-1)
		i = i+1
	print(pi_value)