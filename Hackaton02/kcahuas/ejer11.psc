Algoritmo ejer11
	//Hacer un algoritmo en Pseint que lea tres números y diga cuál es el mayor.
	Definir num1, num2, num3, mayor Como Entero
    Escribir "Ingrese el primer número: "
    Leer num1
    Escribir "Ingrese el segundo número: "
    Leer num2
    Escribir "Ingrese el tercer número: "
    Leer num3
    Si num1 > num2 y num1 > num3 Entonces
        mayor = num1
    SiNo Si num2 > num3  y num2> num1 Entonces
			mayor = num2
		SiNo si num3 >num1 y num3>num2 Entonces
				mayor=num3
			FinSi
			
		FinSi
		
		FinSi
	
		Escribir "El número mayor es: ", mayor
FinAlgoritmo
