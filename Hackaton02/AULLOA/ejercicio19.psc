Proceso Ejercicio19
	//dt: dias Trabajados
	Definir tipoIden,dt,salario Como Entero;
	salario <- 0;
	
	Escribir 'Ingresar el identificador del empleado: (1,2,3,4)';
	Leer tipoIden;
	Escribir 'Ingresar los días trabajados';
	Leer dt;
	
	Segun (tipoIden)  Hacer
		1:
			salario <- dt*56;
		2:
			salario <- dt*64;
		3:
			salario <- dt*80;
		4:
			salario <- dt*48;
			
		De Otro Modo:
			Escribir 'El tipoIden de identificador no es válido';
	FinSegun
	
	Escribir 'La cantidad total a pagar es: ',salario;
	
FinProceso
