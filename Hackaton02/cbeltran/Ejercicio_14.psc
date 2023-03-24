Proceso Determinar_primo
	
	num=0;
	
	Escribir "Ingrese un número entero positivo del 1 al 10:"
    Leer num
	
    Si num < 1 O num > 10 Entonces
        Escribir "El número ingresado no es válido."
    SiNo
        Si num == 2 O num == 3 O num == 5 O num == 7 Entonces
            Escribir "El número ingresado es primo."
        SiNo
            Escribir "El número ingresado no es primo."
        FinSi
    FinSi
FinProceso
