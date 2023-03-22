Algoritmo sin_titulo
	//32.-Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, hacer un algoritmo en Pseint que nos permita saber eso.
	conta1 <- 1;
	mientras (conta1 <= 3) Hacer
		_mayor <- 0;
		conta2 <- 1;
		Mientras (conta2 <= 11) Hacer
			Leer ciudad;
			si (ciudad > _mayor) entonces
				_mayor <- ciudad;
			FinSi
			conta2 <- conta2 + 1;
		FinMientras
		Escribir "La población mayor de la provincia ",conta1," es: ",_mayor;
		conta1 <- conta1 + 1;
	FinMientras
FinAlgoritmo
