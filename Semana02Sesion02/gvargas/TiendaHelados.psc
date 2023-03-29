Algoritmo TiendaHelados
	membresia = ""
	total = 0
	descuento = 0
	Escribir "Indique el tipo de mebresía: "
	Leer membresia
	Escribir "Indique el total de compra: "
	Leer total
	Si membresia='A' Entonces
		descuento = total*0.1
		Escribir "Su descuento es: " descuento " y su total: " total-descuento
	SiNo
		Si membresia='B' Entonces
			descuento = total*0.15
			Escribir "Su descuento es: " descuento " y su total: " total-descuento
		SiNo
			Si membresia='C' Entonces
				descuento = total*0.2
				Escribir "Su descuento es: " descuento " y su total: " total-descuento
			FinSi
		FinSi
	FinSi
FinAlgoritmo
