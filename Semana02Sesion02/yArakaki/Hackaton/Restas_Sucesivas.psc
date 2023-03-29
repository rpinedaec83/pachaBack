Proceso Restas_Sucesivas
    Definir dividendo, divisor, cociente, resto como Entero
	
    Escribir "Ingrese el dividendo:"
    Leer dividendo
    Escribir "Ingrese el divisor:"
    Leer divisor
	
    cociente <- 0
    resto <- dividendo
	
    Mientras resto >= divisor Hacer
        resto <- resto - divisor
        cociente <- cociente + 1
    FinMientras
	
    Escribir "El cociente es: ", cociente
    Escribir "El resto es: ", resto
FinProceso
