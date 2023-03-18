Algoritmo ejercicio19
	Escribir "Ingrese la cantidad de CDs a comprar"
	Leer cantidad
	Definir precio_unitario Como Entero
	Definir ganancia_vendedor Como Real
	Si cantidad <= 0 Entonces
		Escribir "Cantidad no válida"
	Sino Si cantidad >= 1 y cantidad <= 9 Entonces
			precio_unitario = 10
			total = cantidad * precio_unitario
			ganancia_vendedor <- total * 0.0825
		FinSi
	FinSi
	Si cantidad >= 10 y cantidad <= 99 Entonces
		precio_unitario = 8
		total = cantidad * precio_unitario
		ganancia_vendedor <- total * 0.0825
	Sino Si cantidad >= 100 y cantidad <= 499 Entonces
			precio_unitario = 7
			total = cantidad * precio_unitario
			ganancia_vendedor <- total * 0.0825
		FinSi
	FinSi		
	Si cantidad >=500
		precio_unitario = 6
		total = cantidad * precio_unitario
		ganancia_vendedor <- total * 0.0825
	FinSi
	
	Escribir "El precio total para el cliente es de: $", total 
	Escribir "La ganancia para el vendedor es de: $", ganancia_vendedor
	
FinAlgoritmo