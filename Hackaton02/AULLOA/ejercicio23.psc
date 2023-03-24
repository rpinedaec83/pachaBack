Algoritmo ejercicio23
	//Hacer un algoritmo en Pseint para calcular la suma de los números impares menores o iguales a n.
	Escribir "ingrese un numero entero positivo: "
	Leer numeroEnteroIngresado
	count <- 0
	Para i <- 1 Hasta numeroEnteroIngresado Con Paso 2 Hacer
		count <- count + i
	FinPara
	Escribir "la suma de los numeros: ", count
FinProceso