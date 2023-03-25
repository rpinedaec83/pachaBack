Algoritmo ejer27
	
	Definir c como entero
	Definir x, suma Como Real
	x=1
	suma = 0
	contador = 0
	
	Mientras x>=0 Hacer
		Escribir "Ingrese un número positivo (para terminar ingrese un número positivo): "
		Leer x
		
		Si x >= 0 Entonces
			suma = suma + x
			contador = contador + 1
		FinSi
	FinMientras
	si c>0 Entonces
		Escribir "La media es: " , suma/c
		FinSi

	
FinAlgoritmo

