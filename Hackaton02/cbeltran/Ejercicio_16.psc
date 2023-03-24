Proceso Indicar_día
	num=0;
	Escribir "Ingrese un número del 1 al 7"
	leer num
	
	Si num <= 7 Entonces
		
		segun num Hacer
			1:
				Escribir "Al número " num " le corresponde el día lunes"
			2:
				Escribir "Al número " num " le corresponde el día Martes"
			3:
				Escribir "Al número " num " le corresponde el día miercoles"
			4:
				Escribir "Al número " num " le corresponde el día jueves"
			5:
				Escribir "Al número " num " le corresponde el día viernes"
			6:
				Escribir "Al número " num " le corresponde el día sábado"
			7:
				Escribir "Al número " num " le corresponde el día domingo"
		FinSegun
	SiNo
		Escribir "El número ingresado no es válido"
	FinSi
FinProceso
