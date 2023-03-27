def ejercicio01():
    print('Ejercicio numero 1.')

def tarea_01():
	print("1. Encontrar digitos de un numero.")
	#input = int()
	print("")
	ingreso = int(input("Ingrese un numero para validar si tiene 3 digitos: "))
	input_fijo = ingreso
	contador_cociente_menor_igual_1 = 0
	while ingreso>=1:
		ingreso = int(ingreso/10)
		contador_cociente_menor_igual_1 = contador_cociente_menor_igual_1+1
	print("El numero ",input_fijo," tiene ",contador_cociente_menor_igual_1," digitos.")

def tarea_02():
	ingreso = int()
	print("2. Hacer un algoritmo en Pseint que lea un numero entero por el teclado y determinar si es negativo.")
	print("")
	print("Ingrese un numero para validar si es negativo: ")
	ingreso = int(input())
	if ingreso<0:
		print("El numero ",ingreso," es negativo")
	else:
		print("El numero ",ingreso," no es negativo")

def tarea_03():
	print("3. Hacer un algoritmo en Pseint que lea un numero y determinar si termina en 4.")
	ingreso = int()
	print("")
	print("Ingrese un numero para validar si termina en 4: ")
	ingreso = int(input())
	u = ingreso%10
	if u==4:
		print("El numero ",ingreso," si termina en 4.")
	else:
		print("El numero ",ingreso," no termina en 4.")

def tarea_04():
	print("4. Hacer un algoritmo en Pseint que lea tres numeros enteros y los muestre de menor a mayor.")
	n1 = int()
	n2 = int()
	n3 = int()
	print("Ingrese tres numeros:")
	n1 = int(input())
	n2 = int(input())
	n3 = int(input())
	if (n1<n2 and n1<n3):
		if (n2<n3):
			print(n1," ",n2," ",n3)
		else:
			print(n1," ",n3," ",n2)
	if (n2<n1 and n2<n3):
		if (n1<n3):
			print(n2," ",n1," ",n3)
		else:
			print(n2," ",n3," ",n1)
	if (n3<n1 and n3<n2):
		if (n1<n2):
			print(n3," ",n1," ",n2)
		else:
			print(n3," ",n2," ",n1)

def tarea_05():
	print("5.Hacer un algoritmo en Pseint para una tienda de zapatos que tiene una promocion de descuento para vender al mayor, esta dependera del numero de zapatos que se compren. Si son mas de diez, se les dara un 10 porciento de descuento sobre el total de la compra; si el numero de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20 porciento de descuento; y si son ms treinta zapatos se otorgar un 40 porciento de descuento. El precio de cada zapato es de $80.")
	nrozapatos = int()
	precio = int()
	precio = 0
	print("Cantidad de Zapatos a comprar:")
	nrozapatos = int(input())
	precio = nrozapatos*80
	if (nrozapatos<10):
		print("No se aplica descuento. El precio total a pagar es: ",precio)
	else:
		if (nrozapatos<20):
			print("Se aplica descuento. El precio total a pagar es: ",precio-(precio*0.1))
		else:
			if (nrozapatos<30):
				print(" Se aplica descuento. El precio total a pagar es: ",precio-(precio*0.2))
			else:
				print("Se aplica descuento. El precio total a pagar es: ",precio-(precio*0.4))

def tarea_06():
	print("6. Hacer un algoritmo en Pseint para ayudar a un trabajador a saber cual sera su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagar $20 por hora, pero si trabaja ms de 40 horas entonces las horas extras se le pagarn a $25 por hora.")
	horastrab = int()
	sueldo = int()
	horasextra = int()
	horasextra = 0
	sueldo = 0
	print("Ingresar horas trabajadas:")
	horastrab = int(input())
	if (horastrab<40):
		sueldo = horastrab*20
		print("El sueldo que le corresponde esta semana es de: ",sueldo)
	else:
		horasextra = horastrab-40
		sueldo = (horastrab-horasextra)*20
		print("El sueldo que le corresponde esta semana es de: ",sueldo+(horasextra*25))

def tarea_07():
	print("7. Hacer un algoritmo en Pseint para una tienda de helado que da un descuento por compra a sus clientes con membresa dependiendo de su tipo, slo existen tres tipos de membresa, tipo A, tipo B y tipo C. Los descuentos son los siguientes:")
	compra = float()
	tipocliente = str()
	print("Ingresar el monto a comprar: ")
	compra = float(input())
	print("Ingresar el tipo de cliente: A, B, C ")
	tipocliente = input()
	if (tipocliente)=="A":
		print("Tipo de Cliente A")
		print("Total a pagar: ",(compra-(compra*0.10)))
	elif (tipocliente)=="B":
		print("Tipo de Cliente B")
		print("Total a pagar: ",compra-(compra*0.15))
	elif (tipocliente)=="C":
		print("Tipo de Cliente C")
		print("Total a pagar: ",compra-(compra*0.20))
	else:
		print("Total a pagar: ",compra)

def tarea_08():
	print("8. Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprob o no.")
	nota1 = float()
	nota2 = float()
	nota3 = float()
	promedio = float()
	promedio = 0
	print("Recuerda que la mnima nota aprobatoria es 12")
	print("Ingresar sus 3 notas:")
	nota1 = float(input())
	nota2 = float(input())
	nota3 = float(input())
	promedio = (nota1+nota2+nota3)/3
	if (promedio>=11.5):
		print(" Estudiante Aprobado")
	else:
		print("Estudiante Reprobado")

def tarea_09():
	print("9. Hacer un algoritmo en Pseint para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba ms de $2000 tendr un aumento del 5%, si generaba menos de $2000 su aumento ser de un 10%.")
	sueldo = float()
	print("Ingresar su sueldo anterior")
	sueldo = float(input())
	if (sueldo<2000):
		print("Su sueldo actual ser de: ",sueldo+(sueldo*0.1))
	else:
		print("Su sueldo actual ser de: ",sueldo+(sueldo*0.05))

def tarea_10():
	print("10. Hacer un algoritmo en Pseint que diga si un nmero es par o impar.")
	print("Ingrese un numero para evaluar si es par o impar: ")
	n1 = input()
	if n1%2==0:
		print("Este numero es par.")
	else:
		print("Este numero es impar.")

def tarea_11():
	print("11. Hacer un algoritmo en Pseint que lea tres nmeros y diga cul es el mayor.")
	n_mayor = 0
	print("Ingrese el primer numero: ")
	n1 = input()
	if n1>n_mayor:
		n_mayor = n1
	print("Ingrese el segundo numero: ")
	n2 = input()
	if n2>n_mayor:
		n_mayor = n2
	print("Ingrese el tercer numero: ")
	n3 = input()
	if n3>n_mayor:
		n_mayor = n3
	print("El numero mayor es : ",n_mayor)

def tarea_12():
	print("12. Hacer un algoritmo en Pseint que lea dos nmeros y diga cul es el mayor.")
	n_mayor = 0
	print("Ingrese el primer numero: ")
	n1 = input()
	if n1>n_mayor:
		n_mayor = n1
	print("Ingrese el segundo numero: ")
	n2 = input()
	if n2>n_mayor:
		n_mayor = n2
	print("El numero mayor es : ",n_mayor)

def tarea_13():
	print("13. Hacer un algoritmo en Pseint que lea una letra y diga si es una vocal.")
	print("Escriba una letra: ")
	letra = input()
	if str.lower(letra)=="a":
		print("La letra ",letra," es una vocal")
	elif str.lower(letra)=="e":
		print("La letra ",letra," es una vocal")
	elif str.lower(letra)=="i":
		print("La letra ",letra," es una vocal")
	elif str.lower(letra)=="o":
		print("La letra ",letra," es una vocal")
	elif str.lower(letra)=="u":
		print("La letra ",letra," es una vocal")
	else:
		print("La letra ",letra," no es una vocal")

def tarea_14():
	print("14. Hacer un algoritmo en Pseint que lea un entero positivo del 1 al diez y al 9 y determine si es un nmero primo.")
	print("Ingresa un nmero del 1 al 10")
	num = float(input())
	if (num<11 and num>0):
		if (num)==2:
			print("El nmero es primo")
		elif (num)==3:
			print("El nmero es primo")
		elif (num)==5:
			print("El nmero es primo")
		elif (num)==7:
			print("El nmero es primo")
		else:
			print("El nmero no es primo")
	else:
		print("No es un nmero del 1 al 10")

def tarea_15():
	print("15. Hacer un algoritmo en Pseint que convierta centmetros a pulgadas y libras a kilogramos.")
	centimetros = float()
	pulgadas = float()
	kilo = float()
	libra = float()
	print("Ingresa el los centimetros por convertir a pulgadas.")
	centimetros = float(input())
	print("Ingresa el peso en kilogramos por convertir a libras.")
	kilo = float(input())
	pulgadas = centimetros*0.393701
	libra = kilo*2.205
	print("La conversin de centimetros a pulgadas es: ",pulgadas)
	print("La conversin de kilogramos a libras es: ",libra)

def tarea_16():
	print("16. Hacer un algoritmo en Pseint que lea un nmero y segn ese nmero, indique el da que corresponde.")
	print("Ingrese un numero del 1 al 7.")
	code_dia = float(input())
	if code_dia==1:
		print("El dia equivalente al numero ingresado es Lunes.")
	elif code_dia==2:
		print("El dia equivalente al numero ingresado es Marte.")
	elif code_dia==3:
		print("El dia equivalente al numero ingresado es Miercoles.")
	elif code_dia==4:
		print("El dia equivalente al numero ingresado es Jueves.")
	elif code_dia==5:
		print("El dia equivalente al numero ingresado es Viernes.")
	elif code_dia==6:
		print("El dia equivalente al numero ingresado es Sabado.")
	elif code_dia==7:
		print("El dia equivalente al numero ingresado es Domingo.")
	else:
		print("No esiste codificacion para este numero.")

def tarea_17():
	print("17. Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro de un segundo.")
	hora_ = 0
	minutos_ = 0
	segundos_ = 0
	print("Escriba la horas: ", end="")
	hora = input()
	print("Escriba los minutos: ", end="")
	minutos_ = float(input())
	print("Escriba los segundos: ", end="")
	segundos_ = float(input())
	print("La hora dentro de un segundo sera: ",hora,":",minutos_,":",segundos_+1)

def tarea_18():
	print("18. Hacer un algoritmo en Pseint para una empresa se encarga de la venta y distribucin de CD vrgenes. Los clientes pueden adquirir los artculos (supongamos un nico producto de una nica marca) por cantidad. Los precios son:")
	numerocds = 0
	ganancia = 0
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

def tarea_19():
	print("19. Hacer un algoritmo en Pseint para una heladera se tienen 4 tipos de empleados ordenados de la siguiente forma con su nmero identificador y salario diario correspondiente:")
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

def tarea_20():
	print("20. Hacer un algoritmo en Pseint que que lea 4 nmeros enteros positivos y verifique y realice las siguientes operaciones:")
	print("")
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
	print("Primer numero: ")
	n1 = float(input())
	if n1%2==0:
		contador_pares = contador_pares+1
	if n1>numero_mayor:
		numero_mayor = n1
	print("Segundo numero: ")
	n2 = float(input())
	if n2%2==0:
		contador_pares = contador_pares+1
	if n2>numero_mayor:
		numero_mayor = n2
	print("Tercer numero: ")
	n3 = float(input())
	if n3%2==0:
		regla_03 = True
		contador_pares = contador_pares+1
		cuadrado_segundo = n2**2
	if n3>numero_mayor:
		numero_mayor = n3
	print("Cuardo numero: ")
	n4 = float(input())
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

def tarea_21():
	print("21. Hacer un algoritmo en Pseint que permita calcular el factorial de un nmero.")
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

def tarea_22():
	print("22. Hacer un algoritmo en Pseint para calcular la suma de los n primeros nmeros.")
	ingreso = int()
	suma = 0
	contador = 1
	print("Ingrese un numero para sumar sus predecesores:")
	ingreso = int(input())
	for contador in range(1,(ingreso-1)+1):
		suma = suma+contador
	print("La suma de los predecesores es: ",suma)

# RESULETO
def tarea_23():
	print("23. Hacer un algoritmo en Pseint para calcular la suma de los nmeros impares menores o iguales a n.")
	print("")
	print("Ingrese un numero entero positivo:")
	numeroenteroingresado = float(input())
	count = 0
	for i in range(1,numeroenteroingresado+1,2):
		count = count+i
	print("La suma de los numeros es: ",count)

# RESUELTO
def tarea_24():
	print("24. Hacer un algoritmo en Pseint para realizar la suma de todos los nmeros pares hasta el 1000.")
	count = 0
	i = 0
	while i<=1000:
		if i%2==0:
			count = count+i
		i = i+1
	print("La suma de los 1000 numeros pares es: ",count)

def tarea_25():
	print("25. Hacer un algoritmo en Pseint para calcular el factorial de un nmero de una forma distinta.")
	contador = 1
	factorial = 1
	print("Digite un numero para calcular su factorial")
	num = input()
	while contador<num:
		contador = contador+1
		factorial = factorial*contador
	print("El factorial de ",num," es ",factorial)

def tarea_26():
	print("26. Hacer un algoritmo en Pseint para calcular el resto y cociente por medio de restas sucesivas.")
	print("Ingrese el divisor:")
	divisor = float(input())
	print("Ingrese el dividendo:")
	dividendo = float(input())
	cociente = 0
	while divisor>=dividendo:
		divisor = divisor-dividendo
		cociente = cociente+1
	print("El cociente es: ",cociente)
	print("El resto es: ",divisor)

def tarea_27():
	print("27. Hacer un algoritmo en Pseint para determinar la media de una lista indefinida de nmeros positivos, se debe acabar el programa al ingresar un nmero positivo.")
	c = int()
	x = float()
	suma = float()
	x = 1
	suma = 0
	c = 0
	while x>=0:
		print("Ingresa cualquier numero positivo.")
		x = float(input())
		if x>=0:
			suma = suma+x
			c = c+1
	if c>0:
		print("La media es: ",suma/c)

def tarea_28():
	print("28. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien nmeros con un ciclo repetir.")
	count = 1
	suma = 0
	while True:# no hay 'repetir' en python
		suma = suma+count
		count = count+1
		if count==101: break
	print("(ciclo Repetir) La suma de 1 a 100 es : ",suma)

def tarea_29():
	print("29. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien nmeros con un ciclo mientras.")
	count = 1
	suma = 0
	while count<=100:
		suma = suma+count
		count = count+1
	print("(Ciclo Mientras) La suma de 1 a 100 es: ",suma)

def tarea_30():
	print("30. Hacer un algoritmo en Pseint para calcular la suma de los primeros cien nmeros con un ciclo para.")
	suma = 0
	for i in range(1,101):
		suma = suma+i
	print("(Ciclo Para) La suma de 1 a 100 es : ",suma)

def tarea_31():
	print("31. Hacer un algoritmo en Pseint parar calcular la media de los nmeros pares e impares, slo se ingresar diez nmeros.")
	array = [float() for ind0 in range(10)]
	numeroacumulado_par = 0
	pares = 0
	numeroacumulado_impar = 0
	impares = 0
	for i in range(1,11):
		array[i-1] = float(input())
		if array[i-1]%2==0:
			numeroacumulado_par = numeroacumulado_par+array[i-1]
			pares = pares+1
		else:
			numeroacumulado_impar = numeroacumulado_impar+array[i-1]
			impares = impares+1
	print("Media de pares: ",numeroacumulado_par/pares)
	print("Media de impares: ",numeroacumulado_impar/impares)

def tarea_32():
	print("32. Se quiere saber cul es la ciudad con la poblacin de ms personas, son tres provincias y once ciudades, hacer un algoritmo en Pseint que nos permita saber eso.")
	personasxciudad = [str() for ind0 in range(11)]
	ciudad_mas_habitantes = 0
	for i in range(1,12):
		personasxciudad[i-1] = input()
		if personasxciudad[i-1]>ciudad_mas_habitantes:
			ciudad_mas_habitantes = personasxciudad[i-1]
	print("La ciudad con mas habitantes tiene ",ciudad_mas_habitantes," habitantes")

def tarea_33():
	print("33. Hacer un algoritmo en Pseint que permita al usuario continuar con el programa.")
	ingreso = ""
	while ingreso!="N" and ingreso!="n":
		print("Quieres continuar con el programa")
		print("(Any)Si")
		print("(N)No")
		ingreso = input()

def tarea_34():
	print("34. Hacer un algoritmo en Pseint que imprima la tabla de multiplicar de los nmeros del uno nueve.")
	for i in range(10):
		print("Tabla de Multiplicacion del: ",i)
		for j in range(10):
			print(i," x ",j," = ",i*j)

def tarea_35():
	print("35. Hacer un algoritmo en Pseint que nos permita saber cul es el nmero mayor y menor, se debe ingresar slo veinte nmeros.")
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

def tarea_36():
	print("36. Hacer un algoritmo en Pseint para calcular la serie de Fibonacci.")
	numerodedigitosenserie = 0
	numeroacumulado = 0
	n_anterior = 0
	n_actual = 1
	print("Cuantos terminos tendra la sucesion?")
	numerodedigitosenserie = float(input())
	if numerodedigitosenserie==1 or numerodedigitosenserie==2:
		print(1)
	else:
		for i in range(numerodedigitosenserie-1):
			numeroacumulado = n_anterior+n_actual
			n_anterior = n_actual
			n_actual = numeroacumulado
		print(numeroacumulado)

def tarea_37():
	print("37. Hacer un algoritmo en Pseint para conseguir el M.C.D de un nmero por medio del algoritmo de Euclides.")
	print("El M.C.D. entre 1 y 12 es: ",mcdrecursivo(1,12))

def mcdrecursivo(a, b):
	if a<b:
		mcd_ = mcdrecursivo(b,a)
	else:
		if b==0:
			mcd_ = a
		else:
			mcd_ = mcdrecursivo(b,a%b)
	return mcd_

def tarea_38():
	print("38. Hacer un algoritmo en Pseint que nos permita saber si un nmero es un nmero perfecto.")
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

def tarea_39():
	print("39. Hacer un algoritmo en Pseint que cumpla con la aproximacin del nmero pi con la serie de Gregory-Leibniz. La formula que se debe aplicar es:")
	i = 0
	iteraciones_max = 9999
	pi_value = 0
	denominador = 1
	signo = 1
	while i<iteraciones_max:
		pi_value = pi_value+(4/denominador*signo)
		denominador = denominador+2
		signo = signo*(-1)
		i = i+1
	print(pi_value)

def tarea_40():
	print("40. Hacer un algoritmo en Pseint que cumpla con la aproximacin del nmero pi con la serie de Nilakantha. La formula que se debe aplicar es:")
	i = 0
	iteraciones_max = 0
	pi_value = 3
	denominador = 2
	signo = 1
	while i<iteraciones_max:
		pi_value = pi_value+((4/(denominador*(denominador+1)*(denominador+2)))*signo)
		denominador = denominador+2
		signo = signo*(-1)
		i = i+1
	print(pi_value)