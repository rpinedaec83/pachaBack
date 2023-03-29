Proceso Ejercicio38
	Definir n, i como Entero
    Definir pi2, termino como Real
    
    n <- 1000
    
    pi2 <- 0
    
    Para i <- 0 Hasta n-1 Con Paso 1 Hacer
        termino <- 4.0 / (2 * i + 1)
        Si (i Mod 2 = 0) Entonces
            pi2 <- pi2 + termino
        SiNo
            pi2 <- pi2 - termino
        FinSi
    FinPara
    
    Escribir "Pi: ", n, "términos es:", pi2
FinProceso
