Proceso E5
	
  	Definir zapatos, precio, total_compra, descuento Como Entero
	
	precio <- 80
	
	Escribir "Bienvenido a la tienda de zapatos."
	Escribir "¿Cuántos zapatos desea comprar?"
	Leer zapatos
	
	total_compra <- precio * zapatos
	
	Si zapatos > 10 Entonces
		descuento <- total_compra * 0.10
		Si zapatos > 20 y zapatos < 30 Entonces
			descuento <- total_compra * 0.20
			Si zapatos >= 30 Entonces
				descuento <- total_compra * 0.40
			FinSi
			
			total_compra <- total_compra - descuento
			
			Escribir "El total de su compra es de: $", total_compra, " MXN"
			
FinAlgoritmo