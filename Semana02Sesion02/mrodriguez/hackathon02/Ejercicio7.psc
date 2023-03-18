Proceso Ejercicio7
	//Hacer un algoritmo en Pseint para una tienda de helado
	//que da un descuento por compra a sus clientes
	//con membres�a dependiendo de su tipo,
	//s�lo existen tres tipos de membres�a, tipo A, tipo B y tipo C. Los descuentos son los siguientes:

	//Tipo A 10% de descuento
	//Tipo B 15% de descuento
	//Tipo C 20% de descuento

	precioConDescuento = 0

	Escribir "Precio de helado: "
	leer precio
	Escribir "Tipo de membres�a A, B o C: "
	leer tipo

	Segun tipo Hacer
		"A":
			precioConDescuento = precio - (precio * 0.1)
			Escribir "Precio final con 10% dcto: s/", precioConDescuento
		"B":
			precioConDescuento = precio - (precio * 0.15)
			Escribir "Precio final con 15% dcto: s/", precioConDescuento
		"C":
			precioConDescuento = precio - (precio * 0.2)
			Escribir "Precio final con 20% dcto: s/", precioConDescuento	
		De Otro Modo:
			Escribir "Opci�n no v�lida"
	Fin Segun
FinProceso
