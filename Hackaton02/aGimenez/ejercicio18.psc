Proceso ejercicio18
	cantidadCD = 0
	totalAPagar = 0
	gananciaVendedor = 0
	
	Escribir "Cantidad de CD a Comprar"
	Leer cantidadCD
	
	si cantidadCD < 10 Entonces
		Escribir "Precio Unitario: $10"
		totalAPagar = cantidadCD * 10
		gananciaVendedor = totalAPagar * 0.0825
		Escribir "Total a Pagar: $" totalAPagar
		Escribir "Ganancia Vendedor: $" gananciaVendedor
	FinSi
	si cantidadCD >= 10 y cantidadCD < 100 Entonces
		Escribir "Precio Unitario: $8"
		totalAPagar = cantidadCD * 8
		gananciaVendedor = totalAPagar * 0.0825
		Escribir "Total a Pagar: $" totalAPagar
		Escribir "Ganancia Vendedor: $" gananciaVendedor
	FinSi
	si cantidadCD >= 100 y cantidadCD < 500 Entonces
		Escribir "Precio Unitario: $7"
		totalAPagar = cantidadCD * 7
		gananciaVendedor = totalAPagar * 0.0825
		Escribir "Total a Pagar: $" totalAPagar
		Escribir "Ganancia Vendedor: $" gananciaVendedor
	FinSi
	si cantidadCD >= 500 Entonces
		Escribir "Precio Unitario: $6"
		totalAPagar = cantidadCD * 6
		gananciaVendedor = totalAPagar * 0.0825
		Escribir "Total a Pagar: $" totalAPagar
		Escribir "Ganancia Vendedor: $" gananciaVendedor
	FinSi
FinProceso
