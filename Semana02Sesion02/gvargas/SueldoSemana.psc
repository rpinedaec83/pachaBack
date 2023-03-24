Algoritmo SueldoSemana
	tipo = 0
	cant = 0
	sueldo = 0
	Escribir "Escriba el tipo de empleado (1) cajero (2) servido (3) preparador de mezclas (4) mantenimiento: "
	Leer tipo
	Escribir "Indique la cantidad de días que trabajo: "
	Leer cant
	Si cant <= 6 y cant >= 1 Entonces
		Segun tipo Hacer
			1:
				sueldo = 56*cant
				Escribir "Esa semana se le tiene que pagar: " sueldo " dolares"
			2:
				sueldo = 64*cant
				Escribir "Esa semana se le tiene que pagar: " sueldo " dolares"
			3:
				sueldo = 80*cant
				Escribir "Esa semana se le tiene que pagar: " sueldo " dolares"
			4:
				sueldo = 48*cant
				Escribir "Esa semana se le tiene que pagar: " sueldo " dolares"
		FinSegun
	SiNo
		Escribir "Solo se puede trabajar hasta seis días por semana"
	FinSi
FinAlgoritmo
