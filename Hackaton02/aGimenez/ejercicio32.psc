Proceso ejercicio32
	Definir contadorCiudad, contadorProv, ciudad, mayorPoblacion como Entero;
	contadorProv = 1;
	mientras (contadorProv <= 3) Hacer
		mayorProblacion = 0;
		contadorCiudad = 1;
		Mientras (contadorCiudad <= 11) Hacer
			Leer ciudad;
			si (ciudad > mayorPoblacion) entonces
				mayorPoblacion = ciudad;
			FinSi
			contadorCiudad = contadorCiudad + 1;
		FinMientras
		Escribir "La población mayor de la provincia ",contadorProv," es: ", mayorPoblacion;
		contadorProv <- contadorProv + 1;
	FinMientras
FinProceso
