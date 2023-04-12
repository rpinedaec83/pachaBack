//para calcular el resto y cociente por medio de restas sucesivas.

Algoritmo sin_titulo
	Definir n,d,resto,conta Como Entero;
	resto <- 0; conta <- 0;
	Escribir 'Numerador';
	Leer n;
	Escribir 'Denominador';
	Leer d;
	Repetir
		n <- n-d;
		resto <- n;
		conta <- conta+1;
	Hasta Que n<d
	Escribir 'El resto es: ',resto;
	Escribir 'El cociente es: ',conta;	
FinAlgoritmo
