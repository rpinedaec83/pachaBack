Proceso sin_titulo
	Escribir "Ingrese un numero de zapatos a comprar"
	leer numero_zapatos
	precio_zapato = 80
	si numero_zapatos < 10 Entonces
		Escribir "Usted no tiene descuento"
	Sino
		Si numero_zapatos >= 10 y numero_zapatos<20 Entonces
			descuento=20
		SiNo
			si numero_zapatos >= 20 y numero_zapatos<30 Entonces
				descuento= 30
			SiNo
				si numero_zapatos >= 30 Entonces
					descuento= 40
				FinSi
			FinSi
		FinSi
	FinSi
	precio_total = precio_zapato*numero_zapatos
	descuento_total=(precio_total*descuento)/100
	precio_pagar= precio_total - descuento_total
	Escribir "Vas a comprar " numero_zapatos " y tienes un descuento de " descuento " por ciento, y vas a pagar " precio_pagar
FinProceso
