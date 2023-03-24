Proceso Ejercicio36
    Definir n, i, a, b, c Como Entero
    Escribir "Términos de Fibonacci: "
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
FinProceso
