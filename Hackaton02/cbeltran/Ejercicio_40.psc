Proceso Nilakantha_pi

	num=0;
	num_pi = 0.0
	contador = 0
	Escribir "Ingrese un número: ";
	Leer num;
	Para i = 2 hasta num con paso 2 hacer
		Si (contador mod 2=0) entonces
			num_pi = num_pi + (4/ (i * (i + 1) * (i + 2)))
		Sino
			num_pi = num_pi- (4/ (i * (i + 1) * (i + 2)))
		Finsi
		contador = contador + 1
	FinPara
	Escribir "Pi se aproxima a: " num_pi + 3
FinProceso
