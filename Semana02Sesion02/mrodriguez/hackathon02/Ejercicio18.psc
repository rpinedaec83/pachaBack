Proceso Ejercicio18
	//Hacer un algoritmo en Pseint para una
	//empresa se encarga de la venta y distribuci�n de CD v�rgenes. 
	//Los clientes pueden adquirir los art�culos
	//(supongamos un �nico producto de una �nica marca)
	//por cantidad. Los precios son:

    //$10. Si se compran unidades separadas hasta 9.
	//$8. Si se compran entre 10 unidades hasta 99.
	//$7. Entre 100 y 499 unidades.
	//$6. Para mas de 500 unidades.

	//La ganancia para el vendedor es de 8,25 % de la venta.
	//Realizar un algoritmo en Pseint que dado un n�mero de CDs a vender 
	//calcule el precio total para el cliente
	//y la ganancia para el vendedor.

	Definir ventas, total Como Entero;
	total <- 0;

	Escribir "Cantidad de CDs vendidos:";
	Leer ventas;

	Si (ventas <= 9) Entonces
		total <- ventas * 10;
	SiNo
		Si (ventas <= 99) Entonces
			total <- ventas * 8;
		SiNo
			Si (ventas <= 499) Entonces
				total <- ventas * 7;
			SiNo
				Si (ventas >= 500) Entonces
					total <- ventas * 6;
				FinSi
			FinSi
		FinSi
	FinSi

	Escribir "Total a pagar por cliente: ", total;
	Escribir "Ganancia del vendedor: ",total * 0.0825;

FinProceso
