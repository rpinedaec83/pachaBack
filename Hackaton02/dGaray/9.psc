Proceso sin_titulo
	Leer sueldo;
    incremento = 0;
	
    Si sueldo > 2000 Entonces
        incremento = sueldo * 0.05;
    FinSi
	
    Si sueldo < 2000 Entonces
        incremento = sueldo * 0.1;
    FinSi
	
    nuevo_sueldo = sueldo + incremento;
    Escribir "Valor de incremento: ", incremento;
    Escribir "Valor de nuevo sueldo: ", nuevo_sueldo;
FinProceso
