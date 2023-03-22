Proceso Ejercicio22
	//Hacer un algoritmo en Pseint para
	//calcular la suma de los n primeros n�meros.

	Definir num Como Entero
	result = 0
	Escribir "Ingresa un numero positivo"
	leer num

	si num < 0 Entonces
		Escribir "Numero debe ser positivo"
	SiNo
		Para i = 0 Hasta num Con Paso 1 Hacer
			result = result + i
		FinPara
		Escribir "La suma de los n�meros predecesores es: ", result
	FinSi

FinProceso
