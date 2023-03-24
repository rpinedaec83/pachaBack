//trabajador  a saber cuál será su sueldo semanal, 
//se sabe que si trabaja 40 horas o menos,
//se le pagará $20 por hora, pero si trabaja más de 40 horas 
//entonces las horas extras se le pagarán a $25 por hora.
Algoritmo sin_titulo
	definir horas,horas_extras,pago Como Real
	escribir "Ingrese las horas trabajadas"
	leer horas
	si horas>40
		horas_extras=HORAS-40
		PAGO=(40*16)+(horas_extras*20)
	SiNo
		pago=horas*16
																																																																																																																																																																																																																																																																																
	FinSi
Escribir "El pago semanal por ",horas," horas trabajadas es de, " pago
	

FinAlgoritmo
