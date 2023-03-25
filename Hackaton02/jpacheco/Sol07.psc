Algoritmo sin_titulo
	//7.-Hacer un algoritmo en Pseint para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
	//Tipo A 10% de descuento
	//Tipo B 15% de descuento
	//Tipo C 20% de descuento

	
		Escribir "Ingresar el monto a comprar: ";
		Leer compra;
		Escribir "Ingresar el tipo de cliente: A, B, C ";
		Leer TipoCliente;
		
		segun (TipoCliente) hacer
			Caso 'A':
				Escribir "Tipo de Cliente A";
				Escribir "Total a pagar: ",(compra - (compra * 0.10));
			Caso 'B':
				Escribir "Tipo de Cliente B";
				Escribir "Total a pagar: ",compra - (compra * 0.15);
			Caso 'C':
				Escribir "Tipo de Cliente C";
				Escribir "Total a pagar: ",compra - (compra * 0.20);
				
			De Otro Modo:
				Escribir "Total a pagar: ",compra;
		FinSegun
		
FinAlgoritmo
