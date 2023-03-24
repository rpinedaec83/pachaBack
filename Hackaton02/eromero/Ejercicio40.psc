Proceso Ejercicio39
	Definir i, terminos como Entero
    Definir pi3, denominador como Real
    
    terminos <- 1000
    
    pi3 = 3.0
    i = 2
    
    Mientras i <= terminos*2 Hacer
        denominador = i*(i+1)*(i+2) 
        Si i Mod 4 = 2 Entonces
            pi3 = pi3 + 4.0/denominador  
        SiNo
            pi3 = pi3 - 4.0/denominador  
        FinSi
        
        i = i + 2 
    FinMientras
    
    Escribir "Pi: ", n, "términos es:", pi3
FinProceso
