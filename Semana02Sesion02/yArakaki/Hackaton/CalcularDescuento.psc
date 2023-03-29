Algoritmo CalcularDescuento
	Definir totalCompra, descuento, totalConDescuento Como Real
	Definir tipoMembresia Como Carácter
	
	Escribir "Ingrese el total de la compra:"
	Leer totalCompra
	
	Escribir "Ingrese el tipo de membresía (A, B o C):"
	Leer tipoMembresia
	
	Si tipoMembresia = "A" Entonces
		descuento = totalCompra * 0.1
		Sino si tipoMembresia = "B" Entonces
			descuento = totalCompra * 0.15
		Sino Si tipoMembresia = "C" Entonces
				descuento = totalCompra * 0.2
			Sino
				Escribir "El tipo de membresía ingresado no es válido."
			FinSi
		FinSi
	FinSi	
			totalConDescuento = totalCompra - descuento
			Escribir "El descuento aplicado es de: $" , descuento
			Escribir "El total a pagar es de: $" , totalConDescuento
			
FinAlgoritmo
