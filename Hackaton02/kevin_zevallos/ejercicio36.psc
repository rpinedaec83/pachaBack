Algoritmo ejercicio36
	Escribir "Ingrese la cantidad de términos de la serie de Fibonacci que desea obtener:"
    Leer n
	
    a <- 0
    b <- 1
    Escribir a
	
    Para i <- 1 Hasta n-1 Con Paso 1 Hacer
        c <- a + b
        Escribir c
        a <- b
        b <- c
    FinPara


FinAlgoritmo

