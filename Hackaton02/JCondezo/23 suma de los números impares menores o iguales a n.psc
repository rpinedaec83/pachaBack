//suma de los números impares menores o iguales a n.

Algoritmo sin_titulo
	Definir i,n,suma Como Entero;
	Escribir 'Ingrese la cantidad de números que quiere sumar';
	Leer n;
	suma <- 0;
	Para i<-1 Hasta n Con Paso 2 Hacer
		suma <- suma+i;
	FinPara
	Escribir 'La suma total es: ',suma;
FinAlgoritmo
