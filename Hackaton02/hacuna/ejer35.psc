Algoritmo MayorMenor
	
	// Definimos las variables para el mayor y menor número
	Definir mayor, menor Como Entero
	
	// Pedimos al usuario que ingrese el primer número
	Escribir "Ingrese el primer número:"
	Leer mayor
	menor <- mayor // asumimos que el primer número ingresado es el mayor y el menor
	
	// Iniciamos un ciclo para ingresar los restantes 19 números
	Para i <- 2 Hasta 20 Con Paso 1 Hacer
		Escribir "Ingrese el número ", i, ":"
		Definir numero Como Entero
		Leer numero
		
		// Comparamos el número ingresado con el mayor y menor actual
		Si numero > mayor Entonces
			mayor <- numero
		FinSi
		
		Si numero < menor Entonces
			menor <- numero
		FinSi
		
	FinPara
	
	// Imprimimos el resultado
	Escribir "El número mayor es: ", mayor
	Escribir "El número menor es: ", menor
	
FinAlgoritmo

