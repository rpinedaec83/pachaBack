Proceso Ejercicio6
	Definir horasTrab, sueldo, horasExtra Como Entero;
	horasExtra <- 0;
	sueldo <- 0;
	
	Escribir "Ingresar horas trabajadas:";
	Leer horasTrab;
	
	si (horasTrab < 40) entonces
		sueldo <- horasTrab * 20;
		Escribir "El sueldo que le corresponde esta semana es de: ",sueldo;
	SiNo
		horasExtra <- horasTrab - 40;
		sueldo <- (horasTrab - horasExtra) * 20;
		Escribir "El sueldo que le corresponde esta semana es de: ",sueldo + (horasExtra * 25);
	FinSi
	
FinProceso
