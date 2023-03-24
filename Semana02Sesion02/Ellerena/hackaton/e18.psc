Algoritmo e18
	Definir cantidad Como Entero
	Definir precioUnitario, precioTotal Como Real
	
	Escribir "Ingrese la cantidad de CD vírgenes que desea adquirir: "
	Leer cantidad
	
	Si cantidad <= 9 Entonces
		precioUnitario = 10
	Sino
		Si cantidad <= 99 Entonces
			precioUnitario = 8
		Sino
			Si cantidad <= 499 Entonces
				precioUnitario = 7
			Sino
				precioUnitario = 6
			FinSi
		FinSi
	FinSi
	
	precioTotal = cantidad * precioUnitario
	
	Escribir "El precio total de su compra es: $", precioTotal
FinAlgoritmo
