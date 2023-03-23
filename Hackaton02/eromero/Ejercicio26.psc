Proceso Ejercicio26
    Escribir "Introduce el dividendo:"
    Definir dividendo Como Entero
    Leer dividendo
	
    Escribir "Introduce el divisor:"
    Definir divisor Como Entero
    Leer divisor
	
    Definir cociente Como Entero
    Definir resto Como Entero
	
    cociente <- 0
    resto <- dividendo
	
    Mientras resto >= divisor Hacer
        resto <- resto - divisor
        cociente <- cociente + 1
    FinMientras
	
    Escribir "El cociente es:", cociente
    Escribir "El resto es:", resto
FinProceso
