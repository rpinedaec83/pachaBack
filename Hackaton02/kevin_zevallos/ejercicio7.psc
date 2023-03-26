Algoritmo Descuento_Tienda_Helado
    // Declarar variables
    Definir precio_helado, precio_final Como Real
    Definir tipo_membresia Como Caracter
	
    // Pedir el precio del helado
    Escribir "Ingrese el precio del helado: "
    Leer precio_helado
	
    // Pedir el tipo de membresía
    Escribir "Ingrese el tipo de membresía (A, B o C): "
    Leer tipo_membresia
	
    // Calcular el precio final con descuento
    Si tipo_membresia = "A" Entonces
        precio_final = precio_helado * 0.9
    SiNo Si tipo_membresia = "B" Entonces
			precio_final = precio_helado * 0.85
		SiNo Si tipo_membresia = "C" Entonces
				precio_final = precio_helado * 0.8
			SiNo
				Escribir "El tipo de membresía ingresado es inválido. No se aplicará ningún descuento."
				precio_final = precio_helado
			FinSi
		FinSi
	FinSi	
	// Mostrar el resultado
	Escribir "El precio final con descuento es de: $", precio_final
FinAlgoritmo
