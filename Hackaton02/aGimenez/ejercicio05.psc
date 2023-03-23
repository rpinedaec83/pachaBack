Proceso ejercicio05
	nroZapatos = 0
	totalAPagar = 0
	totalDescuento = 0
	precioZapatos = 80
	
	Escribir "Ingresar Cantidad de Zapatos a Comprar"
	Leer nroZapatos
	
	si nroZapatos < 10 Entonces
		totalAPagar = nroZapatos * precioZapatos
		Escribir "No hay descuento"
		Escribir "Total a Pagar: $ " totalAPagar
	FinSi
	si nroZapatos >= 10 y nroZapatos < 20 Entonces
		totalAPagar = nroZapatos * precioZapatos
		Escribir "Descuento de 10%"
		Escribir "Total a Pagar: $" totalAPagar - (totalAPagar * 0.10)
	FinSi
	si nroZapatos >= 20 y nroZapatos < 30 Entonces
		totalAPagar = nroZapatos * precioZapatos
		Escribir "Descuento de 20%"
		Escribir "Total a Pagar: $" totalAPagar - (totalAPagar * 0.20)
	FinSi
	si nroZapatos >= 30 Entonces
		totalAPagar = nroZapatos * precioZapatos
		Escribir "Descuento de 40%"
		Escribir "Total a Pagar: $" totalAPagar - (totalAPagar * 0.40)
	FinSi
FinProceso
