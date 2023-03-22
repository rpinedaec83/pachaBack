Algoritmo Ejercicio23
	//Hacer un algoritmo en Pseint para calcular
	//la suma de los n�meros impares menores o iguales a n.
	Escribir "Ingrese un numero entero positivo"
	leer n
	count <- 0

	Para i <- 1 Hasta n Con Paso 2 Hacer //suma 2 para impar, for
		count <- count + i
	Fin Para
	Escribir "La suma de los n�meros impares menores o iguales a " n , " es: ", count
FinAlgoritmo
