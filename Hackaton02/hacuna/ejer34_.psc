Algoritmo TablaMultiplicar
	
	// Ciclo para recorrer los números del 1 al 9
	Para i = 1 Hasta 9 Con Paso 1 Hacer
		Escribir "Tabla de multiplicar del ", i
		Escribir "---------------------------"
		
		// Ciclo para imprimir la tabla de multiplicar del número actual
		Para j = 1 Hasta 10 Con Paso 1 Hacer
			resultado = i * j
			Escribir i, " x ", j, " = ", resultado
		FinPara
		
		Escribir "" // Salto de línea para separar las tablas de multiplicar
	FinPara
	
FinAlgoritmo
