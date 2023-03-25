Proceso sin_titulo
	Definir  precio,desc Como Real
	Definir  tipo Como Caracter
	Escribir  "¿Cuanto cuesta el helado?"
	Leer  precio
	Escribir  "¿Que tipo de helado es?(tipo a, b y c)"
	Leer  tipo
	Segun tipo Hacer
		"a" o "A":
			desc = (precio * 10)/100
			precio = precio - desc
		"b" o "B":
			descuento = (precio * 15)/100
			precio = precio - desc
		"c" o "C":
			descuento = (precio * 20)/100
			precio = precio - desc
	Fin Segun
	Escribir  "el precio es ", precio
FinProceso
