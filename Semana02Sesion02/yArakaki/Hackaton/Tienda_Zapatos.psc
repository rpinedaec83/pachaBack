Algoritmo Tienda_Zapatos
	
	cantidad_zapatos = 0
	precio_total = 0
	descuento = 0
	precio_descuento = 0

	Escribir "Ingrese la cantidad de zapatos que desea comprar: "
	Leer cantidad_zapatos
	
	
	precio_total <- cantidad_zapatos * 80
	
	
	Si cantidad_zapatos > 10 Y cantidad_zapatos < 20 Entonces
			descuento <- 0.1
			Sino si cantidad_zapatos >= 20 Y cantidad_zapatos < 30 Entonces
			descuento <- 0.2
		Sino si cantidad_zapatos >= 30  Entonces
			descuento <- 0.4
		FinSi
		FinSi
	Finsi
	
	
	precio_descuento <- precio_total - (precio_total * descuento)
	

	Escribir "El precio total de los ", cantidad_zapatos, " zapatos es de $", precio_total
	Escribir "El precio con descuento es de $", precio_descuento
	
FinAlgoritmo
