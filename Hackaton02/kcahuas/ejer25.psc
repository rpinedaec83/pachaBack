Algoritmo ejer25
	
	//Hacer un algoritmo en Pseint para calcular el factorial de un número de una forma distinta.
	Definir n,conta,_factorial Como Entero;
	Escribir 'Ingrese un número';
	Leer n;
	conta <- 1; _factorial <- 1;
	Repetir
		_factorial <- _factorial*conta;
		conta <- conta+1;
	Hasta Que conta>n
	Escribir 'El factorial es: ',_factorial;
	
	
FinAlgoritmo
