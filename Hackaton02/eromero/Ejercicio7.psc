Proceso Ejercicio7
    Definir tipoMembresia Como Caracter
    Definir totalCompra, totalPagar, descuento Como Real
    Escribir "Ingrese el tipo de membresía (A, B o C): "
    Leer tipoMembresia
	
    Escribir "Ingrese el total de la compra: "
    Leer totalCompra
	
    Si tipoMembresia = "A" Entonces
        descuento <- totalCompra * 0.1
	Sino Si tipoMembresia = "B" Entonces
		descuento <- totalCompra * 0.15
	Sino Si tipoMembresia = "C" Entonces
		descuento <- totalCompra * 0.2
	FinSi
	FinSi
	FinSi
			
	totalPagar <- totalCompra - descuento
	Escribir "El total a pagar es: ", totalPagar
FinProceso