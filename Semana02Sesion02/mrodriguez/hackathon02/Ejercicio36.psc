Proceso Ejercicio36
	//Hacer un algoritmo en Pseint para 
	//calcular la serie de Fibonacci.
	
	NumeroDeDigitosEnSerie = 0
	numeroAcumulado = 0
	N_Anterior = 0
	N_Actual = 1
	
	Escribir  "Ingresa numero de termino para Serie Fibonacci"
	Leer  NumeroDeDigitosEnSerie
	
	Si NumeroDeDigitosEnSerie == 1 | NumeroDeDigitosEnSerie == 2 Entonces
		Escribir 1
	SiNo
		Para i <- 0 Hasta NumeroDeDigitosEnSerie-2 Con Paso 1 Hacer
			numeroAcumulado = N_Anterior + N_Actual
			N_Anterior = N_Actual
			N_Actual = numeroAcumulado
		Fin Para
		
		Escribir numeroAcumulado
	Fin Si
FinProceso
