Proceso Tienda_zapatos

	num_zapatos=0
	descuento=0
	
	precio_zapato=0.0
	total_compra=0.0
	precio_con_descuento=0.0

	Escribir "Ingrese el número de zapatos que desea comprar:"
	Leer num_zapatos

	precio_zapato = 80
	total_compra = precio_zapato * num_zapatos

	Si num_zapatos > 30 Entonces
		descuento = 40
	SiNo
		Si num_zapatos > 20 Entonces
			descuento = 20
		SiNo
			Si num_zapatos > 10 Entonces
				descuento = 10
			SiNo
				descuento = 0
			FinSi
		FinSi
	FinSi

	precio_con_descuento = total_compra - (total_compra * descuento / 100)

	Escribir "El precio total de la compra es de: $", total_compra
	Escribir "Se aplica un descuento del ", descuento, "%"
	Escribir "El precio con descuento es de: $", precio_con_descuento
FinProceso
