Algoritmo TiendaDeZapatos
		
		// Pedir la cantidad de zapatos que se van a comprar
		Escribir "Ingrese la cantidad de zapatos que desea comprar: "
		Leer cantidad
		
		// Calcular el precio sin descuento
		precioSinDescuento <- cantidad * 80
		
		// Aplicar el descuento correspondiente
		Si cantidad > 10 y cantidad <= 20 entonces
			descuento <- precioSinDescuento * 0.1
		Sino Si cantidad > 20 y cantidad < 30 entonces
				descuento <- precioSinDescuento * 0.2
			Sino Si cantidad >= 30 entonces
					descuento <- precioSinDescuento * 0.4
				Sino
					descuento <- 0
				Fin Si
			FinSi
		FinSi
				
				// Calcular el precio con descuento
				precioConDescuento <- precioSinDescuento - descuento
				
				// Mostrar el resultado
				Escribir "El precio sin descuento es: $", precioSinDescuento
				Escribir "El descuento aplicado es: $", descuento
				Escribir "El precio con descuento es: $", precioConDescuento
				
FinAlgoritmo
