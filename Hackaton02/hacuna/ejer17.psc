Algoritmo HoraConSegundo
	
	Definir horas, minutos, segundos, tiempo como entero
	Definir horasNuevas, minutosNuevos, segundosNuevos como real
	
	Escribir "Ingrese la hora actual en formato de 24 horas separando horas, minutos y segundos por dos puntos (por ejemplo, 15:30:45):"
	Leer horas, minutos, segundos
	
	tiempo <- (horas * 3600) + (minutos * 60) + segundos
	tiempo <- tiempo + 1
	
	horasNuevas <- trunc(tiempo / 3600)
	minutosNuevos <- trunc((tiempo % 3600) / 60)
	segundosNuevos <- tiempo % 60
	
	Escribir "La hora dentro de un segundo será:", horasNuevas, ":", minutosNuevos, ":", segundosNuevos
	
FinAlgoritmo
