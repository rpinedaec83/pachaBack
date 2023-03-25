Algoritmo e37
	
	Escribir "Ingrese el primer número:"
	Leer num1
	Escribir "Ingrese el segundo número:"
	Leer num2
	
	Si num1 < num2 entonces
		aux = num1
		num1 = num2
		num2 = aux
	FinSi
	
	Mientras num2 <> 0 Hacer
		resto = num1 % num2
		num1 = num2
		num2 = resto
	FinMientras
	
	Escribir "El MCD de los números ingresados es: ", num1
	
FinAlgoritmo

