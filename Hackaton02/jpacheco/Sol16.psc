Algoritmo sin_titulo
	//16.-Hacer un algoritmo en Pseint que lea un número y según ese número, indique el día que corresponde.
	Escribir "Ingrese un día del 1 al 7";
	Leer dia;
	
	si (dia = 1) Entonces
		Escribir "Lunes";
	SiNo
		si (dia = 2) Entonces
			Escribir "Martes";
		SiNo
			si (dia = 3) Entonces
				Escribir "Miércoles";
			SiNo
				si (dia = 4) Entonces
					Escribir "Jueves";
				SiNo
					si (dia = 5) Entonces
						Escribir "Viernes";
					SiNo
						si (dia = 6) Entonces
							Escribir "Sábado";
						SiNo
							si (dia = 7) Entonces
								Escribir "Domingo";
							SiNo
								Escribir "Día inválido";
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
