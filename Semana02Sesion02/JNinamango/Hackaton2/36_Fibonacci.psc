Algoritmo Fibonacci
	NumeroDeDigitosEnSerie = 0
	numeroAcumulado = 0
	N_Anterior = 0
	N_Actual = 1
	
	Escribir  "Cuantos terminos tendra la sucesion?"
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
	


FinAlgoritmo
