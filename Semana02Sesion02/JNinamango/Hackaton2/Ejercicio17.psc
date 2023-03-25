Proceso Ejercicio17
	
	Definir Hora, Minuto, Segundos Como Entero;
	
	Escribir "Ingresa Hora:";
	Leer Hora;
	Escribir "Ingresa Minuto:";
	Leer Minuto; 
	Escribir "Ingresa Segundos:";
	Leer Segundos;
	
	si (Hora < 24 y Minuto < 60 y Segundos < 60) Entonces
		Segundos <- Segundos + 1;
		si (Segundos = 60) Entonces
			Segundos <- 0;
			Minuto <- Minuto + 1;
			si (Minuto = 60) Entonces
				Minuto <- 0;
				Hora <- Hora + 1;
				si (Hora = 24)Entonces
					Hora <- 0;
				FinSi
			FinSi
		FinSi
	FinSi
	
	Escribir Hora, " : ", Minuto, " : ", Segundos, " : ";
	
FinProceso
