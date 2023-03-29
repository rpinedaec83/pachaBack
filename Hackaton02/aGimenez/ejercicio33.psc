Proceso ejercicio33
	respuesta = 'x'
	Repetir
		Escribir "Ingrese si->s, o no->"
		leer respuesta 
		si respuesta = 's' Entonces
			Escribir "El programa se continua ejecutando"
		SiNo
			Escribir "El programa se va a cerrar"
		FinSi
	Hasta Que respuesta == 'n'
FinProceso
