Algoritmo ejercicio17
    Definir hora, minuto, segundo como Entero
	
    Escribir "Ingrese la hora actual (formato 24 horas):"
    Leer hora
    Escribir "Ingrese el minuto actual:"
    Leer minuto
    Escribir "Ingrese el segundo actual:"
    Leer segundo
	
    segundo <- segundo + 1
	
    Si segundo = 60 Entonces
        segundo <- 0
        minuto <- minuto + 1
    FinSi
	
    Si minuto = 60 Entonces
        minuto <- 0
        hora <- hora + 1
    FinSi
	
    Si hora = 24 Entonces
        hora <- 0
    FinSi
	
    Escribir "La hora con el segundo adicional es: ", hora, ":", minuto, ":", segundo
	
FinAlgoritmo