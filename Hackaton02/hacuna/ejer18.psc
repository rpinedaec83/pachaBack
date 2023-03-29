Algoritmo ejercicio18
	Definir cantidad, precio_unitario, precio_total Como Real
    
    Escribir "Ingrese la cantidad de CD vírgenes a comprar:"
    Leer cantidad
    
    Si cantidad >= 1 Y cantidad <= 9 Entonces
        precio_unitario <- 10
    Sino Si cantidad >= 10 Y cantidad <= 99 Entonces
			precio_unitario <- 8
		Sino Si cantidad >= 100 Y cantidad <= 499 Entonces
			precio_unitario <- 7
			Sino Si cantidad >= 500 Entonces
					precio_unitario <- 6
				Sino
					Escribir "Cantidad inválida."
				FinSi
			FinSi
		FinSi
	FinSi
	precio_total <- cantidad * precio_unitario
	ganancia_vendedor <- precio_total * 0.0825
				
	Si precio_unitario <> 0 Entonces
		Escribir "El precio total para el cliente es: $" precio_total
		Escribir "La ganancia para el vendedor es: $" ganancia_vendedor
	FinSi
FinAlgoritmo
