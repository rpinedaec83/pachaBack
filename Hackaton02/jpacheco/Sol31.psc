Algoritmo sin_titulo
	//31.-Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números.
	conta <- 0; conta1 <- 0; conta2 <- 0;
	// conta 1 y 2 son los contadores de los números
	// positivos (conta1) y negativos (conta2)
	suma1 <- 0; suma2 <- 0;
	media1 <- 0; media2 <- 0;
	// Suma 1,2 y Media 1 y 2 también son
	// para los números positivos y negativos
	Repetir
		Leer n;
		Si (n>0) Entonces
			suma1 <- suma1+n;
			conta1 <- conta1+1;
		SiNo
			suma2 <- suma2+n;
			conta2 <- conta2+1;
		FinSi
		conta <- conta+1;
	Hasta Que conta=10
	media1 <- suma1/conta1;
	media2 <- suma2/conta2;
	Escribir 'La media de los números positivos es: ',media1;
	Escribir 'La media de los números negativos es: ',media2;
FinAlgoritmo
