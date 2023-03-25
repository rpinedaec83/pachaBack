//Hacer un algoritmo en Pseint para calcular el factorial de un número de una forma distinta.
Proceso Ejercicio25
	Definir numero,factorial como entero
	Escribir "Brindame un numero y te doy el factorial"
	Leer numero
	si numero < 0 Entonces
		Escribir "El numero ",numero, "no se puede calcular"
	SiNo
		x = 1
		
		factorial = 1
		
		Repetir
			
			factorial = factorial * x
			
			x = x +1
			
		Hasta Que x > numero
		
		Escribir factorial
	FinSi
	
FinProceso