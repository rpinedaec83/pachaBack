Proceso sin_titulo
	
	escribir "Introduce el numero de dia"
	leer num_dia
	si num_dia < 8 y num_dia > 0 Entonces
		Segun num_dia Hacer
			1: escribir "El numero " num_dia " corresponde al dia lunes"
			2: escribir "El numero " num_dia " corresponde al dia martes"
			3: escribir "El numero " num_dia " corresponde al dia miercoles"
			4: escribir "El numero " num_dia " corresponde al dia jueves"
			5: escribir "El numero " num_dia " corresponde al dia viernes"
			6: escribir "El numero " num_dia " corresponde al dia sabado"
			7: escribir "El numero " num_dia " corresponde al dia doimingo"
		FinSegun
	SiNo
		Escribir "El numero " num_dia " no corresponde "
	FinSi

FinProceso
