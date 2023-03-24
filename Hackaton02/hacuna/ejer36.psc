Algoritmo Serie_Fibonacci
    Definir n, a, b, c Como Entero
    
    Escribir "Ingrese el número de términos de la serie de Fibonacci que desea calcular:"
    Leer n
    
    a <- 0
    b <- 1
    
    Escribir a
    Escribir b
    
    Para i <- 3 Hasta n Hacer
        c <- a + b
        Escribir c
        a <- b
        b <- c
    FinPara
    
FinAlgoritmo
