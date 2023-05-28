//para calcular el factorial de un número de una forma distinta.
Algoritmo sin_titulo
	Definir numero, factorial, x Como Real
	Escribir "Ingresa un numero"
	leer numero
	si numero<0 Entonces
		escribir "no puede calcularse por ser negativo"
	SiNo
		x=1
		factorial=1
		mientras x<=numero Hacer
			factorial=factorial*x
			x=x+1
		FinMientras
		escribir "el Factorial de " numero " es" factorial
	FinSi
FinAlgoritmo
