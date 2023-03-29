Algoritmo sin_titulo
	//38.-Hacer un algoritmo en Pseint que nos permita saber si un número es un número perfecto.
	Escribir 'Ingrese un número';
	Leer num;
	cont <- 0;
	canti <- 0;
	// inicio de ciclos
	Mientras (num<>cont) Hacer
		cont <- cont+1;
		Si (cont<>num) Entonces
			resto <- num MOD cont;
			Si (resto=0) Entonces
				canti <- canti+cont;
			FinSi
		SiNo
			cont <- num;
		FinSi
	FinMientras
	Escribir 'Suma de los divisores: ',canti;
	// imprime los contadores
	Si (num=canti) Entonces
		Escribir 'Es perfecto';
	SiNo
		Escribir 'No es perfecto';
	FinSi
FinAlgoritmo
