Algoritmo  CD
Escribir "Ingrese la cantidad de CDs a vender:"
Leer cantidad

Si cantidad >= 1 Y cantidad <= 9 Entonces
	precio_unitario = 10
Sino Si cantidad >= 10 Y cantidad <= 99 Entonces
		precio_unitario = 8
	Sino Si cantidad >= 100 Y cantidad <= 499 Entonces
			precio_unitario = 7
		Sino
			precio_unitario = 6
		Fin Si
	Fin Si
Fin Si	
		precio_total = cantidad * precio_unitario
		ganancia_vendedor = precio_total * 0.0825
		
		Escribir "El precio total para el cliente es: $", precio_total
		Escribir "La ganancia para el vendedor es: $", ganancia_vendedor
FinProceso
