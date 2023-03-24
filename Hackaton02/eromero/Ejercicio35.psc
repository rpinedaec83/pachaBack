Proceso Ejercicio35
	Definir i, num, maxNum, minNum Como Entero;
    Escribir "Ingresa el primer número:"
    Leer num
    maxNum<-num
    minNum<-num
    Para i<-2 Hasta 20 Con Paso 1 Hacer
        Escribir "Ingresa el siguiente número ", i, ":"
        Leer num
        Si num>maxNum Entonces
            maxNum<-num
        FinSi
        Si num<minNum Entonces
            minNum<-num
        FinSi
    FinPara
    Escribir "Número mayor: ", maxNum
    Escribir "Múmero menor: ", minNum
FinProceso
