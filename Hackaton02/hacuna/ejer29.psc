Algoritmo SumaCienNumeros
	
	// Definimos las variables para la suma y el contador
	Definir suma, contador Como Entero
	
	// Inicializamos las variables
	suma <- 0
	contador <- 1
	
	// Iniciamos un ciclo mientras el contador sea menor o igual a 100
	Mientras contador <= 100 Hacer
		suma <- suma + contador // sumamos el contador a la suma actual
		contador <- contador + 1 // aumentamos el contador en 1
	FinMientras
	
	// Imprimimos el resultado
	Escribir "La suma de los primeros cien números es: ", suma
	
FinAlgoritmo

