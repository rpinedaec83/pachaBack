Proceso Ejercicio5
	Escribir "Número de zapatos que se compran: "
	Leer Numerozapatos
	
	PrecioZapato <- 80
	PrecioTotal <- NumeroZapatos * PrecioZapato
	
	Si NumeroZapatos > 10 Y NumeroZapatos < 21
		PrecioTotal <- PrecioTotal * 0.9
	FinSi
	
	Si NumeroZapatos > 20 Y NumeroZapatos < 30 Entonces
		PrecioTotal <- PrecioTotal * 0.8
	FinSi
	
	Si NumeroZapatos > 30 Entonces
		PrecioTotal <- PrecioTotal * 0.6
	FinSi
	
	Escribir "El total a pagar por la compra es: ", PrecioTotal
FinProceso