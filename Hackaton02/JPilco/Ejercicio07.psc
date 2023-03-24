//Hacer un algoritmo en Pseint para una tienda de helado que da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:
//Tipo A 10% de descuento
//Tipo B 15% de descuento
//Tipo C 20% de descuento
Proceso Ejercicio07
	Definir A, B, C,X,descuento Como Caracter
	Escribir "Ingrese que tipo de membresia tiene: "
	Leer X
	Si X==A Entonces
		descuento="10%"
	SiNo
		Si X==B Entonces
			descuento="15%"
		SiNo
			descuento="20%"
		Fin si
	Fin Si
	Escribir "El descuento por la membresia : " X " es: " descuento  
	
FinProceso
