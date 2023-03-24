Proceso Deternimar_mayor_de_2números
	num1=0
	num2=0
	num_mayor=0
	
	Escribir "Ingrese el primer número entero: "
	Leer num1
	
	Escribir "Ingrese el segundo número entero: "
	Leer num2
	
	Si num1 > num2 Entonces
		num_mayor = num1
	Sino
		num_mayor = num2
	FinSi
	
	Escribir "El número mayor es: ", num_mayor
FinProceso
