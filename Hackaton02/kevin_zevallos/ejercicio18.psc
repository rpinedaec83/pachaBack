Algoritmo ejercicio18
    Escribir "Ingrese la cantidad de CDs a comprar"
	Leer cantidad
	
	Si cantidad <= 0 Entonces
		Escribir "Cantidad no válida"
	Sino Si cantidad >= 1 y cantidad <= 9 Entonces
			total = cantidad * 10
		FinSi
	FinSi
	Si cantidad >= 10 y cantidad <= 99 Entonces
		total = cantidad * 8
	Sino Si cantidad >= 100 y cantidad <= 499 Entonces
			total = cantidad * 7
			FinSi
	FinSi		
	Si cantidad >=500
		total = cantidad * 6
				
	FinSi
	Escribir "El total a pagar es: $", total
FinAlgoritmo