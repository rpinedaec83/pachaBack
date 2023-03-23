Proceso Ejercicio9
	Definir sueldo Como Real;
	
	Escribir 'Ingresar su sueldo anterior';
	
	Leer sueldo;
	
	Si (sueldo<2000) Entonces
		Escribir 'Su sueldo actual será de: ',sueldo+(sueldo*0.1);
	SiNo
		Escribir 'Su sueldo actual será de: ',sueldo+(sueldo*0.05);
	FinSi
	
FinProceso
