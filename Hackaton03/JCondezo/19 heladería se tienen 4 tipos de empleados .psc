Algoritmo ejer19
	Definir empleado,diaTrabajado,salariodia,salariototal Como Entero;
	salario <- 0;	
	Escribir 'Ingrese el identificador del empleado';
	Escribir "01: cajero"
	Escribir "02: servidor"
	Escribir "03: preparador de mezclas"
	Escribir "04: mantenimiento"
	Leer empleado;
	Escribir 'Ingrese los días trabajados maximo 6 dias';
	Leer diaTrabajado;
	
	si diaTrabajado <= 6 Entonces
		Segun empleado hacer
			01: escribir "monto total a pagar a un cajero es de ",(diaTrabajado*56)
		    02: escribir "monto total a pagar a un cajero es de ",(diaTrabajado*64)
			03:	escribir "monto total a pagar a un cajero es de ",(diaTrabajado*80)
			03:	escribir "monto total a pagar a un cajero es de ",(diaTrabajado*48)
			
		FinSegun
	SiNo
		Escribir "el numero exde a 6"
	FinSi

	
	
FinAlgoritmo
