Proceso sin_titulo
	Escribir "¿Desea convertir centimetros a pulgadas o libras a pulgadas?"
	Escribir "digite 1 para centimetros a pulgadas o 2 para libras a kilogramos"
	leer opcion_elegida
	si opcion_elegida < 3 y opcion_elegida > 0 Entonces
		segun opcion_elegida Hacer
			caso 1:
				Escribir "Ingrese la distancia en centimetros"
				Leer distancia
				pulgadas = distancia / 2.54
				Escribir "Las pulgadas son: " pulgadas
			caso 2:
				Escribir "Ingrese el peso en libras"
				Leer peso
				kilo = peso / (1 / 2.21)
				Escribir "Los kilogramos son: " kilo
			De Otro Modo:
				Escribir "no es una opcion valida"
		FinSegun
	SiNo
		Escribir "no es una opcion valida"
	FinSi
FinProceso
