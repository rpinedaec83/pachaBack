Algoritmo Factorial
	
	Escribir "Ingrese un número entero positivo: "
	Leer numero
	factorial1 = 1
	
	Si numero < 0 Entonces
		Escribir "El número ingresado no es válido."
	Sino Si numero = 0 Entonces
			Escribir "El factorial de 0 es 1."
		Sino
			Para i = 1 Hasta numero Hacer
				factorial1 = factorial1 * i
			FinPara
			Escribir "El factorial de ", numero, " es: ", factorial1
		FinSi
	FinSi

		
FinAlgoritmo
