Algoritmo DiaSemana
	num = 0
	Escribir "Escriba el número: "
	Leer num
	Si num >= 1 y num <= 7 Entonces
		Segun num Hacer
			1:
				Escribir "Le corresponde el día lunes"
			2:
				Escribir "Le corresponde el día martes"
			3:
				Escribir "Le corresponde el día miércoles"
			4:
				Escribir "Le corresponde el día jueves"
			5:
				Escribir "Le corresponde el día viernes"
			6:
				Escribir "Le corresponde el día sábado"
			7:
				Escribir "Le corresponde el día domingo"
		FinSegun
	SiNo
		Escribir "El número está fuera de rango"
	FinSi
FinAlgoritmo
