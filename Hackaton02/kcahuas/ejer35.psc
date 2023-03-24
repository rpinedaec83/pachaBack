Algoritmo ejer35
	//Hacer un algoritmo en Pseint que imprima la tabla de multiplicar de los números del uno nueve.
	Definir i, j, producto Como Entero;
	para i <- 1 hasta 9 hacer
		Escribir "Tabla del ",i;
		para j <- 1 hasta 10 hacer
			producto <- i * j;
			Escribir i," por ",j," = ",producto;
		FinPara
	FinPara
FinAlgoritmo
