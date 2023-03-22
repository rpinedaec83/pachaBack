Algoritmo Ejericicio17
	numeroCds = 0
	ganancia = 0
	precioTotal = 0
	
	Escribir "Numero de cds que comprara el cliente"
	Leer numeroCds
	
	Si numeroCds <= 9  Entonces
		precioTotal = numeroCds * 10
	FinSi
	
	Si numeroCds >= 10 & numeroCds <= 99 Entonces
		precioTotal = numeroCds * 8
	Fin Si
	
	Si numeroCds >= 100 & numeroCds <= 499  Entonces
		precioTotal = numeroCds * 7
	Fin Si
	
	Si numeroCds > 500  Entonces
		precioTotal = numeroCds * 6
	Fin Si

	Escribir "Precio total del cliente: ", precioTotal
	Escribir "Ganancia para el vendedor: " precioTotal*8.25/100
	
FinAlgoritmo
