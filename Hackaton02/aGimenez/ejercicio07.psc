Proceso ejercicio07
	cantHelado = 0
	tipoMembresia = X
	precioUnitario = 0
	precioTotal = 0
	
	Escribir "Ingrese Cantidad de Helados a Comprar: "
	Leer cantHelado
	Escribir "Ingrese Precio Unitario: "
	Leer precioUnitario
	precioTotal = cantHelado * precioUnitario
	Escribir "Ingrese Tipo de Membresia: "
	Leer tipoMembresia
	
	si tipoMembresia == 'A' o tipoMembresia == 'a' Entonces
		precioTotal = precioTotal - (precioTotal * 0.10)
		Escribir "Total a Pagar: $" precioTotal
		Escribir "Descuento 10%"
	FinSi
	si tipoMembresia == 'B' o tipoMembresia == 'b' Entonces
		precioTotal = precioTotal - (precioTotal * 0.15)
		Escribir "Total a Pagar: $" precioTotal
		Escribir "Descuento 15%"
	FinSi
	si tipoMembresia == 'C' o tipoMembresia == 'c' Entonces
		precioTotal = precioTotal - (precioTotal * 0.20)
		Escribir "Total a Pagar: $" precioTotal
		Escribir "Descuento 20%"
	FinSi
FinProceso
