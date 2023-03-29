Algoritmo Ordenar_Numeros
	
	num1 = 0
	num2 = 0
	num3 = 0
	comp = 0
	

	Escribir "Ingrese el primer número: "
	Leer num1
	
	Escribir "Ingrese el segundo número: "
	Leer num2
	
	Escribir "Ingrese el tercer número: "
	Leer num3
	
	
	Si(num1 > num2) Entonces
		comp <- num1
		num1 <- num2
		num2 <- comp
	FinSi
	
	Si(num2 > num3) Entonces
		comp <- num2
		num2 <- num3
		num3 <- comp
		
		Si(num1 > num2) Entonces
			comp <- num1
			num1 <- num2
			num2 <- comp
		FinSi
	FinSi
	
	
	Escribir num1 "-" num2 "-" num3
	
FinAlgoritmo
