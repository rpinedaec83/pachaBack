Proceso sin_titulo
	Definir x, sueldo, bono Como Entero;
	bono = 0;
	sueldo = 0;
	
	Escribir "ingrese las horas trabajadas";
	Leer x;
	
	si (x < 40) entonces
		sueldo = x * 20;
		Escribir "Sueldo: ",sueldo;
	SiNo
		bono = x - 40;
		sueldo = (x - bono) * 20;
		Escribir "Sueldo: ",sueldo + (bono * 25);
	FinSi
FinProceso
