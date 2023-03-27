Algoritmo Aproximacion_Pi
    Definir n Como Entero
    Definir pi1 Como Real
    pi1 <- 0
    Escribir "Ingrese un valor para n:"
    Leer n
    Para i = 0 Hasta n Con Paso 1 Hacer
        pi1 <- pi1 + ((-1)^i)*(4/(2*i+1))
    FinPara
    Escribir "La aproximación de pi es: ", pi
FinAlgoritmo
