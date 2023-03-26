Algoritmo ejercicio5
    // Declarar variables
    Definir num_zapatos Como Entero
    Definir precio_zapato, total_sin_descuento, descuento, total_con_descuento Como Real
	
    // Asignar el precio del zapato
    precio_zapato = 80
	
    // Pedir el número de zapatos
    Escribir "Ingrese el número de zapatos que desea comprar: "
    Leer num_zapatos
	
    // Calcular el total sin descuento
    total_sin_descuento = num_zapatos * precio_zapato
	
    // Determinar el descuento
    Si num_zapatos > 30 Entonces
        descuento = 0.4
    SiNo
        Si num_zapatos > 20 Entonces
            descuento = 0.2
        SiNo
            Si num_zapatos > 10 Entonces
                descuento = 0.1
            SiNo
                descuento = 0
            FinSi
        FinSi
    FinSi
	
    // Calcular el total con descuento
    total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)
	
    // Mostrar el resultado
    Escribir "El precio de cada zapato es: $", precio_zapato
    Escribir "El total de la compra sin descuento es: $", total_sin_descuento
    Escribir "El descuento que se aplicará es del: ", descuento * 100, "%"
    Escribir "El total de la compra con descuento es: $", total_con_descuento
	
FinAlgoritmo

