Proceso Deternimar_mayor_de_3números

	num1=0
	num2=0
	num3=0
	num_mayor=0

	Escribir "Ingrese el primer número entero: "
	Leer num1
	
	Escribir "Ingrese el segundo número entero: "
	Leer num2
	
	Escribir "Ingrese el tercer número entero: "
	Leer num3

	Si num1 > num2 Y num1 > num3 Entonces
		num_mayor = num1
	Sino
		Si num2 > num3 Entonces
			num_mayor = num2
		Sino
			num_mayor = num3
		FinSi
	FinSi

	Escribir "El número mayor es: ", num_mayor
FinProceso
