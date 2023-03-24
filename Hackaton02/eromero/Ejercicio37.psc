Proceso Ejercicio37
    Escribir "Primer número: "
    Leer a
    Escribir "Segundo número: "
    Leer b
    mientras b <> 0 hacer
        r <- a mod b
        a <- b
        b <- r
    fin mientras
    Escribir "M.C.D: ", a
FinProceso