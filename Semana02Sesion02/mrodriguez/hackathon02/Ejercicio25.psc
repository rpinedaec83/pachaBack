Proceso Ejercicio25
	//Hacer un algoritmo en Pseint para calcular
	//el factorial de un n�mero de una forma distinta.

	Definir num, factorial Como Entero
	Escribir "Ingresa un numero para calcular el fatorial"
	leer num

	si num < 0 Entonces
		Escribir "Numero debe ser positivo"
	SiNo
		i = 1
		factorial = 1
		Repetir
			factorial = factorial * i
			i = i + 1
		Hasta Que i > num
		Escribir factorial
	FinSi
FinProceso
