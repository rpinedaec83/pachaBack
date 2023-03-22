Proceso ejercicio17
	hora = 0
	min = 0
	seg = 0
		
		Escribir "Ingresar Hora"
		Leer hora;
		Escribir "Ingresar Minutos"
		Leer min; 
		Escribir "Ingresar Segundos"
		Leer seg;
		
		si (hora < 24 y min < 60 y seg < 60) Entonces
			seg = seg + 1;
			si (seg == 60) Entonces
				seg = 0;
				min = min + 1;
				si (min == 60) Entonces
					min = 0;
					hora = hora + 1;
					si (hora == 24)Entonces
						hora = 0;
					FinSi
				FinSi
			FinSi
		FinSi
		
		Escribir hora, " : ", min, " : ", seg
		
FinProceso
