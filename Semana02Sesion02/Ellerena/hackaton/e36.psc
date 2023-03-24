Algoritmo e36
    Definir n, i, t1, t2, siguiente Como Entero
    
    Escribir "Ingrese el número de términos a mostrar: "
    Leer n
    
    Escribir "Serie de Fibonacci:"
    
    t1 <- 0
    t2 <- 1
    
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir t1
        siguiente <- t1 + t2
        t1 <- t2
        t2 <- siguiente
    FinPara
    
FinAlgoritmo
