Algoritmo ejercicio4
	//Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
	Definir n1,n2,n3,me,ma,in Como Entero
	Escribir "Ingrese tres numeros: " 
	Leer n1,n2,n3
	//el menor numero
	si (n1 < n2 y n1 < n3) Entonces
		me = n1
	FinSi
	Si (n2 < n1 y n2 < n1) Entonces
		me = n2
	FinSi
	Si (n3 < n1 y n3 < n1) Entonces
		me = n3
	FinSi
	Escribir me
	
	//el numero intermedio
	si ((n1 > n2 y n1 < n3) o (n1 < n2 y n1 > n3)) Entonces
		in=n1
	FinSi
	si ((n2 > n1 y n2 < n3) o (n2 < n1 y n2 > n3)) Entonces
		in=n2
	FinSi
	si ((n3 > n2 y n3 < n1) o (n3 < n2 y n3 > n1)) Entonces
		in=n3
	FinSi
	Escribir in
	
	//el numero mayor
	si (n1 > n2 y n1 > n3) Entonces
		ma=n1
	FinSi
	si (n2 > n1 y n2 > n3) Entonces
		ma=n2
	FinSi
	si (n3 > n1 y n3 > n2) Entonces
		ma=n3
	FinSi
	Escribir ma

FinProceso