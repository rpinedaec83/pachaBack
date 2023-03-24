Proceso Determina_si_termina_en_4

	num=0
	ultimo_digito=0;
	
	Escribir "Ingrese un número:"
	Leer num	
	
	ultimo_digito <- num mod 10
	
	Si ultimo_digito = 4 Entonces
		Escribir "El número ", num, " termina en 4."
	SiNo
		Escribir "El número ", num, " no termina en 4."
  FinSi
FinProceso
