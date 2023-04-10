// para determinar la media de una lista indefinida de números positivos, se debe acabar el programa al ingresar un número positivo.

Algoritmo sin_titulo
	Definir n,media,conta Como Entero;
	Definir i Como Real;
	Escribir 'Ingrese un número';
	Leer n;
	media <- 0; conta <- 0; i <- 0;
	Mientras (n>=0) Hacer // El valor centinela es un número menor que cero
		media <- media+n;
		conta <- conta+1;
		Leer n; // mientra n sea mayorr que cero, el bucle continua     
	FinMientras
	i <- media/conta;
	Escribir 'La media es: ',i;
FinAlgoritmo
