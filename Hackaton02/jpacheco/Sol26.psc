Algoritmo sin_titulo
	//26.-Hacer un algoritmo en Pseint para calcular el resto y cociente por medio de restas sucesivas.
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
