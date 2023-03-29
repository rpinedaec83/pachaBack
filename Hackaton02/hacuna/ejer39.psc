Algoritmo AproximacionPi_GregoryLeibniz
	
    Definir n, signo, divisor, Pii como Real
    Pii <- 0
    signo <- 1
    divisor <- 1
    
    Escribir "Ingrese el valor de n para la aproximación de Pi:"
    Leer n;
    
    Para i <- 1 Hasta n Hacer
        Pii <- Pii + signo*(4/divisor)
        signo <- signo*(-1)
        divisor <- divisor + 2
    FinPara
    
    Escribir "El valor aproximado de Pi es:", Pii
    
FinAlgoritmo
