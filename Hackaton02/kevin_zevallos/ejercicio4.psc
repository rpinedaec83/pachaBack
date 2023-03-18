Algoritmo ejercicio4
    // Declarar variables
    Definir num1, num2, num3 Como Entero
	
    // Pedir tres números
    Escribir "Ingrese el primer número: "
    Leer num1
    Escribir "Ingrese el segundo número: "
    Leer num2
    Escribir "Ingrese el tercer número: "
    Leer num3
	
    // Ordenar los números de menor a mayor
    Si num1 <= num2 y num1 <= num3 Entonces
        Si num2 <= num3 Entonces
            Escribir num1, ", ", num2, ", ", num3
        SiNo
            Escribir num1, ", ", num3, ", ", num2
        FinSi
    SiNo
        Si num2 <= num1 y num2 <= num3 Entonces
            Si num1 <= num3 Entonces
                Escribir num2, ", ", num1, ", ", num3
            SiNo
                Escribir num2, ", ", num3, ", ", num1
            FinSi
        SiNo
            Si num1 <= num2 Entonces
                Escribir num3, ", ", num1, ", ", num2
            SiNo
                Escribir num3, ", ", num2, ", ", num1
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo

