Proceso Ejercicio7
	
	Definir compra Como real;
	Definir tipoCliente como caracter;
	
	Escribir "Ingresar el monto a comprar: ";
	Leer compra;
	Escribir "Ingresar el tipo de cliente: A, B, C ";
	Leer tipoCliente;
	
	segun (tipoCliente) hacer
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
	
	
FinProceso
