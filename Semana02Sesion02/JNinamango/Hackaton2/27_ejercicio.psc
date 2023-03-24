Algoritmo ejercicio_27
	Escribir "27. Hacer un algoritmo en Pseint para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número positivo."
	Definir  C Como Entero
	definir x, suma Como Real
	
	x = 1
	suma = 0
	c= 0
	
	Mientras  x>=0 Hacer
		Escribir  "Ingresa cualquier numero positivo."
		Leer  x
		si x >= 0 Entonces
			suma = suma + x
			c = c + 1
		FinSi
	FinMientras
	
	si c > 0 Entonces
		Escribir  "La media es: ", suma / c
	FinSi
	
FinAlgoritmo
