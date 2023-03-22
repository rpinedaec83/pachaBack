Proceso Continuar_programa
	
	respuesta=""
	Repetir
		
        Escribir "¿Desea continuar con el programa? (Si/No)"
        Leer respuesta
        Si respuesta == "Si" o respuesta =="No" Entonces
		Segun respuesta Hacer
			"Si":
				Escribir "El programa continúa ejecutándose..."
			"No":
				Escribir "El programa se cerrará ahora."
		FinSegun
	SiNo
		Escribir "Respuesta inválida. Intente nuevamente."	
	FinSi
	Hasta Que respuesta = "No"		
FinProceso
