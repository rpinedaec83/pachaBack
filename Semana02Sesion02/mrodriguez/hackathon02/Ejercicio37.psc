Proceso Ejercicio37
	//Hacer un algoritmo en Pseint para
	//conseguir el M.C.D de un numero
	//por medio del algoritmo de Euclides.

	Definir num1, num2, aux, residuo Como Entero
	Repetir
		Escribir "Ingresa primero numero entero positivo"
		leer num1
	Hasta Que  num1 > 0

	Repetir
		Escribir "Ingresa segundo numero entero positivo"
		leer num2
	Hasta Que  num2 > 0

	Si num2 > num1 Entonces
		aux = num2
		num2 = num1
		num1 = aux
	FinSi

	residuo = num1 mod num2

	Mientras residuo > 0 Hacer
		aux = num2
		num2 = residuo
		num1 = aux
		residuo = num1 mod num2
	FinMientras

	Escribir "MCD = " num2
FinProceso
