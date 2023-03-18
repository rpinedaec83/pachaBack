Algoritmo ejercicio21
	Definir num1, num2, num3, num4 Como Entero
	Definir contador_pares, mayor Como Entero
	
	Escribir "Ingrese el primer número: "
	Leer num1
	
	Escribir "Ingrese el segundo número: "
	Leer num2
	
	Escribir "Ingrese el tercer número: "
	Leer num3
	
	Escribir "Ingrese el cuarto número: "
	Leer num4
	
	mayor <- num1
	
	Si num2 > mayor Entonces
		mayor <- num2
	FinSi
	
	Si num3 > mayor Entonces
		mayor <- num3
	FinSi
	
	Si num4 > mayor Entonces
		mayor <- num4
	FinSi
	
	contador_pares <- 0
	
	Si num1 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Si num2 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Si num3 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Si num4 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Escribir "La cantidad de números pares es: ", contador_pares
	Escribir "El número mayor es: ", mayor
	
	Si num3 MOD 2 = 0 Entonces
		Escribir "El cuadrado del segundo número es: ", num2 * num2
	FinSi
	
	Si num1 < num4 Entonces
		media <- (num1 + num2 + num3 + num4) / 4
		Escribir "La media de los 4 números es: ", media
	FinSi
	
	Si num2 > num3 Entonces
 ador_pares <- contador_pares + 1
	FinSi
	
	Si num2 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Si num3 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Si num4 MOD 2 = 0 Entonces
		contador_pares <- contador_pares + 1
	FinSi
	
	Escribir "La cantidad de números pares es: ", contador_pares
	Escribir "El número mayor es: ", mayor
	
FinAlgoritmo