Proceso Ejercicio5
	Definir nroZapatos,precio Como Entero;
	precio <- 0;
	
	Escribir "Cantidad de Zapatos a comprar:";
	Leer nroZapatos;
	precio <- nroZapatos * 80;
	
	si (nroZapatos < 10) entonces
		Escribir "No se aplica descuento. El precio total a pagar es: ", precio;
	SiNo
		si(nroZapatos < 20) entonces
			Escribir "Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.1);
		sino 
			si(nroZapatos < 30) Entonces
				Escribir " Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.2);
			SiNo
				Escribir "Se aplica descuento. El precio total a pagar es: ", precio - (precio * 0.4);
			FinSi
		FinSi
	FinSi
FinProceso
