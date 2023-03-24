Algoritmo ejercicio35
	Definir mayor como entero
    Definir menor como entero
    
    Escribir "Ingrese 20 números:"
    
    Para i <- 1 hasta 20 hacer
        Escribir "Número ", i, ":"
        Leer numero
        
        Si i = 1 entonces
            mayor <- numero
            menor <- numero
        SiNo
            Si numero > mayor entonces
                mayor <- numero
            SiNo
                Si numero < menor entonces
                    menor <- numero
                FinSi
            FinSi
        FinSi
        
    FinPara
    
    Escribir "El número mayor es: ", mayor
    Escribir "El número menor es: ", menor


FinAlgoritmo

